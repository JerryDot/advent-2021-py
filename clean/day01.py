from collections import deque
from typing import List
from functools import reduce


def get_input() -> List[int]:
    with open('../fast/day01/day01.txt', 'rb') as f:
        input = list(map(int, f.readlines()))
    return input


def part_one(input: List[int]) -> int:
    return reduce(
        lambda acc, pair: int(pair[1] > pair[0]) + acc,
        zip(input, input[1:]),
        0
    )


def part_one_alt(input: List[int]) -> int:
    return sum(map(
        lambda pair: int(pair[1] > pair[0]),
        zip(input, input[1:])
    ))


def part_two(input: List[int]) -> int:
    last_three = deque(input[:3])
    last_sum = sum(last_three)
    ans = 0
    for thing in input[3:]:
        last_three.append(thing)
        last_three.popleft()
        new_sum = sum(last_three)
        if new_sum > last_sum:
            ans += 1
        last_sum = new_sum
    return ans


def part_two_alt(input: List[int]) -> int:
    return sum(
        map(
            lambda pair: int(sum(pair[1]) > sum(pair[0])),
            zip(
                zip(input, input[1:], input[2:]),
                zip(input[1:], input[2:], input[3:])
            )
        )
    )


def part_two_ext(input: List[int]) -> int:
    return part_one(
        list(map(sum, zip(
            input, input[1:], input[2:]
        )))
    )


if __name__ == '__main__':
    input = get_input()
    print(part_one(input))
    print(part_one_alt(input))
    print(part_two(input))
    print(part_two_alt(input))
    print(part_two_ext(input))
