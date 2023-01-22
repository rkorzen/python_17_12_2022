import logging

from flask import Flask, request, render_template

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)


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



if __name__ == "__main__":
    app.run()
