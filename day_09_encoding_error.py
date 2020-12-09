import itertools


def part_1(data):
    for i, line in enumerate(data[25:], 25):
        if not any(j+k == line for j, k in itertools.combinations(data[i-25:i], r=2)):
            return line


def part_2(data):
    goal = part_1(data)
    for length in range(2, len(data)):
        for start in range(0, len(data)):
            sequence = data[start:start+length] 
            if sum(sequence) == goal:
                return min(sequence) + max(sequence)


if __name__ == '__main__':
    with open('day_09_input.txt', 'r') as f:
        inp = list(map(int, f.readlines()))
        print("Part 1 answer: " + str(part_1(inp)))
        print("Part 2 answer: " + str(part_2(inp)))
