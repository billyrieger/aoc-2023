import sys

def map_seed(seed: int, all_ranges: list[list[(int, int, int)]]) -> int:
    for ranges in all_ranges:
        for dest_start, source_start, length in ranges:
            if source_start <= seed < source_start + length:
                seed = dest_start + (seed - source_start)
                break
    return seed

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        groups = f.read().split('\n\n')
        initial_seeds = list(map(int, groups[0].split(':')[1].split()))
        all_ranges = []
        for group in groups[1:]:
            ranges = []
            lines = group.splitlines()
            for line in lines[1:]:
                ranges.append(tuple(map(int, line.split())))
            all_ranges.append(ranges)
    mapped_seeds = map(lambda s: map_seed(s, all_ranges), initial_seeds)
    print('part 1:', min(mapped_seeds))