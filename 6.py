from __future__ import annotations
from typing import Tuple
from typing import List
from pathlib import Path
from typing import Optional
import math
import os

def lines(full_file_path: str) -> List[str]:
    p = Path(full_file_path)
    t = p.read_text()
    return t.splitlines()

def work_1(lines: List[str]) -> str:
    times = [int(x) for x in lines[0].split(":")[1].split()]
    distances = [int(x) for x in lines[1].split(":")[1].split()]
    product = 1
    for trial in range(len(times)):
        best_distances_count = 0
        for time_held in range(times[trial]):
            time_moving = times[trial] - time_held
            distance = time_held * 1 * time_moving
            if distance > distances[trial]:
                best_distances_count = best_distances_count + 1
        product = product * best_distances_count
    return str(product)

def work_2(lines: List[str]) -> str:
    times_all = [x for x in lines[0].split(":")[1].split()]
    total_time = int("".join(times_all))
    print(f"total_time {total_time}")
    distances_all = [x for x in lines[1].split(":")[1].split()]
    total_distance = int("".join(distances_all))
    print(f"total_distance {total_distance}")
    solutions = quadratic_solve(-total_time, total_distance)
    start = max(0, math.ceil(solutions[0]))
    end = min(math.ceil(solutions[1]), total_time)
    print(f"start {start} end {end}")
    solution = end-start
    return str(solution)

def quadratic_solve(b: int, c: int) -> list[float]:
    inside_term = b*b - 4 * c
    if inside_term == 0:
        return [float(-b) / 2.0]
    elif inside_term < 0:
        return []
    else:
        return [(float(-b) - math.sqrt(float(inside_term)) /2.0), (float(-b) + math.sqrt(float(inside_term)) / 2.0)]

#path = os.path.join("data_files", "5_1_example.txt")
#path = os.path.join("data_files", "6_1_example.txt")
path = os.path.join("data_files", "6_1.txt")
print(work_2(lines(path)))