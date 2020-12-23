from collections import deque
import itertools


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def part_1(data):
    cups = deque(int(c) for c in data.strip())
    current_i = 0
    current_cup = cups[0]
    max_value = max(cups)
    for _ in range(100):
        # print(str(_+1) + ": " + str(list(cups)))
        #print("cups: " + str(list(cups)))
        #print("current cup: " + str(current_cup))

        three_cups = []
        indices = [i % len(cups) for i in range(current_i+1, current_i+4)]
        for i in indices:
            three_cups.append(cups[i])
        for i in reversed(sorted(indices)):
            del cups[i]

        #print("pick up: " + str(three_cups))

        destination_cup = (current_cup - 1) % (max_value+1)
        while destination_cup not in cups:
            destination_cup = (destination_cup - 1) % (max_value+1)
        destination_i = cups.index(destination_cup)

        #print("destination cup: " + str(destination_cup) + " i: " + str(destination_i))
        # print()

        for i, cup in enumerate(three_cups, start=1):
            cups.insert((destination_i+i) % (len(cups) + 1), cup)

        current_i = (cups.index(current_cup) + 1) % len(cups)
        current_cup = cups[current_i]

    cup_1_index = cups.index(1)
    cups.rotate(-cup_1_index)

    return "".join(str(c) for c in list(cups)[1:])


def part_2(data):
    max_value = 1000000
    steps = 10000000
    cups = [int(c) for c in data.strip()] + list(range(10, max_value+1))
    nodes = dict()

    for i in range(1, max_value+1)
    nodes[i] = Node(i)
    for i, cup in enumerate(cups):
        nodes[cup].next = nodes[cups[(i+1) % len(cups)]]

    current_cup = nodes[cups[0]]

    for _ in range(steps):
        pick_up = current_cup.next
        current_cup.next = current_cup.next.next.next.next

        current_cup_value = current_cup.value
        while current_cup_value in [0, current_cup.value, pick_up.value,
                                    pick_up.next.value, pick_up.next.next.value]:
            current_cup_value = (current_cup_value - 1) % (max_value+1)

        destination = nodes[current_cup_value]
        pick_up.next.next.next = destination.next
        destination.next = pick_up

        current_cup = current_cup.next

    return nodes[1].next.value * nodes[1].next.next.value


if __name__ == '__main__':
    with open('day_23_input.txt', 'r') as f:
        inp = f.read()
        print("Part 1 answer: " + str(part_1(inp)))
        print("Part 2 answer: " + str(part_2(inp)))
