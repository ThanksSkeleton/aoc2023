from __future__ import annotations
import os
from pathlib import Path
from typing import Tuple

def lines(full_file_path: str) -> list[str]:
    p = Path(full_file_path)
    t = p.read_text()
    return t.splitlines()

def work(lines: list[str]) -> str:
    base_count_map = {}
    max_i = 0
    for i, line in enumerate(lines):
        max_i = i+1
        s = score_part_2(line)
        base_count_map[max_i] =s
    recursive_count_map = {}
    count_down = list(range(1, max_i+1))
    count_down.reverse()
    for i in count_down:
        recursive_count_map[i] = recursive_count(i, base_count_map, recursive_count_map)       
    sum = 0
    for k in recursive_count_map.keys():
        sum = sum + recursive_count_map[k]

    return str(sum)

def recursive_count(i: int, base_count_map: dict[int, int], recursive_count_map: dict[int, int]) -> int:
    base_score = base_count_map[i]
    if base_score == 0:
        return 1
    sum = 1
    for children in range(i+1, i+base_score+1):
        sum = sum + recursive_count_map[children]
    return sum

def score_part_1(line: str) -> int:
    first_split = line.split(":")
    second_split = first_split[1].split("|")
    winners_strings = second_split[0].strip().split(None)
    winners = [int(ws) for ws in winners_strings]
    mine_strings = second_split[1].strip().split(None)
    mine = [int(m) for m in mine_strings]
    win_count = 0
    for m in mine:
        if m in winners:
            win_count = win_count + 1
    
    if win_count == 0:
        return 0
    else:
        return pow(2, win_count-1)
    
def score_part_2(line: str) -> int:
    first_split = line.split(":")
    second_split = first_split[1].split("|")
    winners_strings = second_split[0].strip().split(None)
    winners = [int(ws) for ws in winners_strings]
    mine_strings = second_split[1].strip().split(None)
    mine = [int(m) for m in mine_strings]
    win_count = 0
    for m in mine:
        if m in winners:
            win_count = win_count + 1
    return win_count

#path = os.path.join("data_files", "4_1_example.txt")
path = os.path.join("data_files", "4_1.txt")
print(work(lines(path)))