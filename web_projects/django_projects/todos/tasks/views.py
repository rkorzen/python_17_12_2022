from django.shortcuts import render

from tasks.forms import TodoForm, TodoFormset
from tasks.models import Todo
from tasks.services import ModelTodosService as Todos


def tasks_list(request):

    form = TodoForm()
    formset = TodoFormset()

    if request.method == "POST":

        with Todos() as todos:
            title = request.POST.get("title")
            description = request.POST.get("description")
            done = request.POST.get("done", False)

            task = {
                "title": title,
                "description": description,
                "done": done
            }

            todo = todos.create(task)
            print("Utworzono todo", todo)

    with Todos() as todos:
        tasks = todos.all()

    return render(
        request,
        "tasks/list.html",
        {"todos": tasks, "form": form, "formset": formset}
    )


def task_details(request, id):

    if request.method == "POST":
        data = dict(request.POST)
        data.pop("csrfmiddlewaretoken")
        print(data)
        with Todos() as todos:
            data = {k: v[0] for k, v in data.items()}
            todos.update(id, data)

    with Todos() as todos:
        task = todos.get(id)
    return render(
        request,
        "tasks/details.html",
        {"todo": task}
    )


def add_task(request):

    if request.method == "POST":

        t = Todo.objects.create()

