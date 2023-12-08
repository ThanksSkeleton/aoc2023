from __future__ import annotations
from typing import Tuple
from typing import List
from pathlib import Path
from typing import Optional
import math
import os

class CardHand:
    def __init__(self, input: str):
        parsed = input.split()
        self.digits = self.to_digits(parsed[0])
        self.hand = self.determine_hand(self.digits)
        self.bid = int(parsed[1])

    def to_digits(self, hand: str) -> List[int]:
        return [self.to_digit(x) for x in hand] 

    def to_digit(self, card: str) -> int:
        if card.isnumeric():
            return int(card)
        # A, K, Q, J, T
        elif card == "T":
            return 10
        elif card == "J":
            return 11
        elif card == "Q":
            return 12
        elif card == "K":
            return 13
        else:
            return 14
    
    def determine_hand(hand_numerals: List[int]) -> int:
        card_count_dict = {}
        for n in hand_numerals:
            if n in card_count_dict.keys():
                previous_count = card_count_dict[n]
                card_count_dict[n] = previous_count + 1
            else:
                card_count_dict[n] = 1
        matches = sorted(card_count_dict.values, reverse=True)
        # RANK DESCRIPTION
        # 7 Five of a kind, where all five cards have the same label: AAAAA
        # 6 Four of a kind, where four cards have the same label and one card has a different label: AA8AA
        # 5 Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
        # 4 Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
        # 3 Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
        # 2 One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
        # 1 High card, where all cards' labels are distinct: 23456
        if matches[0] == 5:
            return 7
        elif matches[0] == 4:
            return 6
        elif matches[0] == 3:
            if matches[1] == 2:
                return 5
            else:
                return 4
        elif matches[0] == 2:
            if matches[1] == 2:
                return 3
            else:
                return 2
        else:
            return 1

    def __lt__(a: CardHand, b: CardHand) -> int:
        if a.hand != b.hand:
            return a.hand < b.hand
        else:
            for i in range(5):
                if a.digits[i] < b.digits[i]

        

def lines(full_file_path: str) -> List[str]:
    p = Path(full_file_path)
    t = p.read_text()
    return t.splitlines()



def work(lines: List[str]) -> str:
