import random

resources = ["wheat", "wheat", "wheat", "wheat", "sheep", "sheep", "sheep", "sheep", "woods", "woods", "woods", "woods",
             "brick", "brick", "brick", "brick", "metal", "metal", "metal", "metal", ]
numbers = [2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12]
hexes = []
settle = ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*",
          "*", "*", "*", "*", "*", "*", "*", "*", ]
road = ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-",
        "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", ]
for i in range(0, 20):
    res = random.choice(resources)
    num = random.choice(numbers)
    resources.remove(res)
    numbers.remove(num)
    if num < 10:
        num = " " + str(num)
    square = str(num) + " " + res
    hexes.append(square)


def board():
    for i in range(0, 5):
        if i == 4:
            print(settle[i])
            print(road[5], end=" ")
            break
        print(settle[i], "    ", road[i], end="    ") # variables are correct up to here. Must correct from here on
    for c in range(0, 20):
        if c % 4 == 0 and c != 0:
            print()
            for i in range(0, 5):
                if i == 4:
                    print(settle[c])
                    print(road[c], "", end="")
                    break
                print(settle[5 + c], "    ", road[5 + c], end="    ")
        print(hexes[c], " ", end=road[c] + " ")
    print()
    for i in range(0, 5):
        if i == 4:
            print(settle[i])
            break
        print(settle[i], "    ", road[i], end="    ")


board()
#  Road text once built ━, maybe not, actually. Maybe they input what they want their road to look like
