from django.urls import path
from .views import hello, contact

urlpatterns = [
    path("", hello, name="home"),
    path("hello/", hello),
    path("hello/<name>/", hello),
    path("contact/", contact),
]
