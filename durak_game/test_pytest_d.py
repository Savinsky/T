# -*- coding: utf-8 -*-
import pytest
from ndrk import Deck, Player

class TestClassDeckPytest:
    def setup(self):
        self.deck = Deck()
        print ("Start test Deck!")

# Проверяем равна ли количество карт в колоде 36
    def test_len_build_deck(self):
       assert len(self.deck.show()) == 36

# Проверяем выбран ли козырь
    def test_choose_trump_suit(self):
        assert self.deck.choose_trump_suit() != 0

# Проверяем перемешана ли колода(не равна вновь созданной)
    def test_shuffle_deck(self):
        assert self.deck.shuffle() != self.deck

    def teardown(self):
        print('Test completed!')
        del self.deck

class TestClassPlayerPytest:
    def setup(self):
        self.player = Player("Nik")
        print ("Start test Player!")

# Проверяем определение имени игрока
    def test_name_player(self):
        assert self.player.name == "Nik"

# Проверяем есть ли 6 карт в руках игрока
    def test_draw_card(self):
        assert len(self.player.draw(Deck())) == 6

    def tearown(self):
        print('Test completed!')
        del self.player





