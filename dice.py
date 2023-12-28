import random

def roll_die(bet, amount):
    dice_art = {
        1: ("┌─────────┐",
            "│         │",
            "│    ●    │",
            "│         │",
            "└─────────┘"),
        2: ("┌─────────┐",
            "│  ●      │",
            "│         │",
            "│      ●  │",
            "└─────────┘"),
        3: ("┌─────────┐",
            "│  ●      │",
            "│    ●    │",
            "│      ●  │",
            "└─────────┘"),
        4: ("┌─────────┐",
            "│  ●   ●  │",
            "│         │",
            "│  ●   ●  │",
            "└─────────┘"),
        5: ("┌─────────┐",
            "│  ●   ●  │",
            "│    ●    │",
            "│  ●   ●  │",
            "└─────────┘"),
        6: ("┌─────────┐",
            "│  ●   ●  │",
            "│  ●   ●  │",
            "│  ●   ●  │",
            "└─────────┘")
    }

    x = random.randint(1,6)
    y = random.randint(1,6)

    print("you rolled:", x ,"and",y)

    for i in range(5):
        print(dice_art[x][i], "\t", dice_art[y][i])

    if(x+y>7):
        print("which is 7 up")
    elif(x+y<7):
        print("which is 7 down")
    else: 
        print("which is exactly 7")
    if((bet.lower() == "down" and x+y<7) or (bet.lower() == "up" and x+y>7)):
        amount = amount*2 
    elif(bet.lower() == "equal" and x+y == 7):
        amount = amount*5
    else:
        amount = 0
    return amount

def main():
    gain = 0
    while(True):
        bet = input("Place bet (Up/Down/Equal): ")
        amount = int(input("Bet amount: "))
        gain -= amount
        amount = roll_die(bet, amount)
        gain += amount
        if(gain >= 0):
            print("you have gained", gain)
        else:
            print("you have lost", -1*gain)
        roll_again = input("Roll again? (Yes/No): ")
        if(roll_again.lower() == "no"):
            break

if __name__ == "__main__":
    main()