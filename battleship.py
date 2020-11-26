from random import randint

desk = []

for x in range(0, 6):
    desk.append(["0"] * 6)

def print_desk(desk):
    for row in desk:
        print (" ".join(row))

print("lets play Battleship!")
print_desk(desk)

def random_row(desk):
    return randint(0, len(desk) - 1)

def random_col(desk):
    return randint(0, len(desk[0]) - 1)

ship_row = random_row(desk)
ship_col = random_col(desk)
print ("ship_row")
print ("ship_col")

# Everything erom here on should go in your for loop!
# Be sure to indent five spases!
for turn in range(5):
    print("Turn"), turn + 1
    guess_row = int(input("Guess Row:"))
    guess_col = int(input("Guess Col:"))

    if guess_row == ship_row and guess_col == ship_col:
        print("Congratulations! You sunk my battleship!")
        break
    else:
        if (guess_row < 0 or guess_row > 5) or (guess_col < 0 or ship_col > 5):
            print("Oops, that is not even in the ocean.")
        elif((desk[guess_row][guess_col]) == ("X")):
            print("You guessed that one already.")
        else:
            print("You missed my battleship!")
    if turn == 3:
        print("GAME OVER")

        desk[guess_row][guess_col] = "X"
    # Print (turn + 1) here!
print_desk(desk)