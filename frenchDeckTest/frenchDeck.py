import collections
import re
from random import choice


class FrenchDeck:
    Card = collections.namedtuple('Card', ['rank', 'suit'])
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [self.Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    def show_deck(self):
        res = input("Try:")
        while res != 'n':
            if re.match(r'^[0-9]+$', res):
                res = int(res)
                print(self._cards[:res])
            else:
                if res == 'J':
                    print(self._cards[9::13])
                else:
                    print(choice(self._cards))
            res = input("Try:")

        return False


def spade_high(card_input):
    suit_value = dict(spades=3, hearts=2, diamonds=0, clubs=1)
    rank_value = FrenchDeck.ranks.index(card_input.rank)
    return rank_value*len(suit_value)+suit_value[card_input.suit]


if __name__ == "__main__":
    deck = FrenchDeck()
    print(len(deck))
    for card in sorted(deck, key=spade_high):
        print(card)

