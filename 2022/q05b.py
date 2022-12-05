import re
from collections import deque
from aocd.models import Puzzle
puzzle = Puzzle(year=2022, day=5)

crates, sequence = puzzle.input_data.split("\n\n")
crates = crates.splitlines()
numbers = crates[-1].strip()
total = int(numbers[-1])
cargoes = [deque() for _ in range(total)]

for line in crates[:-1]:
    for i, j in enumerate(range(1, len(line), 4)):
        if (line[j] == ' '):
            continue
        cargoes[i].append(line[j])

temp = deque()
for line in sequence.splitlines():
    crates, frm, to = map(int, re.findall(r'\d+', line))
    
    for _ in range(crates):
        temp.append(cargoes[frm - 1].popleft())
    
    for _ in range(crates):
        cargoes[to - 1].appendleft(temp.pop())

puzzle.answer_b = ''.join(map(str, [i[0] for i in cargoes]))