from django.http import HttpResponse
from django.shortcuts import render
from calculus.services import handle_calculation


# Create your views here.


def calculator(request, op, a, b):
    result = handle_calculation(op, a, b)
    return HttpResponse(result)
