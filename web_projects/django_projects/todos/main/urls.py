from django.urls import path
from .views import hello

urlpatterns = [
    path("", hello),
    path("hello/", hello),
    path("hello/<name>/", hello),
]
