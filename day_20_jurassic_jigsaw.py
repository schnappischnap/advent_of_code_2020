from collections import defaultdict, namedtuple
from math import prod


Point = namedtuple("Point", "x y")


def part_1(data):
    def get_edges(tile):
        yield tile[0]
        yield "".join(reversed(list(tile[0])))
        yield "".join(tile[-1])
        yield "".join(reversed(list(tile[-1])))
        yield "".join(line[0] for line in tile)
        yield "".join(reversed(list(line[0] for line in tile)))
        yield "".join(line[-1] for line in tile)
        yield "".join(reversed(list(line[-1] for line in tile)))

    edge_count = defaultdict(int)
    tiles = dict()
    for tile in data.split("\n\n"):
        tile_id = int(tile[5:9])

        tile_edges = list(get_edges(tile.splitlines()[1:]))
        for edge in tile_edges:
            edge_count[edge] += 1
        tiles[tile_id] = tile_edges
        
    return prod(tile_id for tile_id, edges in tiles.items()
                        if sum(edge_count[edge] == 1 for edge in edges) == 4)


def part_2(data):
    def get_edges(tile):
        yield tile[0]
        yield "".join(line[-1] for line in tile)
        yield tile[-1]
        yield "".join(line[0] for line in tile)

    def get_edge(tile, direction):
        if direction == "N":
            return tile[0]
        elif direction == "E":
            return "".join(line[-1] for line in tile)
        elif direction == "S":
            return tile[-1]
        elif direction == "W":
            return "".join(line[0] for line in tile)

    def flipped(tile):
        return  ["".join(reversed(line)) for line in tile]

    tiles = [tile.splitlines()[1:] for tile in data.split("\n\n")]
    positions = dict()

    def check_tile(tile, direction, edge, pos):
        rotated = tile
        for _ in range(2):
            for __ in range(4):
                if direction == 0 and get_edge(rotated, "S") == edge:
                    return Point(pos.x, pos.y - 1), rotated
                elif direction == 1 and get_edge(rotated, "W") == edge:
                    return Point(pos.x + 1, pos.y), rotated
                elif direction == 2 and get_edge(rotated, "N") == edge:
                    return Point(pos.x, pos.y + 1), rotated
                elif direction == 3 and get_edge(rotated, "E") == edge:
                    return Point(pos.x - 1, pos.y), rotated
                
                rotated = ["".join(c for c in line) for line in zip(*rotated[::-1])]
            rotated = flipped(tile)
        return False
    
    def build(c_tile, c_position):
        positions[c_position] = c_tile
        for i, edge in enumerate(get_edges(c_tile)):
            for tile in tiles:
                check = check_tile(tile, i, edge, c_position)
                if check:
                    n_pos, n_tile = check
                    tiles.remove(tile)
                    build(n_tile, n_pos)
                    break

    build(tiles.pop(), Point(0, 0))

    min_y = min(k.y for k in positions.keys())
    max_y = max(k.y for k in positions.keys())
    min_x = min(k.x for k in positions.keys())
    max_x = max(k.x for k in positions.keys())
    image = []
    for y in range(min_y, max_y+1):
        for i in range(1, 9):
            line = ""
            for x in range(min_x, max_x+1):
                line += positions[Point(x, y)][i][1:-1]
            image.append(line)

    monster = ["                  # ",
               "#    ##    ##    ###",
               " #  #  #  #  #  #   "]

    def monster_here(x, y):
        for i, k in enumerate(range(y, y+len(monster))):
            for j, l in enumerate(range(x, x+len(monster[0]))):
                if image[k][l] == "." and monster[i][j] == "#":
                    return False
        return True

    for _ in range(2):
        for __ in range(4):
            count = 0
            for y in range(len(image) - len(monster)):
                for x in range(len(image[0])- len(monster[0])):
                    if monster_here(x, y):
                        count += 1
            if count > 0:
                return sum(c == "#" for line in image for c in line) - (15*count)
            
            image = ["".join(c for c in line) for line in zip(*image[::-1])]
        image = flipped(image)


if __name__ == '__main__':
    with open('day_20_input.txt', 'r') as f:
        inp = f.read()
        print("Part 1 answer: " + str(part_1(inp)))
        print("Part 2 answer: " + str(part_2(inp)))
