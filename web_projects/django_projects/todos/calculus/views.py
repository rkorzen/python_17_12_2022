from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def add(a, b): return a + b


def mul(a, b): return a * b


def div(a, b): return a / b


def sub(a, b): return a - b


operations = {
    "add": add,
    "mul": mul,
    "sub": sub,
    "div": div
}


def calculator(request, op, a, b):
    if op in operations:
        result = operations[op](a, b)
    else:
        result = "Niedozwolona operacja"
    return HttpResponse(result)
