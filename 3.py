from __future__ import annotations
import os
from pathlib import Path
from typing import Tuple
from typing import Optional

def lines(full_file_path: str) -> list[str]:
    p = Path(full_file_path)
    t = p.read_text()
    return t.splitlines()

def work(lines: list[str]) -> str:
    sum = 0
    map = {}
    for y, line in enumerate(lines):
        for x, character in enumerate(line):
            map[(x, y)] = character
    for (x, y) in map.keys():
        value = map[(x, y)]
        if not str(value).isnumeric() and not value == '.':
            for return_value in find_all_labels(map, x, y):
                sum = sum + return_value
    return str(sum)

def work_2(lines: list[str]) -> str:
    sum = 0
    map = {}
    for y, line in enumerate(lines):
        for x, character in enumerate(line):
            map[(x, y)] = character
    for (x, y) in map.keys():
        value = map[(x, y)]
        if value == '*':
            all_labels = find_all_labels(map, x, y)
            if len(all_labels) == 2:
                sum = sum + all_labels[0] * all_labels[1]
    return str(sum)

def find_all_labels(map: dict[Tuple[int, int], str], x: int, y: int) -> list[int]:
    # M1.2 M1.1 M1.3
    # S1 () S2
    # M2.2 M2.1 M2.3
    side_points = [(x-1, y), (x+1, y)]
    middle_points_set = [((x, y-1), (x-1, y-1), (x+1, y-1)), ((x,y+1), (x-1, y+1), (x+1, y+1))]
    to_return: list[Optional[int]] = []
    for side in side_points:
        to_return.append(find_value_total(map, side[0], side[1]))
    for middle in middle_points_set:
        middle_value = find_value_total(map, middle[0][0], middle[0][1])
        if middle_value is None:
            to_return.append(find_value_total(map, middle[1][0], middle[1][1]))
            to_return.append(find_value_total(map, middle[2][0], middle[2][1]))
        else:
            to_return.append(middle_value)
    to_return_real: list[int] = [t for t in to_return if t is not None]
    return to_return_real

def find_value_total(map: dict[Tuple[int, int], str], x: int, y:int) -> Optional[int]:
    raw = find_value_raw(map, x, y)
    if len(raw) == 0:
        return None
    sum = 0
    raw.reverse()
    for i, rawvalue in enumerate(raw):
        sum = sum + int(rawvalue) * pow(10, i)
    return sum 

def find_value_raw(map: dict[Tuple[int, int], str], x: int, y:int) -> list[int]:
    if (x, y) not in map:
        return []
    value = map[(x, y)]
    if not value.isnumeric():
        return []
    else:
        return find_value_raw_direction(map, x-1, y, -1) + [int(value)] + find_value_raw_direction(map, x+1, y, 1)

def find_value_raw_direction(map: dict[Tuple[int, int], str], x: int, y:int, direction: int) -> list[int]:
    if (x, y) not in map:
        return []
    value = map[(x, y)]
    if not value.isnumeric():
        return []
    else:
        direction_result = find_value_raw_direction(map, x+direction, y, direction)
        if direction == -1:
            direction_result.append(int(value))
        else:
            direction_result.insert(0, int(value))
        return direction_result
    
#path = os.path.join("data_files", "3_1_example.txt")
path = os.path.join("data_files", "3_1.txt")
print(work_2(lines(path)))