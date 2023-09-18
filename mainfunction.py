from random import randint as randomInteger

def roll_dice():
    dice_total = randomInteger(1,6) + randomInteger(1,6)
    return dice_total

def main():
    number = int(input("How many player?\n"))
    players = [f'Player {n}' for n in range(1, number+1)]

    for player in players:
        print(f"{player} get {roll_dice()} points")

if __name__ == '__main__':
    main()