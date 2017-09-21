class Card:

    def __init__(self, suit, value):
        if suit not in ['spade', 'diamond', 'club', 'heart']:
            raise ValueError(
                "{} must be in ['spade', 'diamond', 'club', 'heart']")
        self.suit = suit

        if value not in ['A', 'Q', 'K', 'J'] and value not in list(range(2, 11)):
            raise ValueError
        self.value = value


class Deck:
    pass
