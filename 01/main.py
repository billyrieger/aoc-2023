from pathlib import Path
import sys

def calibration1(line: str):
    digits = [x for x in line if x.isdigit()]
    first, last = digits[0], digits[-1]
    return 10 * int(first) + int(last)

def calibration2(line: str):
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
    first, last = found_digits[0], found_digits[-1]
    return 10 * int(first) + int(last)

if __name__ == '__main__':
    input_path = sys.argv[1]
    with open(input_path) as f:
        lines = f.readlines()
    total1, total2 = 0, 0
    for line in lines:
        total1 += calibration1(line)
        total2 += calibration2(line)
    print(total1, total2)