def part_1(data):
    public_keys = [int(line.strip()) for line in data]

    key, loop_size = None, None
    value = 1
    for i in range(1, 10000000):
        value = (value * 7) % 20201227
        if value in public_keys:
            key = public_keys[public_keys.index(value)-1]
            loop_size = i
            break

    value = 1
    for _ in range(loop_size):
        value = (value * key) % 20201227
    return value


def part_2(data):
    return None


if __name__ == '__main__':
    with open('day_25_input.txt', 'r') as f:
        inp = f.readlines()
        print("Part 1 answer: " + str(part_1(inp)))
