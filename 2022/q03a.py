from aocd.models import Puzzle
from string import ascii_letters

puzzle = Puzzle(year=2022, day=3)
priorites = { c: i + 1 for i, c in enumerate(ascii_letters) }

sum_prior = 0
for line in puzzle.input_data.splitlines():
    L = len(line)
    s1 = set(line[:L//2])
    s2 = set(line[L//2:])
    s = s1 & s2
    sum_prior += sum(priorites[c] for c in s)

puzzle.answer_a = sum_prior