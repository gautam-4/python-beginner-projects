import random

def main():
    user_score = 0
    computer_score = 0
    while(True):
        options = ["rock", "paper", "scissors"]
        computer_pick = options[random.randint(0,2)]
        user_pick = input("rock/paper/scissors: ")
        print("Computer chose:", computer_pick)
        if (user_pick.lower() == "rock" and computer_pick.lower() == "scissors") or (user_pick.lower() == "scissors" and computer_pick.lower() == "paper") or (user_pick.lower() == "paper" and computer_pick.lower() == "rock"):
            print("you win")
            user_score += 1
        elif(user_pick == computer_pick):
            print("draw")
            user_score += 0.5
            computer_score += 0.5
        else:
            print("you lose")
            computer_score += 1
        run = input("another round? (Yes/No): ")
        if(run.lower() == "no"):
            break
    print("Final Score: User", user_score, "|", computer_score, "Computer")

if __name__ == "__main__":
    main()