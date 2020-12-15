from collections import defaultdict


def part_1(data):
    return play(list(map(int, data.split(","))), 2020)


def part_2(data):
    # Takes a few seconds, but fast enough not to bother optimising
    return play(list(map(int, data.split(","))), 30000000)


def play(starting, iterations):
    numbers = defaultdict(lambda: (None, None),
                          {n: (None, i) for i, n in enumerate(starting)})
    previous = starting[-1]

    for i in range(len(numbers), iterations):
        current = (0 if numbers[previous][0] is None
                   else numbers[previous][1] - numbers[previous][0])
        numbers[current] = (numbers[current][1], i)
        previous = current

    return previous


if __name__ == '__main__':
    with open('day_15_input.txt', 'r') as f:
        inp = f.read()
        print("Part 1 answer: " + str(part_1(inp)))
        print("Part 2 answer: " + str(part_2(inp)))
