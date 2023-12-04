from __future__ import annotations
import os
from pathlib import Path

def lines(full_file_path: str) -> list[str]:
    p = Path(full_file_path)
    t = p.read_text()
    return t.splitlines()

#Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
def work(lines: list[str]) -> str:
    sum = 0
    for i, s in enumerate(lines):
        sum = sum + calculate_power(s)
    return str(sum)

def is_valid(line: str) -> bool:
    max_red = 12
    max_green = 13
    max_blue = 14
    second_half = line.split(":")
    for reveal in second_half[1].split(";"):
        for color_reveal in reveal.strip().split(","):
            cr_split = color_reveal.strip().split()
            num = int(cr_split[0].strip())
            color_name = cr_split[1].strip()
            invalid = (color_name == "red" and num > max_red) or (color_name == "green" and num > max_green) or (color_name == "blue" and num > max_blue)
            if invalid:
                return False
    return True

def calculate_power(line: str) -> int:
    min_red = 0
    min_green = 0
    min_blue = 0
    second_half = line.split(":")
    for reveal in second_half[1].split(";"):
        for color_reveal in reveal.strip().split(","):
            cr_split = color_reveal.strip().split()
            num = int(cr_split[0].strip())
            color_name = cr_split[1].strip()
            if (color_name == "red" and num > min_red):
                min_red = num
            elif (color_name == "green" and num > min_green):
                min_green = num
            elif (color_name == "blue" and num > min_blue):
                min_blue = num
    return min_red * min_green * min_blue


# path = os.path.join("data_files", "1_1_example.txt")
# path = os.path.join("data_files", "2_1_example.txt")
path = os.path.join("data_files", "2_1.txt")
# path = os.path.join("data_files", "1_2_example.txt")
print(work(lines(path)))