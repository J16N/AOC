from aocd.models import Puzzle
puzzle = Puzzle(year=2022, day=8)

tree_map = tuple(
    tuple(map(int, tuple(line))) 
    for line in puzzle.input_data.splitlines()
)

visible_trees = 4 * (len(tree_map) - 1)

def visible(row, col, n, tm):
    # check left
    if (all(tm[row][i] < tm[row][col] for i in range(col))):
        return True
    # check right
    if (all(tm[row][col] > tm[row][i] for i in range(col + 1, n))):
        return True
    # check up
    if (all(tm[i][col] < tm[row][col] for i in range(row))):
        return True
    # check down
    if (all(tm[row][col] > tm[i][col] for i in range(row + 1, n))):
        return True
    return False


N = len(tree_map)
for i in range(1, N - 1):
    for j in range(1, N - 1):
        if (visible(i, j, N, tree_map)):
            visible_trees += 1


puzzle.answer_a = visible_trees