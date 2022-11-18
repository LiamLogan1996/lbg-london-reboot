from django.shortcuts import render,redirect
from hello.models import Product



def show(request):
    products = Product.objects.all()
    return render(request,"show.html",{'product':products})