# Generated by Django 4.1.6 on 2023-02-25 09:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("books", "0003_book_new_author"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="book",
            name="author",
        ),
    ]
