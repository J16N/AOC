from aocd.models import Puzzle
puzzle = Puzzle(year=2022, day=10)

def log_signal(sig, x, sigs):
    if (sig in (20, 60, 100, 140, 180, 220)):
        sigs.append(x * sig)

signal, X = 0, 1
sig_strengths = []

for command in puzzle.input_data.splitlines():
    if (command[0] == 'n'):
        signal += 1
        log_signal(signal, X, sig_strengths)
    
    else:
        signal += 1
        log_signal(signal, X, sig_strengths)
        signal += 1
        log_signal(signal, X, sig_strengths)
        X += int(command.split()[-1])

puzzle.answer_a = sum(sig_strengths)