class Card:

    def __init__(self, suit):
        if suit not in ['spade', 'diamond', 'club', 'heart']:
            raise ValueError(
                "{} must be in ['spade', 'diamond', 'club', 'heart']")
        self.suit = suit


class Deck:
    pass
