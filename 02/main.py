import re
import sys

game_re = re.compile(r'Game (\d+)')
red_re = re.compile(r'(\d+) red')
green_re = re.compile(r'(\d+) green')
blue_re = re.compile(r'(\d+) blue')

def parse(line: str) -> (int, list[(int, int, int)]):
    def parse_single(pull: str) -> (int, int, int):
        r = int(red_re.search(pull).group(1)) if 'red' in pull else 0
        g = int(green_re.search(pull).group(1)) if 'green' in pull else 0
        b = int(blue_re.search(pull).group(1)) if 'blue' in pull else 0
        return (r, g, b)
    head, tail = line.split(':')
    game_num = int(game_re.search(head).group(1))
    pulls = [parse_single(x) for x in tail.split(';')]
    return (game_num, pulls)

def part1(games: list[(int, list[(int, int, int)])], red: int, green: int, blue: int):
    total = 0
    for game in games:
        ok = True
        for r, g, b in game[1]:
            if r > red or g > green or b > blue: 
                ok = False
                break
        if ok:
            total += game[0]
    print(total)

def part2(games: list[(int, list[(int, int, int)])]):
    total = 0
    for game in games:
        max_r = max(pull[0] for pull in game[1])
        max_g = max(pull[1] for pull in game[1])
        max_b = max(pull[2] for pull in game[1])
        total += max_r * max_g * max_b
    print(total)

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        lines = [parse(line) for line in f.readlines()]
    part1(lines, 12, 13, 14)
    part2(lines)