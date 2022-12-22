import ast
from aocd.models import Puzzle

puzzle = Puzzle(year=2022, day=13)


def compare(left, right):
    if (type(left) == int and type(right) == int):
        return left - right

    elif (type(left) == list and type(right) == list):
        i = 0
        while (i < len(left) and i < len(right)):
            cmp = compare(left[i], right[i])
            if (cmp): return cmp
            i += 1

        if (i == len(left) and i < len(right)):
            return -1

        elif (i < len(left) and i == len(right)):
            return 1

        else:
            return 0

    elif (type(left) == int and type(right) == list):
        return compare([left], right)

    else:
        return compare(left, [right])
        

sum_of_indices = 0
inputs = puzzle.input_data.split("\n\n")

for i, input in enumerate(inputs):
    left, right = input.splitlines()
    left = ast.literal_eval(left)
    right = ast.literal_eval(right)

    if (compare(left, right) < 0):
        sum_of_indices += (i + 1)


puzzle.answer_a = sum_of_indices