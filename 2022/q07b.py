from aocd.models import Puzzle
puzzle = Puzzle(year=2022, day=7)

class Directory:
    @staticmethod
    def get_dir(name, parent):
        dir = Directory(name, parent)
        if (not parent):
            return dir

        if (name not in parent.children):
            parent.children[name] = dir
        
        return parent.children[name]

    def set_size(self, size):
        self.size += size
        if (self.parent is None): return
        return self.parent.set_size(size)

    def __init__(self, name, parent):
        self.name = name
        self.size = 0
        self.parent = parent
        self.children = {}

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        parent_name = getattr(self.parent, 'name', None)
        return f"DIR(name={self.name}, size={self.size}, parent={parent_name})"


class File:
    def __init__(self, name, size, parent):
        self.name = name
        self.size = size
        self.parent = parent

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return f"FILE(name={self.name}, size={self.size}, parent={self.parent.name})"


outputs = puzzle.input_data.splitlines()
root = curr_dir = None

for output in outputs:
    if (output[0] == '$'):
        if (output[2] == 'l'):
            continue

        dir = output[5:]
        if (dir == ".."):
            curr_dir = curr_dir.parent
            continue

        curr_dir = Directory.get_dir(dir, curr_dir)
        if (root is None):
            root = curr_dir

    elif (output[0] == 'd'):
        _, name = output.split(' ', 1)
        Directory.get_dir(name, curr_dir)

    else:
        size, name = output.split(' ', 1)
        size = int(size)
        file = File(name, size, curr_dir)
        curr_dir.set_size(size)
        if (file not in curr_dir.children):
            curr_dir.children[f"_F007_{name}"] = file


dirs = []
free_space = 70000000 - root.size
required_space = 30000000 - free_space

def find(dir, dirs):
    if (dir.size >= required_space):
        dirs.append(dir.size)

    for child in dir.children.values():
        if (isinstance(child, Directory)):
            find(child, dirs)

find(root, dirs)
puzzle.answer_b = min(dirs)