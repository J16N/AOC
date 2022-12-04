from aocd.models import Puzzle
puzzle = Puzzle(year=2022, day=4)

def contains(a, b, c, d):
    return (a <= c <= b and a <= d <= b)

total = 0
for line in puzzle.input_data.splitlines():
    r1, r2 = line.split(',')
    a, b = map(int, r1.split('-'))
    c, d = map(int, r2.split('-'))

    if (contains(a, b, c, d) or contains(c, d, a, b)):
        total += 1

puzzle.answer_a = total