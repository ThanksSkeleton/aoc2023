from __future__ import annotations
import os
from pathlib import Path

def lines(full_file_path: str) -> list[str]:
    p = Path(full_file_path)
    t = p.read_text()
    return t.splitlines()

def work(lines: [str]) -> str:
    sum = 0
    for l in lines:
        sum = sum + line_value(l)
    return str(sum)

def line_value(line: str) -> int:
    first_found = False
    first = 0
    last = 0
    digit_words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    buffer = ""
    for i, c in enumerate(line):
        has_currently_found_digit = False
        currently_found_digit = -1

        if (str(c)).isnumeric():
            buffer = ""
            has_currently_found_digit = True
            currently_found_digit = int(c)
        else:
            buffer = buffer + c
            for word in digit_words:
                if word in buffer:
                    buffer = c
                    has_currently_found_digit = True
                    currently_found_digit = digit_words.index(word) + 1

        if has_currently_found_digit:
            if not first_found:
                first_found = True
                first = currently_found_digit
            last = currently_found_digit
    
    if not first_found:
        return 0
    else: 
        return first * 10 + last
    
# path = os.path.join("data_files", "1_1_example.txt")
path = os.path.join("data_files", "1_1.txt")
# path = os.path.join("data_files", "1_2_example.txt")
print(work(lines(path)))



