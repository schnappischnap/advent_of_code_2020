from collections import defaultdict
from math import prod
import re


def part_1(data):
    valid = set()
    for line in data[:20]:
        for a, b in re.findall(r"(\d+)-(\d+)", line):
            valid.update(range(int(a), int(b)+1))

    return sum(int(i) for line in data[25:]
               for i in line.split(",")
               if int(i) not in valid)


def part_2(data):
    # Build dictionary of possible values for each field.
    fields = defaultdict(set)
    for line in data[:20]:
        field_name = line.split(":")[0]
        for a, b in re.findall(r"(\d+)-(\d+)", line):
            fields[field_name].update(range(int(a), int(b)+1))
    all_values = set(i for field in fields.values() for i in field)

    # Find all possible value indices for each field.
    possible = {field: set(range(20)) for field in fields.keys()}
    for line in data[25:]:
        line = line.split(",")
        if not all(int(v) in all_values for v in line):
            continue
        for field in fields:
            possible[field].intersection_update(i for i, v in enumerate(line)
                                                if int(v) in fields[field])

    # Reduce the possible value indices until there's only 1 for each field.
    while not all(len(v) == 1 for v in possible.values()):
        for field, values in possible.items():
            if len(values) == 1:
                possible = {k: (v.difference(values) if k != field else v)
                            for k, v in possible.items()}

    ticket = list(map(int, data[22].split(",")))
    return prod(ticket[tuple(v)[0]]
                for k, v in possible.items()
                if k.startswith("departure"))


if __name__ == '__main__':
    with open('day_16_input.txt', 'r') as f:
        inp = f.readlines()
        print("Part 1 answer: " + str(part_1(inp)))
        print("Part 2 answer: " + str(part_2(inp)))
