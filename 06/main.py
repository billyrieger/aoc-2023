from math import sqrt, floor, ceil
import sys

def ways_to_win(time: int, record: int) -> int:
    # The record is broken if (time pressing button) * (time left in race) > record.
    # Mathematically, this is solving the quadratic inequality x * (t - x) > r.
    # x^2 - t*x + r < 0, use the quadratic formula and round carefully.
    discriminant = time * time - 4 * record
    min_exact = (time - sqrt(discriminant)) / 2
    max_exact = (time + sqrt(discriminant)) / 2
    min_win = max(floor(min_exact + 1), 0)
    max_win = min(ceil(max_exact - 1), time)
    return max_win - min_win + 1

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        lines = f.read().splitlines()
        times = list(map(int, lines[0].split()[1:]))
        records = list(map(int, lines[1].split()[1:]))
    part1 = 1
    for time, record in zip(times, records):
        part1 *= ways_to_win(time, record)
    print('part 1:', part1)
    combined_time = int(''.join(map(str, times)))
    combined_record = int(''.join(map(str, records)))
    print('part 2:', ways_to_win(combined_time, combined_record))