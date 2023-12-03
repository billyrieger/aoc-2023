import re
import sys

game_re = re.compile(r'Game (\d+)')
red_re = re.compile(r'(\d+) red')
green_re = re.compile(r'(\d+) green')
blue_re = re.compile(r'(\d+) blue')

def parse_game(lines: list[str], red: int, green: int, blue: int):
    part1, part2 = 0, 0
    for line in lines:
        game, tail = line.split(':')
        draws = tail.split(';')
        game_num = int(game_re.search(game).group(1))
        ok = True
        max_r, max_g, max_b = 0, 0, 0
        for draw in draws:
            r = int(red_re.search(draw).group(1)) if 'red' in draw else 0
            g = int(green_re.search(draw).group(1)) if 'green' in draw else 0
            b = int(blue_re.search(draw).group(1)) if 'blue' in draw else 0
            if r > red or g > green or b > blue: 
                ok = False
            max_r = max(r, max_r)
            max_g = max(g, max_g)
            max_b = max(b, max_b)
        if ok:
            part1 += game_num
        part2 += max_r * max_g * max_b
    print(part1, part2)

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()
    parse_game(lines, 12, 13, 14)