import ast, functools
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
packets = [[[2]], [[6]]]

for i, input in enumerate(inputs):
    left, right = input.splitlines()
    left = ast.literal_eval(left)
    right = ast.literal_eval(right)
    packets.append(left)
    packets.append(right)


packets.sort(key=functools.cmp_to_key(compare))
a = packets.index([[2]])
b = packets.index([[6]], a + 1)
puzzle.answer_b = (a + 1) * (b + 1)