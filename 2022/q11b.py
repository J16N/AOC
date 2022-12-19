import re, operator
from collections import deque
from aocd.models import Puzzle
puzzle = Puzzle(year=2022, day=11)

operations = {
    '+': operator.add, '-': operator.sub, 
    '*': operator.mul, '/': operator.floordiv
}

class Monkey:
    def __init__(self, name, items, op, opv, test, success, failure):
        self.name = name
        self.items = items
        self.op = op
        self.op_value = opv
        self.test = test
        self.success = success
        self.failure = failure
        self.inspect = 0

monkeys = []
worry_levels = 1
monkeys_data = puzzle.input_data.split("\n\n")

for monkey in monkeys_data:
    monkey_data = monkey.splitlines()
    name = int(re.search(r"\d+", monkey_data[0]).group(0))
    items = deque(map(int, re.findall(r"\d+", monkey_data[1])))
    op = re.search(r"(\+|\*|\/|\-)", monkey_data[2]).group(0)
    opv = re.search(r"(\d+)", monkey_data[2])
    if (opv): opv = int(opv.group(0))
    test = int(re.search(r"\d+", monkey_data[3]).group(0))
    success = int(re.search(r"\d+", monkey_data[4]).group(0))
    failure = int(re.search(r"\d+", monkey_data[5]).group(0))
    monkeys.append(Monkey(name, items, op, opv, test, success, failure))
    worry_levels = worry_levels * test


for round in range(10000):
    for monkey in monkeys:
        while monkey.items:
            item = monkey.items.popleft()
            monkey.inspect += 1
            opv = item if (not monkey.op_value) else monkey.op_value
            new_item = operations[monkey.op](item, opv)
            new_item = new_item % worry_levels
            
            if (new_item % monkey.test == 0):
                monkeys[monkey.success].items.append(new_item)
            else:
                monkeys[monkey.failure].items.append(new_item)


monkeys.sort(reverse=True, key=lambda m: m.inspect)
puzzle.answer_b = monkeys[0].inspect * monkeys[1].inspect