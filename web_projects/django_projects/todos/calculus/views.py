from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def calculator(request, op, a, b):
    if op == "add":
        result = a + b

    elif op == "sub":
        result = a - b

    elif op == "div":
        result = a / b

    elif op == "mul":
        result = a * b

    return HttpResponse(result)
