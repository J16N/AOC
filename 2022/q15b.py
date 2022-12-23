import re
from aocd.models import Puzzle

puzzle = Puzzle(year=2022, day=15)
find_x = re.compile(r"(?<=x\=)\-?\d+")
find_y = re.compile(r"(?<=y\=)\-?\d+")

class Signal:
    def __init__(self, sensor, beacon):
        self.sensor = sensor
        self.beacon = beacon
        self.range = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])

    def get_dist(self, x, y):
        return abs(x - self.sensor[0]) + abs(y - self.sensor[1])


signals = []

for line in puzzle.input_data.splitlines():
    sx, bx = map(int, find_x.findall(line))
    sy, by = map(int, find_y.findall(line))
    signals.append(Signal((sx, sy), (bx, by)))


possible_positions = set()
in_range = lambda x, y: 0 <= x <= 4000000 and 0 <= y <= 4000000

def add_pos(signal, positions):
    cx, cy = signal.sensor
    dist = signal.range + 1
    offset = 0

    while (dist >= 0):
        x1 = cx - dist
        x2 = cx + dist
        y1 = cy - offset
        y2 = cy + offset

        if (in_range(x1, y1)):
            positions.add((x1, y1))

        if (in_range(x2, y2)):
            positions.add((x2, y2))

        if (in_range(x1, y2)):
            positions.add((x1, y2))

        if (in_range(x2, y1)):
            positions.add((x2, y1))

        dist -= 1
        offset += 1


for signal in signals:
    add_pos(signal, possible_positions)

for position in possible_positions:
    found = True
    x, y = position
    
    for signal in signals:
        if (signal.get_dist(x, y) < signal.range):
            found = False
            break

    if (found):
        print(x, y)
        print(x * 4000000 + y)
        puzzle.answer_b = x * 4000000 + y
        break