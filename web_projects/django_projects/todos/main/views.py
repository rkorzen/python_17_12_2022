# from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def hello(request, name="World"):
    # return HttpResponse(f"Hello {name}!")
    return render(
        request=request,
        template_name="home.html",
        context={"name": name}
    )