from random import shuffle

class Card:

    def __init__(self, value, suit):
        self.suit = suit
        self.value = value

    def __repr__(self):
        if self.value == 'A':
            return f'Ace of {self.suit}'
        elif self.value == 'J':
            return f'Jack of {self.suit}'
        elif self.value == 'Q':
            return f'Queen of {self.suit}'
        elif self.value == 'K':
            return f'King of {self.suit}'
        else:
            return f'{self.value} of {self.suit}'


class Deck:
    def __init__(self):
        suit_list = ('Hearts','Diamonds','Clubs','Spades')
        value_list = ('A','2','3','4','5','6','7','8','9','10','J','Q','K')

        self.cards = [Card(value,suit) for suit in suit_list for value in value_list]

       # for suit in suit_list:
       #     for value in value_list:
       #         self.cards.Card(value, suit)

    def __repr__(self):
        return f'Deck of {self.count()} cards'

    def __iter__(self):
        return iter(self.cards)

    def count(self):
        return len(self.cards)

    def _deal(self, num):
        count = self.count()
        remove_amount = min([count,num])
        if count == 0:
            raise ValueError('All cards have been dealt')
        cards = self.cards[-remove_amount:]
        self.cards = self.cards[:-remove_amount]
        return cards

    def deal_card(self):
        return self._deal(1)[0]

    def deal_hand(self, hand_size):
        return self._deal(hand_size)

    def shuffle(self):
        if self.count() < 52:
            raise ValueError('Only full decks can be shuffled')
        shuffle(self.cards)
        return self

#d = Deck()
#print(d.cards)
#d.shuffle()
#print(d.cards)
#c1 = d.deal_card()
#hand = d.deal_hand(5)
#print(c1)
#print(hand)
#print(d.count())
#hand2 = d.deal_hand(55)
#print(d.count())
#my_deck = Deck()
#my_deck.shuffle()
#
#for card in my_deck:
#    print(card)












