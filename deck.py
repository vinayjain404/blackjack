# Module to represent a deck of cards

import random

from constants import NUMBER_CHOICES
from constants import SUIT_CHOICES


class Card(dict):
    """Class representing a Card"""

    def __init__(self, number, suit, *args, **kwargs):
        super(Card, self).__init__(*args, **kwargs)

        # Perform some validation on the Card object
        if number not in NUMBER_CHOICES:
            raise Exception("Invalid number choice must be one from the"
                            "following choices: %s", str(NUMBER_CHOICES))
        if suit not in SUIT_CHOICES:
            raise Exception("Invalid suit choice must be one from the following"
                            "choices: %s", str(SUIT_CHOICES))

        self['number'] = number
        self['suit'] = suit


    def __str__(self):
        return "%s of %s" %(self['number'], self['suit'])


def blackjack_value(card):
    """This gives you a numeric value that corresponds to a Card object"""
    if card['number'] == "ACE":
        return 11
    elif card['number'] in ("JACK, QUEEN, KING"):
        return 10
    else:
        return int(card['number'])


class Deck(list):
    """Class representing a Deck which is a collection of Cards"""

    def __init__(self, *args, **kwargs):
        initial = kwargs.pop('initial', None)
        super(Deck, self).__init__(*args, **kwargs)

        if initial:
            """Populate the Deck with the Cards"""
            for suit in SUIT_CHOICES:
                for number in NUMBER_CHOICES:
                    card = Card(number, suit)
                    self.append(card)

    def shuffle(self):
        """Shuffle cards randomly.

        TODO: vinayjain Use a random generator htat uses urandom or system
        randomess
        """
        random.shuffle(self)

    def pick(self):
        """Return the top card from the deck"""
        if not self:
            raise Exception("Trying to pick from an empty deck")
        return self.pop(0)

    @property
    def cards_left(self):
        """Count of cards left in the deck"""
        return len(self)


class Hand(list):

    def add_card(self, card):
        self.append(card)

    def __eq__(self, other):
        """Override the compare operator to compare hands"""
        return self.value == other.value

    def __hash__(self):
        return hash(self.value)

    def __lt__(self, other):
        """Override the compare operator to compare hands"""
        return self.value < other.value

    def __gt__(self, other):
        """Override the compare operator to compare hands"""
        return self.value > other.value


    @property
    def value(self):
        return sum([blackjack_value(card) for card in self])

    @property
    def is_blackjack(self):
        return self.value == 21

    @property
    def is_busted(self):
        return self.value > 21

    @property
    def should_play(self):
        return self.value < 17
