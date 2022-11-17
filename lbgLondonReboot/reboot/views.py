from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    input_salary = request.POST.get(int, None)
    input_inflation = request.POST.get(int, None)

    context_dict = salary_inflation_check(input_salary, input_inflation)

    return render(request, 'reboot/index.html', context=context_dict)

def results(request):

    context_dict = {}
    return render(request, 'reboot/results.html', context=context_dict)

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

    return(context_dict)