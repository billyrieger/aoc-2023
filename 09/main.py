import sys

def extrapolate(array: list[int]) -> int:
    if all(x == 0 for x in array):
        return 0
    difference = [array[i + 1] - array[i] for i in range(len(array) - 1)]
    return extrapolate(difference) + array[-1]

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        lines = f.read().splitlines()
    arrays = [list(map(int, line.split())) for line in lines]
    print('part 1:', sum(map(extrapolate, arrays)))
    reversed_arrays = [array[::-1] for array in arrays]
    print('part 2:', sum(map(extrapolate, reversed_arrays)))