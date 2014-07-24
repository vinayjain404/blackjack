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

### Improvements

1. Improve session handling either via Redis or DB to not rely of client side
cookies
2. Add some game features like double down, insurance, soft hand (11 or 1 for
   Ace)
3. Make the code more modular to use serializers and models to avoid code
   duplication
4. Add robust unit tests for the code and specially for the random card shuffle
5. Complete the TODO in the code
6. Improve the API response to be consumed by a variety of client
