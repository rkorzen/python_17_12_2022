# Generated by Django 4.1.6 on 2023-02-25 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tags", "0001_initial"),
        ("posts", "0002_alter_post_author"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="tags",
            field=models.ManyToManyField(to="tags.tag"),
        ),
    ]
