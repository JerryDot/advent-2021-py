

from typing import List, Tuple



def parse_input() -> List[str]:
    with open('day05.txt', 'rb') as f:
        INPUT = f.readlines()

    def parse_line(line: bytes) -> Tuple[int, int, int, int]:
        coords = line.split(b' -> ')
        x_zero, y_zero = map(int, coords[0].split(b','))
        x_one, y_one = map(int, coords[1].split(b','))
        return x_zero, y_zero, x_one, y_one
    return list(map(parse_line, INPUT))


def part_one(input: list) -> int:
    world = [ [ 0 for i in range(1000) ] for j in range(1000) ]
    for line in input:
        if line[0] == line[2]:
            lower = min(line[1], line[3])
            larger = max(line[1], line[3])
            for y in range(lower, larger + 1):
                world[line[0]][y] += 1
        if line[1] == line[3]:
            lower = min(line[0], line[2])
            larger = max(line[0], line[2])
            for x in range(lower, larger + 1):
                world[x][line[1]] += 1
    total = 0
    for i, x in enumerate(world):
        for j, y in enumerate(x):
            if y >= 2:
                total += 1
    return total
        

def part_two(input: list) -> int:
    world = [ [ 0 for i in range(1000) ] for j in range(1000) ]
    for line in input:
        if line[0] == line[2]:
            lower = min(line[1], line[3])
            larger = max(line[1], line[3])
            for y in range(lower, larger + 1):
                world[line[0]][y] += 1
        elif line[1] == line[3]:
            lower = min(line[0], line[2])
            larger = max(line[0], line[2])
            for x in range(lower, larger + 1):
                world[x][line[1]] += 1
        else:
            if line[0] < line[2]:
                xrange = range(line[0], line[2] + 1)
            else:
                xrange = range(line[0], line[2] - 1, -1)
            if line[1] < line[3]:
                yrange = range(line[1], line[3] + 1)
            else:
                yrange = range(line[1], line[3] - 1, -1)
            for x,y in zip(xrange, yrange):
                world[x][y] += 1
    total = 0
    for i, x in enumerate(world):
        for j, y in enumerate(x):
            if y >= 2:
                total += 1
    return total


if __name__ == "__main__":
    print(part_one(parse_input()))
    print(part_two(parse_input()))
    print(int('010000101111', 2) * int('111001111010', 2))