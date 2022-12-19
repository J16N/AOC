from aocd.models import Puzzle
puzzle = Puzzle(year=2022, day=10)

def display(sig, x, crt):
    if (abs(crt - x) <= 1):
        print("#", end='')
    else:
        print(".", end='')
    
    if (sig % 40 == 0):
        crt = 0
        print()
    else:
        crt += 1
    
    return crt


signal, X, crt = 0, 1, 0

for command in puzzle.input_data.splitlines():
    if (command[0] == 'n'):
        signal += 1
        crt = display(signal, X, crt)
    
    else:
        signal += 1
        crt = display(signal, X, crt)
        signal += 1
        crt = display(signal, X, crt)
        X += int(command.split()[-1])

# puzzle.answer_b = "PHLHJGZA"