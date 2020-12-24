from collections import defaultdict
import copy
import re


def part_1(data):
    pattern = re.compile(r"(se|sw|ne|nw|e|w)")
    delta = {"se": (1, 1), "sw": (-1, 1), "ne": (1, -1), 
             "nw": (-1, -1), "e": (2, 0), "w": (-2, 0)}

    black_tiles = defaultdict(bool)
    for line in data: 
        x, y = 0, 0
        for step in pattern.finditer(line):
            d = delta[step.group(0)]
            x += d[0]
            y += d[1]
        black_tiles[(x, y)] = not black_tiles[(x, y)]
    
    return sum(v for v in black_tiles.values())


def part_2(data):
    pattern = re.compile(r"(se|sw|ne|nw|e|w)")
    delta = {"se": (1, 1), "sw": (-1, 1), "ne": (1, -1),
             "nw": (-1, -1), "e": (2, 0), "w": (-2, 0)}

    black_tiles = defaultdict(bool)
    for line in data: 
        x, y = 0, 0
        for step in pattern.finditer(line):
            d = delta[step.group(0)]
            x += d[0]
            y += d[1]
        black_tiles[(x, y)] = not black_tiles[(x, y)]
    
    def neighbours(x, y):
        return [(x + dx, y + dy) for dx, dy in delta.values()]

    for _ in range(100): 
        black_tiles_copy = copy.copy(black_tiles)

        neighbours_count = defaultdict(int)
        for position, is_black in black_tiles.items():
            if is_black:
                if position not in neighbours_count:
                    neighbours_count[position] = 0
                for neighbour in neighbours(position[0], position[1]):
                    neighbours_count[neighbour] += 1
        
        for position, n_count in neighbours_count.items():
            if black_tiles[position] and (n_count == 0 or n_count > 2):
                black_tiles_copy[position] = False
            if black_tiles[position] == False and n_count == 2:
                black_tiles_copy[position] = True
        
        black_tiles = copy.copy(black_tiles_copy)
    
    return sum(v for v in black_tiles.values())


if __name__ == '__main__':
    with open('day_24_input.txt', 'r') as f:
        inp = f.readlines()
        print("Part 1 answer: " + str(part_1(inp)))
        print("Part 2 answer: " + str(part_2(inp)))
