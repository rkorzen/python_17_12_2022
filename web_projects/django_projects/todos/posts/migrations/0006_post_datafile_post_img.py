# Generated by Django 4.1.6 on 2023-02-25 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0005_alter_post_tags"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="datafile",
            field=models.FileField(
                blank=True, null=True, upload_to="posts/files/%Y/%m/%d/"
            ),
        ),
        migrations.AddField(
            model_name="post",
            name="img",
            field=models.ImageField(
                blank=True, null=True, upload_to="posts/images/%Y/%m/%d/"
            ),
        ),
    ]
