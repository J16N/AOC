from aocd.models import Puzzle

puzzle = Puzzle(year=2022, day=14)

def get_coordinate(s):
    x, y = s.split(',')
    return (int(y), int(x))

maze = [['.'] * 1000 for _ in range(1000)]
maze[0][500] = '+'

for line in puzzle.input_data.splitlines():
    coordinates = line.split(' -> ')
    coordinates = tuple(map(get_coordinate, coordinates))
    
    for i in range(len(coordinates) - 1):
        start = coordinates[i]
        end = coordinates[i + 1]

        if (start[0] == end[0]):
            begin = min(start[1], end[1])
            finish = max(start[1], end[1]) + 1
            
            for j in range(begin, finish):
                maze[start[0]][j] = '#'

        elif (start[1] == end[1]):
            begin = min(start[0], end[0])
            finish = max(start[0], end[0]) + 1
            
            for j in range(begin, finish):
                maze[j][start[1]] = '#'


sand = [0, 500]
units = 0

while True:
    i, j = sand
    try:
        if (maze[i + 1][j] == '.'):
            sand[0] += 1

        elif (maze[i + 1][j - 1] == '.'):
            sand[0] += 1
            sand[1] -= 1

        elif (maze[i + 1][j + 1] == '.'):
            sand[0] += 1
            sand[1] += 1

        else:
            maze[i][j] = 'O'
            sand = [0, 500]
            units += 1

    except:
        break


print(units)
puzzle.answer_a = units