from string import ascii_lowercase
from collections import deque
from aocd.models import Puzzle

puzzle = Puzzle(year=2022, day=12)
heightmap = tuple(
    tuple(line)
    for line in puzzle.input_data.splitlines()
)
rows = len(heightmap)
cols = len(heightmap[0])
heights = { c: i + 1 for i, c in enumerate(ascii_lowercase) }
heights = { 'S': 1, 'E': 26, **heights }


def get_neighbours(i, j, rows, cols, visited):
    neighbours = []

    if (i + 1 < rows and not visited[i + 1][j]):
        neighbours.append((i + 1, j))
    
    if (i - 1 >= 0 and not visited[i - 1][j]):
        neighbours.append((i - 1, j))
    
    if (j + 1 < cols and not visited[i][j + 1]):
        neighbours.append((i, j + 1))
    
    if (j - 1 >= 0 and not visited[i][j - 1]):
        neighbours.append((i, j - 1))
    
    return neighbours


def hill_climbing(src, dest):
    visited = [
        [False] * cols
        for _ in range(rows)
    ]

    distances = [
        [float('inf')] * cols
        for _ in range(rows)
    ]

    si, sj = src
    fi, fj = dest
    distances[si][sj] = 0
    neighbours = deque()
    neighbours.append((distances[si][sj], si, sj))

    while (neighbours):
        step, i, j = neighbours.popleft()
        curr = heightmap[i][j]
        if (visited[i][j]): continue
        visited[i][j] = True

        for neighbour in get_neighbours(i, j, rows, cols, visited):
            a, b = neighbour
            dest = heightmap[a][b]
            height = heights[dest] - heights[curr]
            if (height > 1): continue
            if (distances[a][b] < 1 + step): continue
            distances[a][b] = 1 + step
            neighbours.append((distances[a][b], a, b))

    return distances[fi][fj]


dest = None
sources = []
for i in range(rows):
    for j in range(cols):
        if (heightmap[i][j] == 'S'):
            sources.append((i, j))

        if (heightmap[i][j] == 'E'):
            dest = (i, j)


min_dist = float("inf")
for src in sources:
    dist = hill_climbing(src, dest)
    min_dist = min(dist, min_dist)

puzzle.answer_a = min_dist