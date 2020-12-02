import re


def part_1(data):
    pattern = re.compile(r"(\d+)-(\d+) (\w): (\w+)")
    lines = [pattern.search(line).groups() for line in data]
    return sum(int(min_count) <= password.count(char) <= int(max_count)
               for min_count, max_count, char, password in lines)


def part_2(data):
    pattern = re.compile(r"(\d+)-(\d+) (\w): (\w+)")
    lines = [pattern.search(line).groups() for line in data]
    return sum((password[int(i1)-1] == char) ^ (password[int(i2)-1] == char)
               for i1, i2, char, password in lines)


if __name__ == '__main__':
    with open('day_02_input.txt', 'r') as f:
        inp = f.readlines()
        print("Part 1 answer: " + str(part_1(inp)))
        print("Part 2 answer: " + str(part_2(inp)))
