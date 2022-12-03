from aocd.models import Puzzle
puzzle = Puzzle(year=2022, day=2)

shape_scores = { 'A': 1, 'B': 2, 'C': 3 }
losing_moves = { 'A': 'C', 'C': 'B', 'B': 'A' }
winning_moves = { 'A': 'B', 'B': 'C', 'C': 'A' }

scores = 0
for line in puzzle.input_data.splitlines():
    opponent, move = line.split()
    
    # make a losing move
    if (move == 'X'):
        myself = losing_moves[opponent]
        score = 0

    # make a move to end the game in draw
    elif (move == 'Y'):
        myself = opponent
        score = 3

    # make a winning move
    else:
        myself = winning_moves[opponent]
        score = 6

    scores += shape_scores[myself] + score

puzzle.answer_b = scores