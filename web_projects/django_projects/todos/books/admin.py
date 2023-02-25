from django.contrib import admin
from .models import Book, Author, AuthorProfile


# Register your models here.

# class AuthorInline(admin.StackedInline):
#     model = Author

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ["title", "author"]
    search_fields = ["title", "author", "description"]
    # inlines = [AuthorInline]

class AuthorProfileInline(admin.StackedInline):
    model = AuthorProfile


class BookInline(admin.TabularInline):
    model = Book
    extra = 1


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    inlines = [AuthorProfileInline, BookInline]

# @admin.register(AuthorProfile)
# class AuthorProfileAdmin(admin.ModelAdmin):
#     pass
