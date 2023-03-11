from django.urls import path
from snippets import views


urlpatterns = [
    path("snippets/", views.SnippetList.as_view()),
    path("snippets/<int:id>", views.SnippetDetial.as_view()),
]
