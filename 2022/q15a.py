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


y = 2000000
signals = []

for line in puzzle.input_data.splitlines():
    sx, bx = map(int, find_x.findall(line))
    sy, by = map(int, find_y.findall(line))
    signals.append(Signal((sx, sy), (bx, by)))


beacons = set()
positions = set()
min_x = max_x = None

for signal in signals:
    sx, sy = signal.sensor
    dist = signal.range - abs(y - sy)

    if (dist < 0): continue

    if (min_x is None and max_x is None):
        max_x = sx + dist
        min_x = sx - dist

    elif ((sx + dist > max_x and sx - dist > max_x) or 
        (sx + dist < min_x and sx - dist < min_x)):
        positions.update(range(min_x, max_x + 1))
        max_x = sx + dist
        min_x = sx - dist

    else:
        if (sx + dist > max_x and min_x <= sx - dist <= max_x):
            max_x = (sx + dist)

        if (sx - dist < min_x and min_x <= sx + dist <= max_x):
            min_x = (sx - dist)

    if (y == signal.beacon[1]): beacons.add(signal.beacon[0])
            

positions.update(range(min_x, max_x + 1))
positions = positions - beacons
puzzle.answer_a = len(positions)