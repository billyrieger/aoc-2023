import math, sys

def ways_to_win(time: int, record: int) -> int:
    ways = [i for i in range(time) if i * (time - i) > record]
    return len(ways)

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