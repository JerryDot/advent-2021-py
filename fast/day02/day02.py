from typing import Iterable, List, Tuple


"""
----------> (1,0)
|
|
|
|
v
(0,1)
"""

def parse_input() -> List[Tuple[int, int]]:
    with open('day02.txt', 'rb') as f:
        INPUT = map(lambda x: x.strip(), map(lambda x: x.decode("utf-8"), f.readlines()))
    moves = []
    for entry in INPUT:
        direction, size = entry.split()[0], int(entry.split()[1])
        if direction == "forward":
            moves.append((size, 0))
        elif direction == "backward":
            moves.append((-size, 0))
        elif direction == "down":
            moves.append((0, size))
        elif direction == "up":
            moves.append((0, -size))
        else:
            raise Exception("This should not occur")
    return moves


def part_one(p_input: List[Tuple[int, int]]) -> int:
    position = [0, 0]
    for move in p_input:
        position[0] += move[0]
        position[1] += move[1]
    return position[0] * position[1]

def part_two(p_input: List[Tuple[int, int]]) -> int:
    position = [0, 0]
    aim = 0
    for move in p_input:
        position[0] += move[0]
        position[1] += move[0] * aim
        aim += move[1]

    return position[0] * position[1]


if __name__ == "__main__":
    print(part_one(parse_input()))
    print(part_two(parse_input()))


