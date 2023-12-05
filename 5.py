from typing import Tuple
from typing import List
from pathlib import Path
from typing import Optional
import os

MapEntry = Tuple[int, int, int]

def lines(full_file_path: str) -> List[str]:
    p = Path(full_file_path)
    t = p.read_text()
    return t.splitlines()

def work(lines: List[str]) -> str:
    seeds = parse_seeds(lines.pop(0)) # seeds line
    lines.pop(0) # starting empty
    lines.pop(0) # first label
    maps = []
    current_map : List[MapEntry]= []
    for line in lines:
        if line.isspace() or not line:
            pass # just consume
        elif ":" in line:
            maps.append(current_map)
            current_map = []
        else:
            split_line = line.split()
            current_map.append((int(split_line[0]), int(split_line[1]), int(split_line[2])))
    maps.append(current_map)
    min_seed = find_minimum_seed(seeds, maps)
    return str(min_seed)

def parse_seeds(line: str) -> List[int]:
    seeds = line.split(":")
    each_seed = [int(x) for x in seeds[1].split()] 
    return each_seed

def find_minimum_seed(seeds: List[int], maps: List[List[MapEntry]]) -> int:
    minimum = None
    for seed in seeds:
        result = translate_all(seed, maps)
        if minimum is None or result < minimum:
            minimum = result
    return minimum or 0

def translate_all(source: int, maps: List[List[MapEntry]]) -> int:
    current = source
    for map in maps:
        current = translate(current, map)
    return current

def translate(source: int, map: List[MapEntry]) -> int:
    for map_entry in map:
        translation = translate_if_possible(source, map_entry)
        if translation is not None:
            return translation
    return 0

def translate_if_possible(source: int, map_entry: MapEntry) -> Optional[int]: # or None
    if source < map_entry[0]:
        return None
    elif source > map_entry[0] + map_entry[2]:
        return None
    else:
        index = source - map_entry[0]
        return index + map_entry[1]

path = os.path.join("data_files", "5_1_example.txt")
#path = os.path.join("data_files", "5_1.txt")
print(work(lines(path)))