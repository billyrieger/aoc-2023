import re
import sys

digit_re = re.compile('(\d+)')

def any_adjacent_symbols(lines: list[str], row: int, span: (int, int)) -> bool:
    for row in [row - 1, row, row + 1]:
        for col in range(span[0] - 1, span[1] + 1):
            if lines[row][col] not in '.0123456789':
                return True
    return False

def update_gear_map(gear_map, lines: list[str], row: int, match):
    span = match.span()
    for row in [row - 1, row, row + 1]:
        for col in range(span[0] - 1, span[1] + 1):
            if lines[row][col] == '*':
                if (row, col) not in gear_map:
                    gear_map[(row, col)] = [int(match.group(1))]
                else:
                    gear_map[(row, col)].append(int(match.group(1)))

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        lines = f.read().splitlines()
    # pad the grid with empty space
    lines = ['.' + line + '.' for line in lines]
    empty_line = '.' * len(lines[0])
    lines = [empty_line] + lines + [empty_line]
    part1 = 0
    gear_map: dict[(int, int), list[int]] = {}
    for row, line in enumerate(lines):
        if row == 0 or row == len(lines) - 1:
            continue
        for match in digit_re.finditer(line):
            if any_adjacent_symbols(lines, row, match.span()):
                part1 += int(match.group(1))
            update_gear_map(gear_map, lines, row, match)
    print(part1)
    part2 = sum([values[0] * values[1] for values in gear_map.values() if len(values) == 2])
    print(part2)