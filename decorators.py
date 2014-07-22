from functools import wraps

from flask import session

from api_exceptions import ApplicationError


def require_incomplete_game(func):
    """Decorator to make sure we dont proceed if the game is completed."""
    @wraps(func)
    def inner(*args, **kwargs):
        if session.get('winner'):
            raise ApplicationError(message="Game is complete so call /deal to start a new game")
        return func(*args, **kwargs)
    return inner
