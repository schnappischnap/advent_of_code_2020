from collections import namedtuple


Point = namedtuple("Point", "x y")


def part_1(data):
    directions = {"N": Point(0, -1), "E": Point(1, 0),
                  "S": Point(0, 1), "W": Point(-1, 0)}

    position = Point(0, 0)
    heading = Point(1, 0)

    for line in data:
        instruction, amount = line[0], int(line[1:])
        if instruction in directions:
            position = Point(position.x + directions[instruction].x * amount,
                             position.y + directions[instruction].y * amount)
        elif instruction == "F":
            position = Point(position.x + heading.x * amount,
                             position.y + heading.y * amount)
        else:
            if instruction == "L":
                amount = 360 - amount

            if amount == 90:
                heading = Point(-heading.y, heading.x)
            elif amount == 270:
                heading = Point(heading.y, -heading.x)
            elif amount == 180:
                heading = Point(-heading.x, -heading.y)

    return abs(position.x) + abs(position.y)


def part_2(data):
    directions = {"N": Point(0, -1), "E": Point(1, 0),
                  "S": Point(0, 1), "W": Point(-1, 0)}
    
    position = Point(0, 0)
    waypoint = Point(10, -1)

    for line in data:
        instruction, amount = line[0], int(line[1:])

        if instruction in directions:
            waypoint = Point(waypoint.x + directions[instruction].x * amount,
                             waypoint.y + directions[instruction].y * amount)
        elif instruction == "F":
            position = Point(position.x + waypoint.x * amount,
                             position.y + waypoint.y * amount)
        else:
            if instruction == "L":
                amount = 360 - amount

            if amount == 90:
                waypoint = Point(-waypoint.y, waypoint.x)
            elif amount == 270:
                waypoint = Point(waypoint.y, -waypoint.x)
            elif amount == 180:
                waypoint = Point(-waypoint.x, -waypoint.y)

    return abs(position.x) + abs(position.y)


if __name__ == '__main__':
    with open('day_12_input.txt', 'r') as f:
        inp = f.readlines()
        print("Part 1 answer: " + str(part_1(inp)))
        print("Part 2 answer: " + str(part_2(inp)))
