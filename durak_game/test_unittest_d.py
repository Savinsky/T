# -*- coding: utf-8 -*-
import unittest
from collections import Counter
from ndrk import Deck, Player

class TestClassDeckUnittest(unittest.TestCase):
    def setUp(self):
        print('Start test class Deck!')
        self.deck = Deck()

# Проверяем козырь is not none
    def test_choose_trump_suit(self):
        self.assertIsNotNone(self.deck.choose_trump_suit())

# Проверяем количество карт в колоде(больше 32)
    def test_draw_card(self):
        self.assertGreater(len(self.deck.build()), 32)

    def test_deck_count(self):
        self.assertEqual(len(self.deck.build()), 36)

    def tearDown(self):
        print('Test completed!')

class TestClassPlayerUnittest(unittest.TestCase):
    def setUp(self):
        print ('Start test class Player!')
        self.player = Player("N")

# Проверяем количество карт в руках игрока меньше числа карт в колоде
    def test_deck(self):
        self.assertLess(self.player.draw, Deck().build())

# Проверяем есть ли карты у игрока
    def test_deck1(self):
        self.assertTrue(self.player.draw)


    def tearDown(self):
        print('Test completed!')

