import logging

from flask import Flask, request, render_template

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)


dane = [
    {},{}
]

@app.route("/")
def home():
    return f"Hello Flask!"


@app.route("/message/", methods=["GET", "POST"])
def post_message():
    if request.method == "POST":
        logger.info(f"{request.json}")
        return "POST OK"
    else:
        return "OK"


@app.route("/<name>/")
def home2(name):
    return f"Hello {name}!"


@app.route("/maths/<op>/<int:a>/<int:b>/")
def kalk(op, a, b):
    # a, b = int(a), int(b)
    if op == "add":
        return f"{a + b}"


@app.route("/examples/template/")
def template_view():
    return render_template(
        "content.html",
        data=["ala", "kot"],
        oceny=[["a", "b", "c"], 2, 3, 4, 5],
        dane={"psy": 100, "słonie": 1}
    )


@app.route("/examples/xxx/")
def template_view2():
    return render_template(
        "content.html",
        data=[1, 2, 3, 4, 5],
        oceny=[0, 0, 0, 0, 0, 0],
        dane=[0, 0, 0, 0, 0]
    )


@app.route("/about/")
def about():
    text = "jakis dlugoi opis ..."
    return render_template(
        "about.html",
        text=text
    )


@app.route("/bizcard/")
def bizcard():
    person = {
        "name": "Rafał",
        "last_name": "Korzeniewski",
        "age": 42,
        "bio": "Fizyk muzyk puzonista"
    }

    return render_template(
        "card.html",
        person=person
    )


@app.route("/formularz/", methods=["GET", "POST"])
def my_form():
    if request.method == "POST":
        data = request.form
        name = data["name"]
        last_name = data["lastname"]
        gender = data["gender"]
        hobby = data.getlist("hobby")

        logger.info(f"{name} {last_name} {gender} {hobby}")
        return "POST OK"
    else:
        return render_template("formularz.html")


if __name__ == "__main__":
    app.run(debug=True)
