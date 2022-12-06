from aocd.models import Puzzle
puzzle = Puzzle(year=2022, day=6)

ans = 0
for i in range(len(puzzle.input_data) - 3):
    if (len(set(puzzle.input_data[i:i + 4])) == 4):
        ans = i + 4
        break

puzzle.answer_a = ans