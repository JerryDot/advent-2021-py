from collections import deque
from typing import List


def get_input() -> List[int]:
    with open('../fast/day01/day01.txt', 'rb') as f:
        input = list(map(int, f.readlines()))
    return input


def part_one(input: List[int]) -> int:
    previous_number = 9999999
    ans = 0
    for number in input:
        if number > previous_number:
            ans += 1
        previous_number = number
    return ans


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


if __name__ == '__main__':
    input = get_input()
    print(part_one(input))
    print(part_two(input))