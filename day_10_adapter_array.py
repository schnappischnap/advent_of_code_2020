from collections import defaultdict


def part_1(data):
    data = sorted(map(int, data))
    data = [0] + data + [max(data)+3]

    return (sum(data[i] - data[i-1] == 1 for i in range(1, len(data))) *
            sum(data[i] - data[i-1] == 3 for i in range(1, len(data))))


def part_2(data):
    data = sorted(map(int, data))

    combinations = defaultdict(int)
    combinations[0] = 1
    for jolts in data:
        combinations[jolts] = sum(combinations[jolts-i] for i in range(1, 4))
    return combinations[data[-1]]


if __name__ == '__main__':
    with open('day_10_input.txt', 'r') as f:
        inp = f.readlines()
        print("Part 1 answer: " + str(part_1(inp)))
        print("Part 2 answer: " + str(part_2(inp)))
