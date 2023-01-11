import random
import time


def blank():
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()


WAIT = 0


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
settle = ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*",
          "*", "*", "*", "*", "*", "*", "*", "*"]
road = ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-",
        "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"]
# Create squares and board
for i in range(0, len(numbers)):
    num = random.choice(numbers)
    res = random.choice(resources)
    resources.remove(res)
    numbers.remove(num)
    hexes.append(square(num, res, False))


def board():
    print("1            2            3            4            5")
    print()
    for p in range(0, 5):
        if p == 4:
            print(settle[p], end="    ")
            print("1      1")
            print(road[p], end=" ")
            break
        print(settle[p], "    ", road[p], end="     ") # variables are correct up to here for roads. Must correct from here on. Settlements are done
    c = 0
    for item in hexes:
        if c % 4 == 0 and c != 0:
            print("         ", c//2)
            for i in range(0, 5):
                if i == 4:
                    print(settle[((c // 4) * 5) + i], end="    ")
                    print(c // 4 + 1, "    ", (c//4 + 1) * 2 - 1)
                    print(road[((c // 4) * 5) + i + (4 * (c // 4))], "", end="")
                    break
                print(settle[((c // 4) * 5) + i], "    ", road[((c // 4) * 5) + i + (4 * (c // 4))], end="     ")
        print(item.numb, item.resource, item.settle, " ", end=road[c + 5 + (c // 4 * 5)] + " ")
        c += 1
    print("         ", 10)
    for i in range(0, 5):
        if i == 4:
            print(settle[i + 25], "   6      11")
            break
        print(settle[i + 25], "    ", road[i + 45], end="     ")


print("         |-------------------------------------|")  # Welcome Script
print("         |----Welcome to Settlers of Catan!----|")
print("         |-------------------------------------|")
print()
print()
time.sleep(WAIT)
print("The inside coordinates are for the settlements, outside coordinates are for roads.")
print()
print()
board()
print("Now it's time to place:")
firstP = input("Input lowercase character for player one. The lowercase will represent a settlement, the uppercase a city:")
secondP = input("Input lowercase character for player two. The lowercase will represent a settlement, the uppercase a city:")
thirdP = input("Input lowercase character for player three. The lowercase will represent a settlement, the uppercase a city:")
firstR = input("Input lowercase character for player one. The lowercase will represent a road:")
secondR = input("Input lowercase character for player two. The lowercase will represent a road:")
thirdR = input("Input lowercase character for player three. The lowercase will represent a road:")
players = [firstP, secondP, thirdP]
roads = [firstR, secondR, thirdR]
for j in range(0, 2):
    for i in range(0, 3):
        settles = input("Location of " + players[i] + "\'s " + str(j + 1) + " settlement(xy):")
        x = int(settles[0])
        y = int(settles[1])
        settle[((y*5) - (5 - x)) - 1] = players[i]
        board()
        rode = input("Location of " + players[i] + "\'s" + str(j + 1) + " road(xy)")
        x = int(rode[0])
        y = int(rode[1:])
        if y % 2 == 0:
            rode = (y // 2 * 9) - (5 - x) - 1
        elif y % 2 != 0:
            rode = (y // 2 * 9) + x - 1
        road[rode] = roads[i]
        board()


#  Main game loop
while True:
    print("Now let's get started!")
    print("Turn order will go " + players[0] + players[1] + players[2])
    break
