# Blackjack application
from flask import Flask

from constants import SECRET_KEY

app = Flask(__name__)
app.secret_key = SECRET_KEY


@app.route("/")
def home():
    return "Lets play Blackjack"


@app.route("/deal")
def deal():
    return "Hello World!"


@app.route("/hit")
def hit():
    return "Hello World!"


@app.route("/stand")
def stand():
    return "Hello World!"


@app.route("/cards")
def cards():
    return "Hello World!"


if __name__ == "__main__":
    app.run()
