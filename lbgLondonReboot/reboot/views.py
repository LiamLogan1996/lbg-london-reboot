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
            return results(request)
        else:
            print(form.errors)
    context_dict['form'] = form
    return render(request, 'reboot/index.html', context_dict)


def results(request):
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
    salary = request.session.get('salary_input')
    context_dict['salary'] = salary
    salary = salary
    context_dict['bill_spend'] = round(total(bill_spend), 2)
    context_dict['food_spend'] = round(total(food_spend), 2)
    context_dict['sub_spend'] = round(total(subscription_spend), 2)
    context_dict['rest_spend'] = round(total(restaurant_spend), 2)
    context_dict['alcohol_spend'] = round(total(alcohol_spend), 2)
    context_dict['bill_percent'] = percent(context_dict['bill_spend'], salary)
    context_dict['food_percent'] = percent(context_dict['food_spend'], salary)
    context_dict['sub_percent'] = percent(context_dict['sub_spend'], salary)
    context_dict['rest_percent'] = percent(context_dict['rest_spend'], salary)
    context_dict['alcohol_percent'] = percent(
        context_dict['alcohol_spend'], salary)
    spare = round(salary - (context_dict['bill_spend'] + context_dict['food_spend'] +
                            context_dict['sub_spend'] + context_dict['rest_spend'] +
                            context_dict['alcohol_spend']), 2)
    data = [context_dict['bill_spend'], context_dict['food_spend'], context_dict['sub_spend'],
            context_dict['rest_spend'], context_dict['alcohol_spend'], spare]
    labels = ['Bills', 'Food', 'Subscriptions',
              'Eating Out', 'Going Out', 'Savings']
    data = [838.86, 346.89, 115.06, 247.04, 103.33]
    data.append(spare)
    if spare > 0:
        context_dict['message'] = "You have the following left over at the end of the month ??" + \
            str(spare) + "."
    else:
        context_dict['message'] = "You are currently spending more than you are bring in. Please check out our help page for advice on what to do next."
    return render(request, 'reboot/results.html', {'labels': ['Bills', 'Food', 'Subscriptions', 'Eating Out', 'Going Out', 'Savings'], 'data': data, 'colors': ["#40bf40", "#00ff00", "#00ff55", "#009900", "#008000", "#004d00"],
                  'message': context_dict['message'], 'alcohol_percent': context_dict['alcohol_percent'], 'rest_percent': context_dict['rest_percent'], 'sub_percent': context_dict['sub_percent'],
        'food_percent': context_dict['food_percent'], 'bill_percent': context_dict['bill_percent'], 'sub_percent': context_dict['sub_percent'], 'salary': salary,
        'alcohol_spend': context_dict['alcohol_spend'], 'rest_spend': context_dict['rest_spend'], 'sub_spend': context_dict['sub_spend'],
                  'food_spend': context_dict['food_spend'], 'bill_spend': context_dict['bill_spend'], 'alcohol_product': context_dict['alcohol_product'],
                  'rest_product': context_dict['rest_product'], 'sub_product': context_dict['sub_product'], 'food_product': context_dict['food_product'], 'bill_product': context_dict['bill_product']})


def inflation(request):
    allProducts = Product.objects.all()
    bill_itemInfo = {}
    food_itemInfo = {}
    restaurant_itemInfo = {}
    alcohol_itemInfo = {}
    subscriptions_itemInfo = {}
    bill_total_inflation = 0.0
    food_total_inflation = 0.0
    restaurant_total_inflation = 0.0
    alcohol_total_inflation = 0.0
    sub_total_inflation = 0.0

    bill_spend = Product.objects.filter(
        ProductCategory='Bills').order_by('-ProductPrice')
    context_dict = {'bill_product': bill_spend}
    food_spend = Product.objects.filter(
        ProductCategory='Food').order_by('-ProductPrice')
    context_dict['food_product'] = food_spend
    restaurant_spend = Product.objects.filter(
        ProductCategory='Food').order_by('-ProductPrice')
    context_dict['restaurant_product'] = restaurant_spend
    alcohol_spend = Product.objects.filter(
        ProductCategory='Alcohol').order_by('-ProductPrice')
    context_dict['alcohol_product'] = alcohol_spend
    subscription_spend = Product.objects.filter(
        ProductCategory='Subscriptions').order_by('-ProductPrice')
    context_dict['sub_product'] = subscription_spend

    user_input = Input.objects.last()
    salary = request.session.get('salary_input')
    print(salary)
    context_dict['salary'] = salary
    context_dict['bill_spend'] = round(total(bill_spend), 2)
    context_dict['food_spend'] = round(total(food_spend), 2)
    context_dict['restaurant_spend'] = round(total(restaurant_spend), 2)
    context_dict['alcohol_spend'] = round(total(alcohol_spend), 2)
    context_dict['sub_spend'] = round(total(subscription_spend), 2)
    context_dict['bill_percent'] = percent(context_dict['bill_spend'], salary)
    context_dict['restaurant_spend'] = round(total(restaurant_spend), 2)
    context_dict['alcohol_percent'] = percent(
        context_dict['alcohol_spend'], salary)
    context_dict['sub_percent'] = percent(context_dict['sub_spend'], salary)
    context_dict['food_percent'] = percent(context_dict['food_spend'], salary)
    context_dict['restaurant_percent'] = percent(
        context_dict['restaurant_spend'], salary)

    for prod in allProducts:
        if prod.ProductCategory == "Bills":
            bill_itemInfo[prod.ProductName] = [prod.ProductPrice, round(
                prod.ProductPrice * 1.117, 2), round(prod.ProductPrice * 1.117, 2) - prod.ProductPrice]  # 11/7% increase
            bill_total_inflation += round(prod.ProductPrice *
                                          1.117, 2) - prod.ProductPrice
            bill_table = [[key, values[0], values[1], round(
                values[2], 2)] for key, values in bill_itemInfo.items()]

        elif prod.ProductCategory == "Food":
            food_itemInfo[prod.ProductName] = [prod.ProductPrice, round(
                prod.ProductPrice * 1.164, 2), round(prod.ProductPrice * 1.164, 2) - prod.ProductPrice]  # 16.4% increase
            food_total_inflation += round(prod.ProductPrice *
                                          1.164, 2) - prod.ProductPrice
            food_table = [[key, values[0], values[1], round(
                values[2], 2)] for key, values in food_itemInfo.items()]

        elif prod.ProductCategory == "Restaurants":
            restaurant_itemInfo[prod.ProductName] = [prod.ProductPrice, round(
                prod.ProductPrice * 1.087, 2), round(prod.ProductPrice * 1.096, 2) - prod.ProductPrice]  # 9.6% increase
            restaurant_total_inflation += round(
                prod.ProductPrice * 1.096, 2) - prod.ProductPrice
            restaurant_table = [[key, values[0], values[1], round(
                values[2], 2)] for key, values in restaurant_itemInfo.items()]

        elif prod.ProductCategory == "Alcohol":
            alcohol_itemInfo[prod.ProductName] = [prod.ProductPrice, round(
                prod.ProductPrice * 1.062, 2), round(prod.ProductPrice * 1.062, 2) - prod.ProductPrice]  # 6.2% increase
            alcohol_total_inflation += round(prod.ProductPrice *
                                             1.062, 2) - prod.ProductPrice
            alcohol_table = [[key, values[0], values[1], round(
                values[2], 2)] for key, values in alcohol_itemInfo.items()]

        elif prod.ProductCategory == "Subscriptions":
            subscriptions_itemInfo[prod.ProductName] = [prod.ProductPrice, round(
                prod.ProductPrice * 1.051, 2), round(prod.ProductPrice * 1.051, 2) - prod.ProductPrice]  # 5.1% increase
            sub_total_inflation += round(prod.ProductPrice *
                                         1.051, 2) - prod.ProductPrice
            sub_table = [[key, values[0], values[1], round(
                values[2], 2)] for key, values in subscriptions_itemInfo.items()]

    bill_data_now = bill_total_inflation
    bill_data_1y = bill_total_inflation*1.117
    food_data_now = food_total_inflation
    food_data_1y = bill_total_inflation*1.164
    rest_data_now = restaurant_total_inflation
    rest_data_1y = restaurant_total_inflation*1.096
    alc_data_now = alcohol_total_inflation
    alc_data_1y = alcohol_total_inflation*1.062
    sub_data_now = sub_total_inflation
    sub_data_1y = sub_total_inflation*1.051

    return render(request, 'reboot/inflation.html', {'labels': ['bill_current', 'bill_1y', 'food_current', 'food_1y', 'rest_current', 'rest_1y', 'alc_current', 'alc_1y', 'sub_current', 'sub_1y'], 'bill_data': [bill_data_now, bill_data_1y], 'food_data': [food_data_now, food_data_1y], 'restaurant_data': [rest_data_now, rest_data_1y], 'alc_data': [alc_data_now, alc_data_1y], 'sub_data': [sub_data_now, sub_data_1y], 'colors': ["#ccff99", "#ccff99", "#ccff99", "#ccff99", "#ccff99", "#ccff99", "#ccff99", "#ccff99", "#ccff99", "#ccff99"], 'sub_total_inflation': round(sub_total_inflation, 2), 'alcohol_total_inflation': round(alcohol_total_inflation, 2), 'restaurant_total_inflation': round(restaurant_total_inflation, 2),
                                                     'food_total_inflation': round(food_total_inflation, 2), 'bill_total_inflation': round(bill_total_inflation, 2), 'restaurant_table': restaurant_table,
                                                     'restaurant_spend': context_dict['restaurant_spend'], 'restaurant_percent': context_dict['restaurant_percent'], 'sub_percent': context_dict['sub_percent'], 'alcohol_percent': context_dict['alcohol_percent'], 'food_percent': context_dict['food_percent'], 'alcohol_spend': context_dict['alcohol_spend'], 'sub_spend': context_dict['sub_spend'], 'food_spend': context_dict['food_spend'], 'bill_total': context_dict['bill_spend'], 'bill_percent': context_dict['bill_percent'], 'inflation': inflation, 'salary': salary, 'bill_table': bill_table, 'food_table': food_table, 'alcohol_table': alcohol_table, 'sub_table': sub_table})


def total(spending):
    total = 0
    for spend in spending:
        total += spend.ProductPrice
    return total


def inflation_calculation(products, inflation_input):
    # products is the array of all products with an associated cost
    # inflation_input is the user inputted inflation
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
    Categories = ["Going Out (??'s)", "Subscriptions (??'s)"]

    for product in products:
        productName.append(product.ProductName)
        productPriceAppended = float(product.ProductPrice)
        productPrice.append(productPriceAppended)

        if product.ProductCategory == "Alcohol":
            productSavingsMisc.append(product.ProductName)
            savingitems[product.ProductName] = product.ProductPrice
            miscTotal = round(miscTotal + product.ProductPrice, 2)
        elif product.ProductCategory == "Subscriptions":
            productSavingsSubscriptions.append(product.ProductName)
            savingitems[product.ProductName] = product.ProductPrice
            subscrtotal = round(subscrtotal + product.ProductPrice, 2)

    for productname, productprice in savingitems.items():
        totalsavings = round(totalsavings + productprice, 2)

    return render(request, "reboot/savings.html", {'product': products,  'labels': Categories, 'data': [miscTotal, subscrtotal], 'colors': ["#40bf40", "#00ff00"], 'wheresavings': savingitems, 'savings': savingitems, 'totalsavings': totalsavings})


def savings1(request):
    products = Product.objects.all()

    return render(request, "reboot/savings.html", {'product': products,  'labels': ['F', 'M'], 'data': [52, 82], 'colors': ["#FF4136", "#0074D9"]
                                                   })
