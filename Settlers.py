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


class people:
    def __init__(self, name, hander, score):
        self.name = name
        self.hander = hander
        self.score = score


resources = ["wheat", "wheat", "wheat", "wheat", "sheep", "sheep", "sheep", "sheep", "woods", "woods", "woods", "woods",
             "brick", "brick", "brick", "brick", "metal", "metal", "metal", "metal", ]
numbers = [2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12]
hexes = []
settle = ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*",
          "*", "*", "*", "*", "*", "*", "*", "*"]
road = ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-",
        "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-",
        "-", "-", "-", "-", "-"]
hand1 = []
hand2 = []
hand3 = []
hands = [hand1, hand2, hand3]
# Create squares and board
for i in range(0, len(numbers)):
    num = random.choice(numbers)
    res = random.choice(resources)
    resources.remove(res)
    numbers.remove(num)
    hexes.append(square(num, res, False))


def trade(trader, tradee, stuff_give, stuff_take):
    trader.hander.remove(stuff_give)
    tradee.hander.append(stuff_give)
    trader.hander.append(stuff_take)
    tradee.hander.remove(stuff_take)


def build(building, player, location):
    if building == "c":
        player.hander.remove("wheat")
        player.hander.remove("wheat")
        player.hander.remove("metal")
        player.hander.remove("metal")
        player.hander.remove("metal")
        player.score = player.score + 2
        xc = int(location[0])
        yc = int(location[1])
        settle[((yc * 5) - (5 - xc)) - 1] = player.name.upper()
    elif building == "s":
        player.hander.remove("wheat")
        player.hander.remove("woods")
        player.hander.remove("brick")
        player.hander.remove("sheep")
        player.score = player.score + 1
        xc = int(location[0])
        yc = int(location[1])
        settle[((yc * 5) - (5 - xc)) - 1] = player.name.lower()
    elif building == "r":
        player.hander.remove("brick")
        player.hander.remove("woods")
        xc = int(location[0])
        yc = int(location[1:])
        if yc % 2 == 0:
            rodes = (yc // 2 * 9) - (5 - xc) - 1
        elif y % 2 != 0:
            rodes = (yc // 2 * 9) + xc - 1
        road[rodes] = roads[i]


def roll():
    rolls = str(random.randint(2, 12))
    while rolls == "7":
        rolls = str(random.randint(2, 12))
    return rolls


def hand(number):
    if int(number) < 10:
        number = " " + str(number)
    for item in range(0, len(hexes)):
        if hexes[item].numb == number:
            if item % 4 == 0 and item != 0:
                index = item + (item // 4 - 1)
            else:
                index = item + (item // 4)
            for p in range(0, len(players)):
                if settle[index].lower() == players[p].name or settle[index + 1].lower() == players[p].name or settle[index + 5].lower() == players[p].name or settle[index + 6].lower() == players[p].name:
                    players[p].hander.append(hexes[item].resource)
                if settle[index].upper() == players[p].name or settle[index + 1].upper() == players[p].name or settle[index + 5].upper() == players[p].name or settle[index + 6].upper() == players[p].name:
                    players[p].hander.append(hexes[item].resource)
                    players[p].hander.append(hexes[item].resource)

    for i in players:
        print(i.name + ": ", end="")
        print(i.hander)


def board():
    print("1            2            3            4            5")
    print()
    for p in range(0, 5):
        if p == 4:
            print(settle[p], end="    ")
            print("1      1")
            print(road[p], end=" ")
            break
        print(settle[p], "    ", road[p],
              end="     ")  # variables are correct up to here for roads. Must correct from here on. Settlements are done
    c = 0
    for item in hexes:
        if c % 4 == 0 and c != 0:
            print("         ", c // 2)
            for i in range(0, 5):
                if i == 4:
                    print(settle[((c // 4) * 5) + i], end="    ")
                    print(c // 4 + 1, "    ", (c // 4 + 1) * 2 - 1)
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
firstP = input(
    "Input lowercase character for player one. The lowercase will represent a settlement, the uppercase a city:")
secondP = input(
    "Input lowercase character for player two. The lowercase will represent a settlement, the uppercase a city:")
thirdP = input(
    "Input lowercase character for player three. The lowercase will represent a settlement, the uppercase a city:")
firstR = input("Input lowercase character for player one. The lowercase will represent a road:")
secondR = input("Input lowercase character for player two. The lowercase will represent a road:")
thirdR = input("Input lowercase character for player three. The lowercase will represent a road:")
players = [firstP.lower(), secondP.lower(), thirdP.lower()]
roads = [firstR, secondR, thirdR]
for j in range(0, 2):
    for i in range(0, 3):
        settles = input("Location of " + players[i] + "\'s " + str(j + 1) + " settlement(xy):")
        x = int(settles[0])
        y = int(settles[1])
        settle[((y * 5) - (5 - x)) - 1] = players[i]
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

# Logic for starting cards
for h in hands:
    h.append("wheat")
    h.append("woods")
    h.append("brick")


vic1 = 0
vic2 = 0
vic3 = 0
victory_points = [vic1, vic2, vic3]
firstP = people(firstP, hand1, vic1)
secondP = people(secondP, hand2, vic2)
thirdP = people(thirdP, hand3, vic3)
players = [firstP, secondP, thirdP]
print(players[0].name)
hand(0)
#  Main game loop
print("Now let's get started!")
print("Turn order will go " + players[0].name + ", " + players[1].name + ", " + players[2].name)
while True:
    for i in range(0, 3):
        board()
        print(players[i].name + " \'s turn. They rolled a " + roll())
        hand(roll())
        turn = "You chumpy idiot!"
        while turn != "q":
            turn = input("Would you like to trade(t), build(b), or end your turn(q)?")
            if turn == "t":  # I finished the trade function! This swaps cards stored in people's hands.
                perpole = input("Please enter the pre-stored character representing the person you'd like to trade with (assuming you have their permission):")
                for j in range(0, 3):
                    if players[j].name == perpole:
                        life = j
                resource_given = input("What resource would you like to give them?")
                resource_taken = input("What resource are you taking?")
                trade(players[i], players[life], resource_given, resource_taken)
                hand(0)
            elif turn == "b":
                type = input("Would you like to build a city(c), settlement(s), or a road(r).")
                location = input("Please enter the coordinates you would like to place it:")
                build(type, players[i], location)
            elif turn == "q":  #  Makes it the next players turn
                break
        for score in range(0, len(victory_points)):
            if players[score].score >= 10:
                print("Game is over! " + players[score].name + " won! They got ten victory points!")
                break
