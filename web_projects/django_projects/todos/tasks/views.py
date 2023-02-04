from django.shortcuts import render

from tasks.services import Todos


def tasks_list(request):

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
        {"todos": tasks}
    )


def task_details(request, id):
    with Todos() as todos:
        task = todos.get(id)
    return render(
        request,
        "tasks/details.html",
        {"todo": task}
    )
