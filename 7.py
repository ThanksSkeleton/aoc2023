from __future__ import annotations
from typing import Dict
from typing import List
from pathlib import Path
import functools
import os

class CardHand:
    def __init__(self, input: str):
        parsed = input.split()
        self.digits = self.to_digits(parsed[0])
        self.hand = self.determine_hand(self.digits)
        self.bid = int(parsed[1])

    def to_digits(self, hand: str) -> List[int]:
        return [self.to_digit(x) for x in hand] 

    def __str__(self):
        return f"CardHand: {self.hand}, {self.digits}, {self.bid}"

    def __repr__(self):
        return f"CardHand: {self.hand}, {self.digits}, {self.bid}"

    def to_digit(self, card: str) -> int:
        if card.isnumeric():
            return int(card)
        # A, K, Q, J, T
        elif card == "T":
            return 10
        elif card == "J":
            return 1
        elif card == "Q":
            return 12
        elif card == "K":
            return 13
        else:
            return 14
    
    def determine_hand(self, hand_numerals: List[int]) -> int:
        card_count_dict: Dict[int, int] = {}
        num_jokers = 0
        for n in hand_numerals:
            if n == 1:
                num_jokers = num_jokers + 1
            elif n in card_count_dict.keys():
                previous_count = card_count_dict[n]
                card_count_dict[n] = previous_count + 1
            else:
                card_count_dict[n] = 1
        hand_counts = sorted(card_count_dict.values(), reverse=True)
        simple_hand = self.simple_translation(hand_counts)
        upgraded_hand = self.upgrade_hand(simple_hand, num_jokers)
        return upgraded_hand

    def simple_translation(self, hand_counts: List[int]) -> int:
        FIVE_OF_A_KIND = 7
        FOUR_OF_A_KIND = 6
        FULL_HOUSE = 5
        THREE_OF_A_KIND = 4
        TWO_PAIR = 3
        ONE_PAIR = 2
        HIGH_CARD = 1
        # RANK DESCRIPTION
        # 7 Five of a kind, where all five cards have the same label: AAAAA
        # 6 Four of a kind, where four cards have the same label and one card has a different label: AA8AA
        # 5 Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
        # 4 Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
        # 3 Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
        # 2 One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
        # 1 High card, where all cards' labels are distinct: 23456
        padded_counts = []

        if len(hand_counts) == 1:
            padded_counts = [hand_counts[0], 0]
        elif len(hand_counts) == 0:
            padded_counts = [0, 0]
        else: 
            padded_counts = hand_counts

        if padded_counts[0] == 5:
            return FIVE_OF_A_KIND
        elif padded_counts[0] == 4:
            return FOUR_OF_A_KIND
        elif padded_counts[0] == 3:
            if padded_counts[1] == 2:
                return FULL_HOUSE
            else:
                return THREE_OF_A_KIND
        elif padded_counts[0] == 2:
            if padded_counts[1] == 2:
                return TWO_PAIR
            else:
                return ONE_PAIR
        else:
            return HIGH_CARD
        
    def upgrade_hand(self, hand: int, num_jokers: int) -> int:
        FIVE_OF_A_KIND = 7
        FOUR_OF_A_KIND = 6
        FULL_HOUSE = 5
        THREE_OF_A_KIND = 4
        TWO_PAIR = 3
        ONE_PAIR = 2
        HIGH_CARD = 1   
        if num_jokers == 0:
            return hand
        elif num_jokers == 1:
            if hand == FOUR_OF_A_KIND:
                return FIVE_OF_A_KIND
            elif hand == THREE_OF_A_KIND:
                return FOUR_OF_A_KIND
            elif hand == TWO_PAIR:
                return FULL_HOUSE
            elif hand == ONE_PAIR:
                return THREE_OF_A_KIND
            elif hand == HIGH_CARD:
                return ONE_PAIR
            else:
                raise Exception("Invalid_Conversion")
        elif num_jokers == 2:
            if hand == THREE_OF_A_KIND:
                return FIVE_OF_A_KIND
            elif hand == ONE_PAIR:
                return FOUR_OF_A_KIND
            elif hand == HIGH_CARD:
                return THREE_OF_A_KIND
            else:
                raise Exception("Invalid_Conversion")
        elif num_jokers == 3:
            if hand == ONE_PAIR:
                return FIVE_OF_A_KIND
            elif hand == HIGH_CARD:
                return FOUR_OF_A_KIND
            else:
                raise Exception("Invalid_Conversion")
        else:
            return FIVE_OF_A_KIND


def custom_comparison(a: CardHand, b: CardHand) -> int:
    comp_simple = (a.hand > b.hand) - (a.hand < b.hand)
    if comp_simple != 0:
        return comp_simple
    else:
        for i in range(5):
            comp = (a.digits[i] > b.digits[i]) - (a.digits[i] < b.digits[i])
            if comp == 0:
                pass
            else:
                return comp
        return 0

def lines(full_file_path: str) -> List[str]:
    p = Path(full_file_path)
    t = p.read_text()
    return t.splitlines()

def work(lines: List[str]) -> str:
    hands_unsorted = [ CardHand(line) for line in lines]
    hands_sorted = sorted(hands_unsorted, key=functools.cmp_to_key(custom_comparison))
    print(hands_sorted)
    sum = 0
    for i, hand in enumerate(hands_sorted):
        sum = sum + (i+1) * hand.bid
    return str(sum)

#path = os.path.join("data_files", "7_1_example.txt")
path = os.path.join("data_files", "7_1.txt")
print(work(lines(path)))