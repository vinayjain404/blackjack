# Blackjack application
from flask import Flask
from flask import jsonify
from flask import session

from api_exceptions import ApplicationError
from constants import SECRET_KEY
from deck import Card
from deck import Deck
from deck import Hand
from decorators import require_incomplete_game

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
    deck = Deck(initial=True)
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

    # TODO handle corner case of both dealer and player having blackjacks
    if player_hand.is_blackjack:
        data["winner"] = "player"
    elif dealer_hand.is_blackjack:
        data["winner"] = "dealer"

    # Clear any previously stored sessions
    session.clear()

    # Store state of deck and hands in session
    session['deck'] = deck
    session['dealer_hand'] = dealer_hand
    session['player_hand'] = player_hand
    session['winner'] = data['winner']

    return jsonify(data)


@app.route("/hit")
@require_incomplete_game
def hit():
    """API endpoint for fetching a card via a human.

    Actions:
    - Fetch a new card from the deck and computes the scores.
    - If the score is >21 then computer wins, =21 human wins else continue the
    game
    """
    # Fetch state from session
    deck = Deck(session.get("deck"))
    player_hand = Hand(session.get("player_hand"))
    dealer_hand = Hand(session.get("dealer_hand"))

    player_hand.add_card(deck.pick())

    data = {
        "winner": None,
        "player_hand": player_hand,
        "dealer_hand": dealer_hand,
    }

    if player_hand.is_blackjack:
        data["winner"] = "player"
    elif player_hand.is_busted:
        data["winner"] = "dealer"

    # Store state of deck and hands in session
    session['deck'] = deck
    session['dealer_hand'] = dealer_hand
    session['player_hand'] = player_hand
    session['winner'] = data['winner']
    return jsonify(data)


@app.route("/stand")
@require_incomplete_game
def stand():
    """API endpoint for stopping fetching cards for a human.

    Actions:
    - Computes score for human and stops if >21, = 21
    - Fetches card for the computer until the computer reaches atlteast 17
    - If the score is >21 then human wins, =21 computer wins, human and computer
    score is the same then its a push
    """
    # Fetch state from session
    deck = Deck(session.get("deck"))
    dealer_hand = Hand(session.get("dealer_hand"))
    player_hand = Hand(session.get("player_hand"))

    data = {
        "winner": None,
        "player_hand": player_hand,
        "dealer_hand": dealer_hand,
    }

    while dealer_hand.should_play:
        dealer_hand.add_card(deck.pick())

    if dealer_hand.is_busted:
        data["winner"] = "player"
    elif dealer_hand == player_hand:
        data["winner"] = "push"
    elif dealer_hand < player_hand:
        data["winner"] = "player"
    else:
        data["winner"] = "dealer"

    # Store state of deck and hands in session
    session['deck'] = deck
    session['dealer_hand'] = dealer_hand
    session['player_hand'] = player_hand
    session['winner'] = data['winner']

    return jsonify(data)


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
