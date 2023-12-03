from pathlib import Path
import sys

def calibration(digits: list[int]):
    if digits:
        first, last = digits[0], digits[-1]
        return 10 * int(first) + int(last)
    else:
        return 0

def part1(line: str) -> int:
    digits = [x for x in line if x.isdigit()]
    return calibration(digits)

def part2(line: str) -> int:
    digit_values = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
    }
    found_digits: list[int] = []
    for i in range(len(line)):
        if line[i].isdigit():
            found_digits.append(int(line[i]))
            continue
        for digit, value in digit_values.items():
            if line[i:].startswith(digit):
                found_digits.append(value)
                break
    return calibration(found_digits)

if __name__ == '__main__':
    input_path = sys.argv[1]
    with open(input_path) as f:
        lines = f.readlines()
    total1, total2 = 0, 0
    for line in lines:
        total1 += part1(line)
        total2 += part2(line)
    print(total1, total2)