import itertools
import re


def part_1(data):
    values = dict()
    for line in data:
        if line.startswith("mask"):
            mask = line.rstrip()[7:]
        else:
            address, value = re.findall(r"(\d+)", line)
            value = bin(int(value))[2:].zfill(36)
            result = "".join(m_bit if m_bit != "X" else v_bit
                             for m_bit, v_bit in zip(mask, value))
            values[address] = int(result, 2)

    return sum(v for v in values.values())


def part_2(data):
    values = dict()
    for line in data:
        if line.startswith("mask"):
            mask = line.rstrip()[7:]
        else:
            address, value = re.findall(r"(\d+)", line)
            address = bin(int(address))[2:].zfill(36)

            result = "".join(m_bit if m_bit != "0" else a_bit
                             for m_bit, a_bit in zip(mask, address)).split("X")

            for floating in itertools.product("01", repeat=len(result)-1):
                address = ""
                for r_bit, f_bit in itertools.zip_longest(result, floating, fillvalue=""):
                    address += r_bit + f_bit
                values[address] = int(value)

    return sum(v for v in values.values())


if __name__ == '__main__':
    with open('day_14_input.txt', 'r') as f:
        inp = f.readlines()
        print("Part 1 answer: " + str(part_1(inp)))
        print("Part 2 answer: " + str(part_2(inp)))
