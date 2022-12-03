from aocd.models import Puzzle
puzzle = Puzzle(year=2022, day=2)

shape_scores = { 'X': 1, 'Y': 2, 'Z': 3 }
tie_moves = { 'X': 'A', 'Y': 'B', 'Z': 'C' }
winning_moves = { 'X': 'C', 'Y': 'A', 'Z': 'B' }

scores = 0
for line in puzzle.input_data.splitlines():
    opponent, myself = line.split()
    scores += shape_scores[myself]

    if (opponent == winning_moves.get(myself)):
        scores += 6

    elif (opponent == tie_moves.get(myself)):
        scores += 3

puzzle.answer_a = scores