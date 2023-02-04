from django.http import HttpResponse
from django.shortcuts import render
from calculus.services import handle_calculation, operations


# Create your views here.


def calculator(request, op, a, b):
    result = handle_calculation(op, a, b)
    return HttpResponse(result)

def home(request):
    # return HttpResponse(f"Dostępne operacje: {[x for x in operations]}")
    return render(
        request,
        "calculus/home.html",
        {}
    )