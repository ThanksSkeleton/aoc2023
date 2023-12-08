from __future__ import annotations
from typing import Dict, Tuple
from typing import List
from pathlib import Path
import functools
import os

Node = Tuple[str, str]
Label_And_Node = Tuple[str, Tuple[str, str]]

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
    return str(navigate_all(map, instructions))

def parse_line(input: str) -> Label_And_Node:
    clean_1 = input.replace("(", "")
    clean_2 = clean_1.replace(")", "")
    splitted_1 = clean_2.split("=")
    splitted_2 = splitted_1[1].split(",")
    return (splitted_1[0].strip(), (splitted_2[0].strip(), splitted_2[1].strip()))


def navigate_all(map: Dict[str, Node], instructions: str) -> int:
    START = "AAA"
    END = "ZZZ"
    move_count = 0
    current_instructions = instructions
    current_location = START
    while True:
        current_move = current_instructions[0]
        if current_move == "L":
            current_location = map[current_location][0]
        else:
            current_location = map[current_location][1]
        move_count = move_count + 1
        if current_location == END:
            return move_count
        if len(current_instructions) == 1:
            current_instructions = instructions
        else: 
            current_instructions = current_instructions[1:]

#path = os.path.join("data_files", "8_1_example_1.txt")
#path = os.path.join("data_files", "8_1_example_2.txt")
path = os.path.join("data_files", "8_1.txt")
print(work(lines(path)))