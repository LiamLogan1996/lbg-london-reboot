from django.http import HttpResponse
from django.shortcuts import render
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
        else:
            print("You have entered a negative inflation")
    else:
        print("You have not entered a number")

    return (context_dict)
