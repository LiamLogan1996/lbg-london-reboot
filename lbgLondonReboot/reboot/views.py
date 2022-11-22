from django.shortcuts import render
<<<<<<< HEAD
from reboot.models import Product
from django.db import router, transaction
from django.shortcuts import render
from decimal import ROUND_HALF_DOWN, Decimal
from django.core.management.base import BaseCommand
from django.core.cache import cache


def index(request):
    input_salary = request.POST.get(int, None)
    input_inflation = request.POST.get(int, None)

    context_dict = salary_inflation_check(input_salary, input_inflation)

    return render(request, 'reboot/index.html', context=context_dict)


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        cache.clear()
        self.stdout.write('Cleared cache\n')


def results(request):
    context_dict = {}
    return render(request, 'reboot/results.html', context=context_dict)


def savings(request):
    products = Product.objects.all()
    productName = []
    productPrice = []

    for product in products:
        productName.append(product.ProductName)
        productPriceAppended = float(product.ProductPrice)
        productPrice.append(productPriceAppended)

    print(productName)
    print(productPrice)

    return render(request, "reboot/savings.html", {'product': products,  'labels': productName, 'data': productPrice, 'colors': ["#FF4136", "#0074D9"]})


def savings1(request):
    products = Product.objects.all()

    return render(request, "reboot/savings.html", {'product': products,  'labels': ['F', 'M'], 'data': [52, 82], 'colors': ["#FF4136", "#0074D9"]
                                                   })


def salary_inflation_check(x, y):
    context_dict = {}
    if isinstance(x, int) or isinstance(x, float):
        if x > 0:
            context_dict['salary'] = x
        else:
            print("You have entered a negative salary")
    else:
        print("You have not entered a number")

    if isinstance(y, int) or isinstance(y, float):
        if y > 0:
            context_dict['inflation'] = y
=======
from .models import Input, Product
from .forms import InputForm


def index(request):
    form = InputForm()
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            form.save()
            return results(request)
>>>>>>> origin/frontend
        else:
            print(form.errors)
    return render(request, 'reboot/index.html', {'form': form})

<<<<<<< HEAD
    return (context_dict)
=======
def results(request):
    bill_spend = Product.objects.filter(ProductCategory='Bills').order_by('-ProductPrice')
    context_dict = {'bill_product': bill_spend}
    misc_spend = Product.objects.filter(ProductCategory='MiscSpend').order_by('-ProductPrice')
    context_dict['misc_product'] = misc_spend
    subscription_spend = Product.objects.filter(ProductCategory='Subscriptions').order_by('-ProductPrice')
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

def saving(request):

    return render(request, 'reboot/saving.html', {})

def inflation(request):

    return render(request, 'reboot/inflation.html', {})

def total(spending):
    total = 0
    for spend in spending:
        total += spend.ProductPrice
    return total

def percent(a, b):
    return(round((a/b)*100, 2))
>>>>>>> origin/frontend
