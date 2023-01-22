from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return f"Hello Flask!"

@app.route("/<name>/")
def home2(name):
    return f"Hello {name}!"


if __name__ == "__main__":
    app.run()