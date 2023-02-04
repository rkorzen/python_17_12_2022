from django.urls import path
from .views import calculator, home

urlpatterns = [
    path("", home),
    path("<op>/<int:a>/<int:b>/", calculator)
]
