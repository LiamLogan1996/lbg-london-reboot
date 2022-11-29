from django.shortcuts import render
from .models import Input, Product
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
    allProducts = Product.objects.all()
    bill_itemInfo = {}
    food_itemInfo = {}
    alcohol_itemInfo = {}
    subscriptions_itemInfo = {}

    bill_spend = Product.objects.filter(
        ProductCategory='Bills').order_by('-ProductPrice')
    context_dict = {'bill_product': bill_spend}
    food_spend = Product.objects.filter(
        ProductCategory='Food').order_by('-ProductPrice')
    context_dict['food_product'] = food_spend
    alcohol_spend = Product.objects.filter(
        ProductCategory='Alcohol').order_by('-ProductPrice')
    context_dict['alcohol_product'] = alcohol_spend
    subscription_spend = Product.objects.filter(
        ProductCategory='Subscriptions').order_by('-ProductPrice')
    context_dict['sub_product'] = subscription_spend
    
    user_input = Input.objects.last()
    salary = (user_input.salary_input)
    inflation = (user_input.inflation_input)
    context_dict['salary'] = salary
    context_dict['inflation'] = inflation
    context_dict['bill_spend'] = round(total(bill_spend), 2)
    context_dict['food_spend'] = round(total(food_spend), 2)
    context_dict['alcohol_spend'] = round(total(alcohol_spend), 2)
    context_dict['sub_spend'] = round(total(subscription_spend), 2)
    context_dict['bill_percent'] = percent(context_dict['bill_spend'], salary)
    context_dict['alcohol_percent'] = percent(context_dict['alcohol_spend'], salary)
    context_dict['sub_percent'] = percent(context_dict['sub_spend'], salary)
    context_dict['food_percent'] = percent(context_dict['food_spend'], salary)

    for prod in allProducts:
        if prod.ProductCategory == "Bills":            
            bill_itemInfo[prod.ProductName] = [prod.ProductPrice, round(prod.ProductPrice * 1.117, 2)] #11/7% increase
            bill_table = [[key, values[0], values[1]] for key, values in bill_itemInfo.items()]

        elif prod.ProductCategory == "Food":
            food_itemInfo[prod.ProductName] = [prod.ProductPrice, round(prod.ProductPrice * 1.164, 2)] #16.4% increase
            food_table = [[key, values[0], values[1]] for key, values in food_itemInfo.items()]
    
        elif prod.ProductCategory == "Alcohol":
            alcohol_itemInfo[prod.ProductName] = [prod.ProductPrice, round(prod.ProductPrice * 1.062, 2)] #6.2% increase
            alcohol_table = [[key, values[0], values[1]] for key, values in alcohol_itemInfo.items()]

        elif prod.ProductCategory == "Subscriptions":
            subscriptions_itemInfo[prod.ProductName] = [prod.ProductPrice, round(prod.ProductPrice * 1.051, 2)] #5.1% increase
            sub_table = [[key, values[0], values[1]] for key, values in subscriptions_itemInfo.items()]

    return render(request, 'reboot/inflation.html', {'sub_percent': context_dict['sub_percent'], 'alcohol_percent': context_dict['alcohol_percent'], 'food_percent': context_dict['food_percent'], 'alcohol_spend' :context_dict['alcohol_spend'], 'sub_spend' :context_dict['sub_spend'], 'food_spend': context_dict['food_spend'], 'bill_total': context_dict['bill_spend'], 'bill_percent': context_dict['bill_percent'] , 'inflation': inflation, 'salary': salary, 'bill_table': bill_table, 'food_table':food_table, 'alcohol_table': alcohol_table, 'sub_table': sub_table})


def total(spending):
    total = 0
    for spend in spending:
        total += spend.ProductPrice
    return total


def inflation_calculation(products, inflation_input):
    #products is the array of all products with an associated cost
    #inflation_input is the user inputted inflation
    all_inflation = {}
    for x in products:
        all_inflation[x] = round(x/100 * inflation_input, 2)
    return all_inflation



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
