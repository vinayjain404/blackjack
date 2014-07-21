# Module to represent a deck of cards

from constants import NUMBER_CHOICES
from constants import SUIT_CHOICES


class Card(object):
    """Class representing a Card"""

    def __init__(self, number, suit):
        # Perform some validation on the Card object
        if number not in NUMBER_CHOICES:
            raise Exception("Invalid number choice must be one from the
                             following choices: %s", str(NUMBER_CHOICES)
        if suit not in SUIT_CHOICES:
            raise Exception("Invalid suit choice must be one from the following
                             choices: %s", str(SUIT_CHOICES))

        self.number = number
        self.suit = suit

    @property
    def blackjack_value(self):
        """This gives you a numeric value that corresponds to a Card object"""
        if self.number == "ACE":
            return 11
        elif self.number in ("JACK, QUEEN, KING"):
            return 10
        else:
            return self.number

    def __unicode__(self):
        return "%s of %s" %(self.number, self.suit)


class Deck(List):
    """Class representing a Deck which is a collection of Cards"""

    def __init__(self):
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
