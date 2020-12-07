from collections import defaultdict
import re


def part_1(data):
    contained_in = defaultdict(list)
    for line in data:
        match = re.findall(r"(\w+ \w+) bag", line)
        for bag in match[1:]:
            contained_in[bag].append(match[0])

    answer = set()
    def r(bag):
        for outer_bag in contained_in[bag]:
            answer.add(outer_bag)
            r(outer_bag)
    r("shiny gold")

    return len(answer)


def part_2(data):
    contains = defaultdict(list)
    for line in data:
        match = re.findall(r"(\d )?(\w+ \w+) bag", line)
        for count, bag in match[1:]:
            if bag != "no other":
                contains[match[0][1]].append((int(count), bag))

    def r(count, bag, total=0):
        total += count
        for inner_count, inner_bag in contains[bag]:
            total += r(inner_count*count, inner_bag)
        return total

    return r(1, "shiny gold") - 1  # Account for the original shiny gold bag


if __name__ == '__main__':
    with open('day_07_input.txt', 'r') as f:
        inp = f.readlines()
        print("Part 1 answer: " + str(part_1(inp)))
        print("Part 2 answer: " + str(part_2(inp)))
