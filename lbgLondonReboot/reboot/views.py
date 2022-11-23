from django.shortcuts import render
from .models import Input, Product
from .forms import InputForm


def index(request):
    form = InputForm()
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            form.save()
            return results(request)
        else:
            print(form.errors)
    return render(request, 'reboot/index.html', {'form': form})


def results(request):
    bill_spend = Product.objects.filter(
        ProductCategory='Bills').order_by('-ProductPrice')
    context_dict = {'bill_product': bill_spend}
    misc_spend = Product.objects.filter(
        ProductCategory='MiscSpend').order_by('-ProductPrice')
    context_dict['misc_product'] = misc_spend
    subscription_spend = Product.objects.filter(
        ProductCategory='Subscriptions').order_by('-ProductPrice')
    context_dict['sub_product'] = subscription_spend
    user_input = Input.objects.last()
    salary = (user_input.salary_input)
    inflation = (user_input.inflation_input)
    context_dict['salary'] = salary
    context_dict['inflation'] = inflation
    context_dict['bill_spend'] = round(total(bill_spend), 2)
    context_dict['misc_spend'] = round(total(misc_spend), 2)
    context_dict['sub_spend'] = round(total(subscription_spend), 2)
    context_dict['bill_percent'] = percent(context_dict['bill_spend'], salary)
    context_dict['sub_percent'] = percent(context_dict['sub_spend'], salary)
    context_dict['misc_percent'] = percent(context_dict['misc_spend'], salary)

    return render(request, 'reboot/results.html', context_dict)


def inflation(request):

    return render(request, 'reboot/inflation.html', {})


def total(spending):
    total = 0
    for spend in spending:
        total += spend.ProductPrice
    return total


def percent(a, b):
    return (round((a/b)*100, 2))


def savings(request):
    products = Product.objects.all()
    productName = []
    productPrice = []
    productSavingsMisc = []
    productSavingsSubscriptions = []
    savingitems = {}
    totalsavings = 0
    miscTotal = 0
    subscrtotal = 0
    Categories = ["Misc (£'s)", "Subscriptions (£'s)"]

    for product in products:
        productName.append(product.ProductName)
        productPriceAppended = float(product.ProductPrice)
        productPrice.append(productPriceAppended)

        if product.ProductCategory == "MiscSpend":
            productSavingsMisc.append(product.ProductName)
            savingitems[product.ProductName] = product.ProductPrice
            miscTotal = miscTotal + product.ProductPrice
        elif product.ProductCategory == "Subscriptions":
            productSavingsSubscriptions.append(product.ProductName)
            savingitems[product.ProductName] = product.ProductPrice
            subscrtotal = subscrtotal + product.ProductPrice
    
    for productname, productprice in savingitems.items():
        totalsavings = totalsavings + productprice


    return render(request, "reboot/savings.html", {'product': products,  'labels': Categories, 'data': [miscTotal, subscrtotal], 'colors': ["#FF4136", "#0074D9"], 'wheresavings': savingitems, 'savings': savingitems, 'totalsavings': totalsavings})


def savings1(request):
    products = Product.objects.all()

    return render(request, "reboot/savings.html", {'product': products,  'labels': ['F', 'M'], 'data': [52, 82], 'colors': ["#FF4136", "#0074D9"]
                                                   })
