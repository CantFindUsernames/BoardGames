import random

resources = ["wheat", "wheat", "wheat", "wheat", "sheep", "sheep", "sheep", "sheep", "woods", "woods", "woods", "woods",
             "brick", "brick", "brick", "brick", "metal", "metal", "metal", "metal", ]
numbers = [2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12]
hexes = []
settle = ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*",
          "*", "*", "*", "*", "*", "*", "*", "*", ]
road = ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-",
        "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"]

for i in range(0, 20):
    res = random.choice(resources)
    num = random.choice(numbers)
    resources.remove(res)
    numbers.remove(num)
    if num < 10:
        num = " " + str(num)
    square = str(num) + " " + res
    hexes.append(square)


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


def board():
    print("1           2           3           4           5")
    for i in range(0, 5):
        if i == 4:
            print(settle[i] + "   1")
            print(road[i], end=" ")
            break
        print(settle[i], "    ", road[i], end="    ")  # variables are correct up to here. Must correct from here on
    for c in range(0, 20):
        if c % 4 == 0 and c != 0:
            a = c // 4
            print()
            for i in range(0, 5):
                if i == 4:
                    print(settle[(5 * a) + i], " ", 1 + (c // 4))
                    print(road[(5 * a) + i], "", end="")
                    break
                print(settle[(5 * a) + i], "    ", road[(5 * a) + i], end="    ")
        print(hexes[c], " ", end=road[c + 5] + " ")
    print()
    for i in range(0, 5):
        if i == 4:
            print(settle[i + 25], "  6")
            break
        print(settle[i + 25], "    ", road[i], end="    ")


# Now the game can start
print("Welcome to Settlers of Catan!")
board()
P1 = input("Player one, please input you first initial. It will be used to mark settlements, uppercase will be city:")
P1r = input("Player one, please input a symbol you would like to use for roads, it cannot be \'-\':")
P2 = input("Player two, please input you first initial. It will be used to mark settlements, uppercase will be city:")
P2r = input("Player two, please input a symbol you would like to use for roads, it cannot be \'-\':")
P3 = input("Player three, please input you first initial. It will be used to mark settlements, uppercase will be city:")
P3r = input("Player three, please input a symbol you would like to use for roads, it cannot be \'-\':")
users = [P1, P2, P3]
roads = [P1r, P2r, P3r]
x = 0
for i in users:
    blank()
    set = input(str(i) + " Where would you like to put your first settlement? (xy)")
    x = int(set[0])
    y = (int(set[1])) * 5
    set = (y - (5 - x)) - 1
    settle[set] = i.lower()
    board()
    rode = input(str(i) + " Where would you like to put your first road? Please note for roads the value of each coordinate doubles and rounds down to the nearest odd number and the corresponding coordinate is added inbetween.(xy)")
    x = int(rode[0])
    y = (int(rode[1])) * 5
    rode = (y - (5 - x)) - 1
    road[rode] = roads[x].lower()
    board()
    x += 1
    print(road)
