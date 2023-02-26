# Generated by Django 4.1.6 on 2023-02-05 11:03

from django.db import migrations, transaction
from tasks.services import TaskLoadData


def add_tasks(apps, schema_editor):
    with transaction.atomic():
        Todo = apps.get_model("tasks", "Todo")
        tld = TaskLoadData(klass=Todo)
        tld.insert()
    print("Done!")


def reverse_code(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ("tasks", "0002_alter_todo_done"),
    ]

    operations = [
        migrations.RunPython(add_tasks, reverse_code=reverse_code),
    ]
