# Generated by Django 4.1.6 on 2023-02-25 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("books", "0007_book_created_book_modified"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="cover",
            field=models.ImageField(
                blank=True, null=True, upload_to="books/covers/%Y/%m/"
            ),
        ),
    ]
