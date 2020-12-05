def part_1(data):
    return max(calculate_id(line) for line in data)


def part_2(data):
    seats = set(calculate_id(line) for line in data)

    for seat_id in range(127 * 8):
        if seat_id not in seats and seat_id + 1 in seats and seat_id - 1 in seats:
            return seat_id


def calculate_id(seat):
    # Just convert the seat string into binary...
    # return int(seat.translate(str.maketrans("FLBR", "0011")), 2)

    seat_id = 0
    for i, c in enumerate(seat):
        if c == "B":
            seat_id += (2**(6-i)) * 8
        elif c == "R":
            seat_id += (2**(9-i))
    return seat_id 


if __name__ == '__main__':
    with open('day_05_input.txt', 'r') as f:
        inp = f.readlines()
        print("Part 1 answer: " + str(part_1(inp)))
        print("Part 2 answer: " + str(part_2(inp)))
