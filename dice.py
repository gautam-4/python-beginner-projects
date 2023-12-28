import random

def roll_die():
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

def main():
    while(True):
        roll_die()
        roll_again = input("Roll again? (Yes/No): ")
        if(roll_again.lower == "No".lower):
            break

if __name__ == "__main__":
    main()