## README

## Blackjack via APIs

### Requiremnets:

1. Python Flask Web Framework (http://flask.pocoo.org/)

```
pip install flask
```

### Running the project:
```
python app.py
```

### How to Play
1. Access the API /deal to start the game
2. If the player wants to hit looking at the game then call the /hit API
3. If the player wants to stand call the /stand API
4. To see the current state of the game call the /cards API

### Features
1. Session based game
2. Ability to not cheat and call hit or stand after the game is over


### Improvements

1. Improve session handling either via Redis or DB to not rely of client side
cookies (possibly make it stateless but will involve handling security)
2. Add some game features like double down, insurance, soft hand (11 or 1 for
   Ace)
3. Make the code more modular to use serializers and models to avoid code
   duplication
4. Add robust unit tests for the code and specially for the random card shuffle
5. Complete the TODO in the code
6. Improve the API response to be consumed by a variety of client
