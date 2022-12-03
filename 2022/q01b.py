from aocd.models import Puzzle
puzzle = Puzzle(year=2022, day=1)

calories = [
    sum(map(int, lines.splitlines()))
    for lines in puzzle.input_data.split("\n\n")
]

calories.sort(reverse=True)
puzzle.answer_b = sum(calories[:3])