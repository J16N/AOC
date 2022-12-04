from aocd.models import Puzzle
puzzle = Puzzle(year=2022, day=4)

def overlaps(a, b, c, d):
    return (a <= c <= b or c <= a <= d)

total = 0
for line in puzzle.input_data.splitlines():
    r1, r2 = line.split(',')
    a, b = map(int, r1.split('-'))
    c, d = map(int, r2.split('-'))

    if (overlaps(a, b, c, d)):
        total += 1

puzzle.answer_b = total