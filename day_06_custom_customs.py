def part_1(data):
    return sum(len(set(group.replace("\n", "")))
               for group in data.split("\n\n"))


def part_2(data):
    return sum(len(set.intersection(*map(set, group.splitlines())))
               for group in data.split("\n\n"))


if __name__ == '__main__':
    with open('day_06_input.txt', 'r') as f:
        inp = f.read()
        print("Part 1 answer: " + str(part_1(inp)))
        print("Part 2 answer: " + str(part_2(inp)))
