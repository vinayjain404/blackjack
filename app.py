# Blackjack application
from flask import Flask
from flask import jsonify
from flask import session

from api_exceptions import ApplicationError
from constants import SECRET_KEY
from deck import Card
from deck import Deck
from deck import Hand

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
    deck = Deck()
    deck.shuffle()
    player_hand = Hand()
    dealer_hand = Hand()

    player_hand.add_card(deck.pick())
    dealer_hand.add_card(deck.pick())
    player_hand.add_card(deck.pick())
    dealer_hand.add_card(deck.pick())

    data = {
        "winner": None,
        "player_hand": player_hand,
        "dealer_hand": dealer_hand,
    }

    if player_hand.is_blackjack:
        data["winner"] = "player"
    if dealer_hand.is_blackjack:
        data["winner"] = "dealer"

    # Store state of deck and hands in session
    session['winner'] = data['winner']
    session['dealer_hand'] = dealer_hand
    session['player_hand'] = player_hand

    print player_hand

    return jsonify(data)

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
    """API to show all the cards for the game and result"""
    player_hand = session.get("player_hand")
    dealer_hand = session.get("dealer_hand")
    winner = session.get("winner")

    data = {
        "player_hand": player_hand,
        "dealer_hand": dealer_hand,
        "winner": winner,
    }
    return jsonify(data)


@app.errorhandler(ApplicationError)
def handle_application_error(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response

if __name__ == "__main__":
    app.debug = True
    app.run()
