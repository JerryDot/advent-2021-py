bingo_order = [6,69,28,50,36,84,49,13,48,90,1,33,71,0,94,59,53,58,60,96,30,34,29,91,11,41,77,95,17,80,85,93,7,9,74,89,18,25,26,8,87,38,68,5,12,43,27,46,62,73,16,55,22,4,65,76,54,52,83,10,21,67,15,47,45,40,35,66,79,51,75,39,64,24,37,72,3,44,82,32,78,63,57,2,86,31,19,92,14,97,20,56,88,81,70,61,42,99,23,98]

from typing import List, Tuple


class Card:
    
    def __init__(self, entry_info: bytes) -> None:
        rows = map(lambda x: x.decode('utf-8'), entry_info.split(b'\n'))
        self.grid = list(map(lambda x: x.split(), rows))
    
    def mark_number(self, number: int) -> None:
        for i, row in enumerate(self.grid):
            self.grid[i] = [x if x != str(number) else 'x' for x in row]

    def check_finished(self) -> bool:
        for row in self.grid:
            if all(x == 'x' for x in row):
                return True
        for col in range(len(self.grid[0])):
            if all(x == 'x' for x in [y[col] for y in self.grid]):
                return True
        return False
    
    def get_remaining_sum(self) -> int:
        total = 0
        for row in self.grid:
            for value in row:
                if value != 'x':
                    total += int(value)
        return total

    def get_result(self) -> Tuple[int, int]:
        """ Return the index of the number called to solve & the answer """
        for i, number in enumerate(bingo_order):
            self.mark_number(number)
            if self.check_finished():
                return i, self.get_remaining_sum() * number
        return 10000000, 10000000
        


    


def parse_input() -> List[str]:
    with open('day04.txt', 'rb') as f:
        INPUT = f.read().split(b'\n\n')
    return INPUT

def part_one(input: list) -> int:
    quickest = 100000
    best_score = 0
    for bingo_card in input:
        current = Card(bingo_card)
        turn, score = current.get_result()
        print(f"turn is {turn} and score is {score}")
        if turn < quickest:
            quickest = turn
            best_score = score
    return best_score


def part_two(input: list) -> int:
    quickest = 0
    best_score = 0
    for bingo_card in input:
        current = Card(bingo_card)
        turn, score = current.get_result()
        print(f"turn is {turn} and score is {score}")
        if turn > quickest:
            quickest = turn
            best_score = score
    return best_score

if __name__ == "__main__":
    parse_input()
    print(part_one(parse_input()))
    print(part_two(parse_input()))
    # print(int('010000101111', 2) * int('111001111010', 2))