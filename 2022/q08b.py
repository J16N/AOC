from aocd.models import Puzzle
puzzle = Puzzle(year=2022, day=8)

tree_map = tuple(
    tuple(map(int, tuple(line))) 
    for line in puzzle.input_data.splitlines()
)

visible_trees = 4 * (len(tree_map) - 1)

def distance(row, col, n, tm):
    if (row in (0, n - 1) or col in (0, n - 1)):
        return 0
    
    left = right = up = down = 0
    for i in range(col - 1, -1, -1):
        left += 1
        if (tm[row][i] >= tm[row][col]):
            break

    for i in range(col + 1, n):
        right += 1
        if (tm[row][i] >= tm[row][col]):
            break

    for i in range(row - 1, -1, -1):
        up += 1
        if (tm[i][col] >= tm[row][col]):
            break

    for i in range(row + 1, n):
        down += 1
        if (tm[i][col] >= tm[row][col]):
            break

    return left * right * up * down


N = len(tree_map)
max_dist = -float('inf')

for i in range(1, N - 1):
    for j in range(1, N - 1):
        max_dist = max(max_dist, distance(i, j, N, tree_map))


puzzle.answer_b = max_dist