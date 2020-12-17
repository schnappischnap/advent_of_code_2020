import itertools


def part_1(data):
    def neighbours(x, y, z):
        return [(x + dx, y + dy, z + dz)
                for dx, dy, dz in itertools.product((-1, 0, 1), repeat=3)
                if not dx == dy == dz == 0]

    active = set((x, y, 0) for y, line in enumerate(data)
                 for x, c in enumerate(line)
                 if c == "#")

    for cycle in range(1, 7):
        active_copy = set(active)
        for z in range(-cycle, cycle+1):
            for x, y in itertools.product(range(-cycle, cycle+1), repeat=2):
                active_neighbours = sum(n in active
                                        for n in neighbours(x, y, z))
                if (x, y, z) in active and active_neighbours not in [2, 3]:
                    active_copy.remove((x, y, z))
                elif (x, y, z) not in active and active_neighbours == 3:
                    active_copy.add((x, y, z))
        active = set(active_copy)

    return len(active)


def part_2(data):
    def neighbours(x, y, z, w):
        return [(x + dx, y + dy, z + dz, w+dw)
                for dx, dy, dz, dw in itertools.product((-1, 0, 1), repeat=4)
                if not dx == dy == dz == dw == 0]

    active = set((x, y, 0, 0) for y, line in enumerate(data)
                 for x, c in enumerate(line)
                 if c == "#")

    for cycle in range(1, 7):
        active_copy = set(active)
        for w, z in itertools.product(range(-cycle, cycle+1), repeat=2):
            for x, y in itertools.product(range(-cycle, cycle+7), repeat=2):
                active_neighbours = sum(n in active
                                        for n in neighbours(x, y, z, w))
                if (x, y, z, w) in active and active_neighbours not in [2, 3]:
                    active_copy.remove((x, y, z, w))
                elif (x, y, z, w) not in active and active_neighbours == 3:
                    active_copy.add((x, y, z, w))
        active = set(active_copy)

    return len(active)


if __name__ == '__main__':
    with open('day_17_input.txt', 'r') as f:
        inp = f.readlines()
        print("Part 1 answer: " + str(part_1(inp)))
        print("Part 2 answer: " + str(part_2(inp)))
