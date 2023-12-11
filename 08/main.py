import itertools
import sys


def part1(graph: dict[str, (str, str)], movement: str) -> int:
    steps = 0
    current = 'AAA'
    for direction in itertools.cycle(movement):
        (left, right) = graph[current]
        current = left if direction == 'L' else right
        steps += 1
        if current == 'ZZZ':
            break
    return steps


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        lines = f.read().splitlines()
    movement = lines[0]
    graph = {}
    for line in lines:
        # Scuffed line parsing
        input, left, right = line[0:3], line[7:10], line[12:15]
        graph[input] = (left, right)
    
    print('part 1:', part1(graph, movement))