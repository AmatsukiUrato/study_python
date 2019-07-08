from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "<p>Chose one</p> <br> <a href=\"/red\">red</a> or <a href=\"/blue\">blue</a>"


@app.route("/red")
def red():
    return "<body style=\"background-color: indianred\">"


@app.route("/blue")
def blue():
    return "<body style=\"background-color: cornflowerblue\">"


if __name__ == '__main__':
    app.run()