

from typing import List


def parse_input() -> List[str]:
    with open('day03.txt', 'rb') as f:
        INPUT = list(map(lambda x: x.strip(), map(lambda x: x.decode("utf-8"), f.readlines())))
    return INPUT

def part_one(input: list) -> int:
    entry_size = len(input[0])
    input_length = len(input)
    summer = map(lambda x: map(int, list(x)), input)
    resultant = [sum(x) for x in zip(*summer)]
    
    def translate(count: int) -> str:
        if count >= input_length / 2:
            return '1'
        else:
            return '0'
    gamma = int(''.join(list(map(translate, resultant))), 2)
    epsilon = int(''.join(list(map(translate, resultant))).replace('1', '2').replace('0', '1').replace('2', '0'), 2)
    
    return gamma * epsilon

def part_two(input: list, depth: int = 0) -> int:
    def get_most_pop(input: List[str]) -> str:
        one_count = sum(map(lambda x: int(x[depth]), input))
        if one_count < len(input) / 2:
            return '1'
        else:
            return '0'
    
    def filter_entry(input: List[str], pop: str) -> List[str]:
        return list(filter(lambda x: x[depth] == pop, input))
    
    pop = get_most_pop(input)
    smaller_input = filter_entry(input, pop)
    if len(smaller_input) == 1:
        return smaller_input[0]
    else:
        return part_two(smaller_input, depth + 1)

if __name__ == "__main__":
    print(part_one(parse_input()))
    print(part_two(parse_input()))
    print(int('010000101111', 2) * int('111001111010', 2))