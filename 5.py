from __future__ import annotations
from typing import Tuple
from typing import List
from pathlib import Path
from typing import Optional
import os

MapEntry = Tuple[int, int, int]

class MyRange:
    def __init__(self, start: int, size: int):
        if start < 0 or size <= 0:
            raise Exception(f"Error! {start} {size}")
        self.start = start
        self.size = size
    
    def __str__(self):
        return f"MyRange: {self.start}, {self.size}"

    def __repr__(self):
        return f"MyRange: {self.start}, {self.size}"

    def ending_index(self) -> int:
        return self.start + self.size - 1

    def find_overlap(self, other: MyRange) -> Optional[MyRange]:
        print(f"Checking overlap between {self} and {other}")
        if self.start > other.start:
            return other.find_overlap(self)
        else:
            if self.ending_index() < other.start:
                return None
            else:
                new_start = max(self.start, other.start)
                new_end = min(self.ending_index(), other.ending_index())
                if new_start > new_end:
                    return None
                else: 
                    new_size = new_end - new_start + 1
                    to_return = MyRange(new_start, new_size)
                    print(f"Overlap found: {to_return}")
                    return to_return

    def subtract_overlap(self, overlap: MyRange) -> List[MyRange]:
        print(f"Subtracting overlap of {overlap} from {self}")
        start_diff = overlap.start - self.start
        end_diff = self.ending_index() - overlap.ending_index()
        to_return = []
        if start_diff != 0:
            print(f"building {start_diff}")
            starting_chunk = MyRange(self.start, start_diff)
            print(f"Starting Chunk {starting_chunk}")
            to_return.append(starting_chunk)
        if end_diff != 0:
            ending_chunk = MyRange(overlap.ending_index()+1, end_diff)
            print(f"ending Chunk {ending_chunk}")
            to_return.append(ending_chunk)
        return to_return

def lines(full_file_path: str) -> List[str]:
    p = Path(full_file_path)
    t = p.read_text()
    return t.splitlines()

def work(lines: List[str]) -> str:
    seeds: List[MyRange] = parse_seeds(lines.pop(0)) # seeds line
    lines.pop(0) # starting empty
    lines.pop(0) # first label
    print(f"seeds: {seeds}")
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
            current_map.append((int(split_line[1]), int(split_line[0]), int(split_line[2])))
    maps.append(current_map)
    #print(f"maps: {maps}")
    min_seed = translate_all(seeds, maps)
    return str(min_seed)

def parse_seeds(line: str) -> List[MyRange]:
    seeds = line.split(":")
    each_seed = [int(x) for x in seeds[1].split()] 
    to_return: List[MyRange] = []
    for i, seed in enumerate(each_seed):
        if i % 2 == 1:
            to_return.append(MyRange(each_seed[i-1], each_seed[i]))
    return to_return

def translate_all(source: List[MyRange], maps: List[List[MapEntry]]) -> int:
    print(f"starting with source: {source}")
    current = source
    for i, map in enumerate(maps):
        print(f"starting round {i} - {map}")
        current = translate(current, map)        
        print(f"new source is {current}")
    current_starts = [x.start for x in current]
    return min(current_starts)

def translate(source: List[MyRange], map: List[MapEntry]) -> List[MyRange]:
    to_process : List[MyRange] = source
    print(f"Processing start: {to_process}")
    to_return : List[MyRange] = []
    while len(to_process) > 0:
        current_source = to_process.pop()      
        result = chomp_and_translate_full(current_source, map)
        to_return.append(result[0])
        to_process.extend(result[1])
    return to_return

def chomp_and_translate_full(source: MyRange, map_entries: List[MapEntry]) -> Tuple[MyRange, List[MyRange]]:
    print(f"Processing individual: {source}")
    for map_entry in map_entries:
        print(f"Checking {source} against {map_entry}")
        translation_and_remainder = chomp_and_translate(source, map_entry)
        if translation_and_remainder[0] is not None:
            print(f"Translated, we have {translation_and_remainder}")
            return (translation_and_remainder[0], translation_and_remainder[1])
    print(f"no overlaps found between {source} and any of {map_entries}. Returning original value.")
    return (source, [])

def chomp_and_translate(source: MyRange, map_entry: MapEntry) -> Tuple[Optional[MyRange], List[MyRange]]:
    # find overlap
    entry_as_source: MyRange = MyRange(map_entry[0], map_entry[2])
    overlap = source.find_overlap(entry_as_source)
    if overlap is None:
        print(f"no overlap found between {source} and {map_entry}")
        return (None, [])
    else: 
        remainders = source.subtract_overlap(overlap)
        return (translate_pure(overlap, map_entry), remainders)

def translate_pure(overlap: MyRange, map_entry: MapEntry) -> MyRange:
    change = map_entry[0] - map_entry[1]
    return MyRange(overlap.start - change, overlap.size)

#path = os.path.join("data_files", "5_1_example.txt")
path = os.path.join("data_files", "5_1.txt")
print(work(lines(path)))