import sys

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        lines = f.read().splitlines()
    part1 = 0
    copies_count = [1] * len(lines)
    for i, line in enumerate(lines):
        card, rest = line.split(':')
        card_num = int(card.split()[1])
        winning, given = rest.split('|')
        winning_nums = set(map(int, winning.split()))
        given_nums = set(map(int, given.split()))
        winners = given_nums.intersection(winning_nums)
        if winners:
            part1 += 2 ** (len(winners) - 1) 
            for j in range(1, len(winners) + 1):
                copies_count[i + j] += copies_count[i]
    print(part1)
    print(sum(copies_count))
