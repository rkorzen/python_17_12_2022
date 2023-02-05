from django.urls import path

from books.views import book_list, book_details

urlpatterns = [
    path("", book_list),
    path("<int:id>", book_details)
]