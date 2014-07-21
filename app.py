# Blackjack application
from flask import Flask
from flask import jsonify

from constants import SECRET_KEY
from api_exceptions import ApplicationError

app = Flask(__name__)
app.secret_key = SECRET_KEY


@app.route("/")
def home():
    return "Lets play Blackjack"


@app.route("/deal")
def deal():
    """API endpoint for starting the game.

    Actions:
    - Deal 2 cards to the human and 2 the computer alternately
    - Checks if either is 21 if it is then returns the winner

    TODO: Splitting cards, double down and insurance are not a feature yet
    """
    return "Hello World!"


@app.route("/hit")
def hit():
    """API endpoint for fetching a card via a human.

    Actions:
    - Fetch a new card from the deck and computes the scores.
    - If the score is >21 then computer wins, =21 human wins else continue the
    game
    """

    return "Hello World!"


@app.route("/stand")
def stand():
    """API endpoint for stopping fetching cards for a human.

    Actions:
    - Computes score for human and stops if >21, = 21
    - Fetches card for the computer until the computer reaches atlteast 17
    - If the score is >21 then human wins, =21 computer wins, human and computer
    score is the same then its a push
    """
    return "Hello World!"


@app.route("/cards")
def cards():
    """API to show all the cards for the human"""
    return "Hello World!"


@app.errorhandler(ApplicationError)
def handle_application_error(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response

if __name__ == "__main__":
    app.run()
