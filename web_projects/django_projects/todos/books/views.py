from django.shortcuts import render

from books.forms import BookForm
from books.models import Book


# Create your views here.

def book_list(request):
    books = Book.objects.all()

    if request.method == "POST":
        form = BookForm(data=request.POST)
        if form.is_valid():
            # Book.objects.create(**form.cleaned_data)
            form.save()

    form = BookForm()

    return render(
        request,
        "books/list.html",
        {"books": books, "form": form}
    )


def book_details(request, id):
    book = Book.objects.get(pk=id)
    if request.method == "POST":
        form = BookForm(instance=book, data=request.POST)
        if form.is_valid():
            # for field, value in form.cleaned_data.items():
            #     setattr(book, field, value)

            form.save()

    # form = BookForm(data=book.__dict__)
    form = BookForm(instance=book)

    return render(
        request,
        "books/details.html",
        {"book": book, "form": form}
    )