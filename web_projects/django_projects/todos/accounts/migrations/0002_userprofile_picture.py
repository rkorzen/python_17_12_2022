# Generated by Django 4.1.6 on 2023-02-25 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="userprofile",
            name="picture",
            field=models.ImageField(blank=True, null=True, upload_to="users/pictures/"),
        ),
    ]
