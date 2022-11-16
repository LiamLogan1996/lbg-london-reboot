from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context_dict = { 'example' : "Transaction group: bills, transation: Glasow Council Rent, value: 450.00" }
    return render(request, 'reboot/index.html', context=context_dict)