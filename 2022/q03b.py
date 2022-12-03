from aocd.models import Puzzle
from string import ascii_letters

puzzle = Puzzle(year=2022, day=3)
priorites = { c: i + 1 for i, c in enumerate(ascii_letters) }

sum_prior = 0
lines = puzzle.input_data.splitlines()
for i in range(0, len(lines), 3):
    s1 = set(lines[i])
    s2 = set(lines[i + 1])
    s3 = set(lines[i + 2])
    s = s1 & s2 & s3
    sum_prior += sum(priorites[c] for c in s)

puzzle.answer_b = sum_prior