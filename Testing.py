import random
class people:
    def __init__(self, name, hander, score):
        self.name = name
        self.hander = hander
        self.score = score


players = [people("Hi", [], 0), people("Bob", [], 0), people("Fred", [], 0)]
class square:
    def __init__(self, numb, resource, settle):
        self.numb = numb
        if self.numb < 10:
            self.numb = " " + str(numb)
        self.resource = resource
        self.settle = settle
        if not self.settle:
            self.settle = ''

resources = ["wheat", "wheat", "wheat", "wheat", "sheep", "sheep", "sheep", "sheep", "woods", "woods", "woods", "woods",
             "brick", "brick", "brick", "brick", "metal", "metal", "metal", "metal", ]
numbers = [2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12]
hexes = []
settle = ["*", "*", "Bob", "Fred", "Hi", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*",
          "*", "*", "*", "*", "*", "*", "*", "*"]
road = ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-",
        "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-",
        "-", "-", "-", "-", "-"]

# Create squares and board
for i in range(0, len(numbers)):
    num = random.choice(numbers)
    res = random.choice(resources)
    resources.remove(res)
    numbers.remove(num)
    hexes.append(square(num, res, False))


players[0].hander.append(hexes[4].resource)
print(players[0].hander)