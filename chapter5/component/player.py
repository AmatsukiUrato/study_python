# coding: utf-8
import random

class Player:
    _hand_dictionary = {1: "グー", 2:"チョキ", 3:"パー"}

    def __init__(self, name, winner_sentence):
        self.name = name
        self.winner_sentence = winner_sentence

    def choose_hand(self):
        self.myself_hand_number = random.randint(1, 3)

    def say_win_voice(self):
        sentence_number = random.randint(0, len(self.winner_sentence) - 1)
        print(self.winner_sentence[sentence_number])

    def show_hand(self):
        return self._hand_dictionary[ self.myself_hand_number]

    def say_hand(self):
        print(self.name + "の手は" + self.show_hand())