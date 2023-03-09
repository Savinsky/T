# -*- coding: utf-8 -*-

import random
VALUES_DICT = { 6: '6', 7: '7', 8: '8', 9: '9', 10: '10', 11: 'J', 12: 'Q', 13: 'K', 14: 'A'}
SUITS = ["Пики", "Червы", "Трефи", "Бубны"]

class Card(object):
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def show(self):
        print("{} {}".format(VALUES_DICT[self.value], self.suit))


class Deck(object):
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        return [self.cards.append(Card(s, v)) for s in SUITS for v in range(6, 15)]

    def show(self):
        return [c.show() for c in self.cards]

    def shuffle(self):
        return random.shuffle(self.cards)

    def draw_card(self):
        return self.cards.pop()


class Player(object):
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck):
        return [self.hand.append(deck.draw_card()) for i in range(6)]

    def show_hand(self):
        return [card.show() for card in self.hand]

deck = Deck()
deck.shuffle()
#deck.show()
n = Player("Nik")
print ("Карты в руках "), n.name
n.draw(deck)
n.show_hand()

bot = Player("Bot")
print ("Карты в руках "), bot.name
bot.draw(deck)
bot.show_hand()


