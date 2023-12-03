from pathlib import Path
import sys

def calibration1(line):
    digits = [x for x in line if x.isdigit()]
    first, last = digits[0], digits[-1]
    return 10 * int(first) + int(last)

if __name__ == '__main__':
    input_path = sys.argv[1]
    with open(input_path) as f:
        lines = f.readlines()
    total = 0
    for line in lines:
        total += calibration1(line)
    print(total)