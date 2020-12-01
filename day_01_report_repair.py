import itertools


def part_1(data):
    for i, j in itertools.combinations(map(int, data), 2):
        if i + j == 2020:
            return i * j


def part_2(data):
    for i, j, k in itertools.combinations(map(int, data), 3):
        if i + j + k == 2020:
            return i * j * k


if __name__ == '__main__':
    with open('day_01_input.txt', 'r') as f:
        inp = f.readlines()
        print("Part 1 answer: " + str(part_1(inp)))
        print("Part 2 answer: " + str(part_2(inp)))
