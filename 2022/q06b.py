from aocd.models import Puzzle
puzzle = Puzzle(year=2022, day=6)

ans = 0
for i in range(len(puzzle.input_data) - 13):
    if (len(set(puzzle.input_data[i:i + 14])) == 14):
        ans = i + 14
        break

puzzle.answer_b = ans