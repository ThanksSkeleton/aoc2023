from __future__ import annotations
from typing import Dict, Tuple, Optional
from typing import List
from pathlib import Path
import functools
import os

BranchNodeKey = str
BranchNodeValue = Tuple[str, str]
BranchNodeDict = Dict[BranchNodeKey, BranchNodeValue]

def lines(full_file_path: str) -> List[str]:
    p = Path(full_file_path)
    t = p.read_text()
    return t.splitlines()

def work(lines: List[str]) -> str:
    instructions = lines.pop(0)
    lines.pop(0)
    label_and_nodes = [ parse_line(line) for line in lines]
    map = {}
    for ln in label_and_nodes:
        map[ln[0]] = ln[1]
    return str(follow_all_trackers(map, instructions))

def parse_line(input: str) -> Tuple[BranchNodeKey, BranchNodeValue]:
    clean_1 = input.replace("(", "")
    clean_2 = clean_1.replace(")", "")
    splitted_1 = clean_2.split("=")
    splitted_2 = splitted_1[1].split(",")
    return (splitted_1[0].strip(), (splitted_2[0].strip(), splitted_2[1].strip()))

LinearNodeKey = Tuple[str, int]

class ChainTracker:
    def __init__(self, starter: str):
        print(f"tracker for {starter}")
        self.starter = starter
        self.sequence_array : dict[LinearNodeKey, int] = {}
        self.reverse_sequence_array : dict[int, LinearNodeKey] = {}
        self.next_index = 0
        self.terminus = None
        self.add((starter, 0))

    def add(self, key: LinearNodeKey):
        self.sequence_array[key] = self.next_index
        self.reverse_sequence_array[self.next_index] = key
        self.next_index = self.next_index+1

    def has_key(self, key: LinearNodeKey) -> bool:
        return key in self.sequence_array.keys()
    
    def follow_all(self, map: BranchNodeDict, sequence: str):
        print(f"tracking {self.starter}")
        while True:            
            current = self.reverse_sequence_array[self.next_index - 1]
            next_sequence_index = self.next_index % len(sequence)
            next_direction_string = sequence[next_sequence_index]
            next_direction = 0 if next_direction_string == "L" else 1
            next_label = map[current[0]][next_direction]
            next_node = (next_label, next_sequence_index)
            if self.has_key(next_node):
                print(f"for tracker starting at {self.starter} - loop detected at {next_node} {next_sequence_index} after {self.next_index}")
                return
            else:
                self.add(next_node)
            
# This can be expressed as
# n Full Cycles + 1 subcycle of size k
# k such that some number of starting nodes all align to a zero


def follow_all_trackers(map: BranchNodeDict, instructions: str):
    trackers = []
    for key in map.keys():
        if key.endswith("A"):
            trackers.append(ChainTracker(key))
    
    for t in trackers:
        t.follow_all(map, instructions)

#path = os.path.join("data_files", "8_1_example_1.txt")
#path = os.path.join("data_files", "8_1_example_2.txt")
path = os.path.join("data_files", "8_1.txt")
print(work(lines(path)))