from aocd.models import Puzzle
puzzle = Puzzle(year=2022, day=9)

rope_length = 2
rope = [[0, 0] for _ in range(rope_length)]
visited = set()
visited.add(tuple(rope[-1]))
UNIT_VECTORS = { 'L': (0, -1), 'R': (0, 1), 'U': (1, 1), 'D': (1, -1) }

def make_move(direction, steps, rope, visited):
    head = rope[0]

    for _ in range(steps):
        point, step = UNIT_VECTORS[direction]
        head[point] += step

        for i in range(1, len(rope)):
            pred = rope[i - 1]
            succ = rope[i]

            dx = pred[0] - succ[0]
            dy = pred[1] - succ[1]

            if (abs(dx) > abs(dy)):
                succ[0] += dx - (dx // abs(dx))
                succ[1] = pred[1]

            elif (abs(dx) < abs(dy)):
                succ[1] += dy - (dy // abs(dy))
                succ[0] = pred[0]

            else:
                if (dx): succ[0] += dx - (dx // abs(dx))
                if (dy): succ[1] += dy - (dy // abs(dy))
        
        visited.add(tuple(rope[-1]))


for move in puzzle.input_data.splitlines():
    direction, steps = move.split()
    make_move(direction, int(steps), rope, visited)


puzzle.answer_a = len(visited)