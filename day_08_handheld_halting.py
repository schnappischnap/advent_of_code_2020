def part_1(data):
    return run_program(data)[0]


def part_2(data):
    for i, line in enumerate(data):
        if line.startswith("acc"):
            continue

        data_copy = data[:]
        data_copy[i] = ("nop" if line.startswith("jmp") else "jmp") + line[3:]
        
        accumulator, index = run_program(data_copy)
        if index == len(data):
            return accumulator


def run_program(data):
    index = 0
    accumulator = 0
    seen = set()
    while index not in seen and index < len(data):
        seen.add(index)
        op, arg = data[index].split()
        if op == "acc":
            accumulator += int(arg)
        elif op == "jmp":
            index += int(arg)
            continue
        index += 1
    return accumulator, index


if __name__ == '__main__':
    with open('day_08_input.txt', 'r') as f:
        inp = f.readlines()
        print("Part 1 answer: " + str(part_1(inp)))
        print("Part 2 answer: " + str(part_2(inp)))
