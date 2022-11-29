from django.shortcuts import render
from .models import Product, Input
from .forms import InputForm

def index(request):
    form = InputForm()
    context_dict = {}
    bill_spend = Product.objects.filter(
        ProductCategory='Bills').order_by('-ProductPrice')
    context_dict['bill_product'] = bill_spend
    food_spend = Product.objects.filter(
        ProductCategory='Food').order_by('-ProductPrice')
    context_dict['food_product'] = food_spend
    subscription_spend = Product.objects.filter(
        ProductCategory='Subscriptions').order_by('-ProductPrice')
    context_dict['sub_product'] = subscription_spend
    restaurant_spend = Product.objects.filter(
        ProductCategory='Restaurants').order_by('-ProductPrice')
    context_dict['rest_product'] = restaurant_spend
    alcohol_spend = Product.objects.filter(
        ProductCategory='Alcohol').order_by('-ProductPrice')
    context_dict['alcohol_product'] = alcohol_spend
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            request.session['salary_input'] = form.cleaned_data['salary_input']
            salary_input = request.session['salary_input']
            return results(request, salary_input)
        else:
            print(form.errors)
    context_dict['form'] = form
    return render(request, 'reboot/index.html', context_dict)


def results(request, salary_input):
    bill_spend = Product.objects.filter(
        ProductCategory='Bills').order_by('-ProductPrice')
    context_dict = {'bill_product': bill_spend}
    food_spend = Product.objects.filter(
        ProductCategory='Food').order_by('-ProductPrice')
    context_dict['food_product'] = food_spend
    subscription_spend = Product.objects.filter(
        ProductCategory='Subscriptions').order_by('-ProductPrice')
    context_dict['sub_product'] = subscription_spend
    restaurant_spend = Product.objects.filter(
        ProductCategory='Restaurants').order_by('-ProductPrice')
    context_dict['rest_product'] = restaurant_spend
    alcohol_spend = Product.objects.filter(
        ProductCategory='Alcohol').order_by('-ProductPrice')
    context_dict['alcohol_product'] = alcohol_spend
    context_dict['salary'] = salary_input
    salary = salary_input
    context_dict['bill_spend'] = round(total(bill_spend), 2)
    context_dict['food_spend'] = round(total(food_spend), 2)
    context_dict['sub_spend'] = round(total(subscription_spend), 2)
    context_dict['rest_spend'] = round(total(restaurant_spend), 2)
    context_dict['alcohol_spend'] = round(total(alcohol_spend), 2)
    context_dict['bill_percent'] = percent(context_dict['bill_spend'], salary)
    context_dict['food_percent'] = percent(context_dict['food_spend'], salary)
    context_dict['sub_percent'] = percent(context_dict['sub_spend'], salary)
    context_dict['rest_percent'] = percent(context_dict['rest_spend'], salary)
    context_dict['alcohol_percent'] = percent(context_dict['alcohol_spend'], salary)
    spare = round(salary - (context_dict['bill_spend'] + context_dict['food_spend'] +
                                            context_dict['sub_spend'] + context_dict['rest_spend'] +
                                            context_dict['alcohol_spend']), 2)

    if spare > 0:
        context_dict['message'] = "You have the following left over at the end of the month £" + str(spare) +"."
    else:
        context_dict['message'] = "You are currently spending more than you are bring in. Please check out our help page for advice on what to do next."
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
    Categories = ["Misc", "Subscriptions"]

    for product in products:
        productName.append(product.ProductName)
        productPriceAppended = float(product.ProductPrice)
        productPrice.append(productPriceAppended)

        if product.ProductCategory == "MiscSpend":
            productSavingsMisc.append(product.ProductName)
        elif product.ProductCategory == "Subscriptions":
            productSavingsSubscriptions.append(product.ProductName)

    print(productSavingsMisc)
    print(productSavingsSubscriptions)

    return render(request, "reboot/savings.html", {'product': products,  'labels': Categories, 'data': [len(productSavingsMisc), len(productSavingsSubscriptions)], 'colors': ["#FF4136", "#0074D9"]})


def savings1(request):
    products = Product.objects.all()

    return render(request, "reboot/savings.html", {'product': products,  'labels': ['F', 'M'], 'data': [52, 82], 'colors': ["#FF4136", "#0074D9"]
                                                   })
