import itertools


def part_1(data):
    seats = [[c for c in line.strip()] for line in data]
    w = len(seats[0])
    h = len(seats)

    def neighbours(x, y):
        return [(x + dx, y + dy)
                for dx in range(-1, 2)
                for dy in range(-1, 2)
                if (dx, dy) != (0, 0) and 0 <= (x+dx) < w and 0 <= (y+dy) < h]

    while True:
        new_seats = [row[:] for row in seats]
        for y, row in enumerate(seats):
            for x, c in enumerate(row):
                if c == ".":
                    continue

                count = sum(seats[ny][nx] == "#" for nx, ny in neighbours(x, y))
                if c == "L" and count == 0:
                    new_seats[y][x] = "#"
                elif c == "#" and count >= 4:
                    new_seats[y][x] = "L"

        if seats == new_seats:
            return sum(c == "#" for row in seats for c in row)
        seats = new_seats


def part_2(data):
    seats = [[c for c in line.strip()] for line in data]
    w = len(seats[0])
    h = len(seats)

    def visible_from(x, y):
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if (dx, dy) == (0, 0):
                    continue
                
                distance = 1
                while 0 <= x+(dx*distance) < w and 0 <= y+(dy*distance) < h:
                    c = seats[y+dy*distance][x+dx*distance]
                    if c != ".":
                        yield c
                        break
                    distance += 1 

    while True:
        new_seats = [row[:] for row in seats]
        for y, row in enumerate(seats):
            for x, c in enumerate(row):
                if c == ".":
                    continue

                count = sum(c == "#" for c in visible_from(x, y))
                if c == "L" and count == 0:
                    new_seats[y][x] = "#"
                elif c == "#" and count >= 5:
                    new_seats[y][x] = "L"

        if seats == new_seats:
            return sum(c == "#" for row in seats for c in row)
        seats = [row[:] for row in new_seats]


if __name__ == '__main__':
    with open('day_11_input.txt', 'r') as f:
        inp = f.readlines()
        print("Part 1 answer: " + str(part_1(inp)))
        print("Part 2 answer: " + str(part_2(inp)))
