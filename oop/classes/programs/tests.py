from Deck_of_Cards import Card
from Deck_of_Cards import Deck
import unittest

class CardTests(unittest.TestCase):
    def setUp(self):
        self.firstcard = Card('A','Hearts')
        self.secondcard = Card('J','Hearts')
        self.thirdcard = Card('Q','Hearts')
        self.fourthcard = Card('K','Hearts')
        self.fifthcard = Card('4','Hearts')

    def test_init(self):
        self.assertEqual(self.firstcard.suit,"Hearts")
        self.assertEqual(self.secondcard.suit,"Hearts")
        self.assertEqual(self.thirdcard.suit,"Hearts")
        self.assertEqual(self.fourthcard.suit,"Hearts")
        self.assertEqual(self.fifthcard.suit,"Hearts")
        self.assertEqual(self.firstcard.value,"A")
        self.assertEqual(self.secondcard.value,"J")
        self.assertEqual(self.thirdcard.value,"Q")
        self.assertEqual(self.fourthcard.value,"K")
        self.assertEqual(self.fifthcard.value,"4")

    def test_repr(self):
        self.assertEqual(repr(self.firstcard),"Ace of Hearts")
        self.assertEqual(repr(self.secondcard),"Jack of Hearts")
        self.assertEqual(repr(self.thirdcard),"Queen of Hearts")
        self.assertEqual(repr(self.fourthcard),"King of Hearts")
        self.assertEqual(repr(self.fifthcard),"4 of Hearts")

class DeckTests(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()

    def test_init(self):
        self.assertTrue(isinstance(self.deck.cards,list))
        self.assertEqual(len(self.deck.cards),52)

    def test_repr(self):
        self.assertEqual(repr(self.deck), 'Deck of 52 cards')

    def count(self):
        self.assertEqual(self.deck.count(),52)

    def test_deal_insufficient_cards(self):
        cards = self.deck._deal(100)
        self.assertEqual(len(cards),52)
        self.assertEqual(self.deck.count(),0)

    def test_deal_no_cards(self):
        self.deck._deal(self.deck.count())
        with self.assertRaises(ValueError):
            self.deck._deal(1)

    def test_deal_card(self):
       card = self.deck.cards[-1]
       removed_card = self.deck.deal_card()
       self.assertEqual(card,removed_card)
       self.assertEqual(self.deck.count(),51)

    def test_deal_hand(self):
        hand = self.deck.cards[-5:self.deck.count()+1]
        removed_hand = self.deck.deal_hand(5)
        self.assertEqual(hand,removed_hand)
        self.assertEqual(self.deck.count(),47)



if __name__ == '__main__':
    unittest.main()
