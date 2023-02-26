from flask import Flask, render_template, request
from db import todos

app = Flask(__name__)


@app.route("/")
def main():
    return render_template("main.html")


@app.route("/todos/", methods=["GET", "POST"])
def todos_list():

    if request.method == "POST":

        title = request.form.get("title")
        description = request.form.get("description")
        done = bool(request.form.get("done"))
        todo = {"title": title, "description": description, "done": done}
        todos.create(todo)

    return render_template("todos.html", todos=todos.all())


@app.route("/todos/<int:id>/")
def todo_details(id):
    todo = todos.get(id)
    return render_template("details.html", todo=todo)


if __name__ == "__main__":
    app.run(debug=True)
