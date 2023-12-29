import random
from words import words
import string

GUESSES = 7

def is_valid_word(word):
    if ' ' not in word and '-' not in word and 3<=len(word)<=6:
        return True
    else:
        return False
    
def choose_word():
    word = random.choice(words)
    while not is_valid_word(word):
        word = random.choice(word)
    return word.upper()

def hangman(word):
    letters_guessed = set() 

    j = 0
    correct = 0
    while  GUESSES - j + correct > 0:
        word_guessed = True
        print("you have", GUESSES - j + correct, "guesses")
        for i in word:
            if i in letters_guessed:
                print(i, end=" ")
            else:
                print("-", end=" ")
                word_guessed = False
        if j>0:
            print("\tletters guesses so far:", letters_guessed)
        else:
            print()

        if word_guessed:
            break

        while True:
            letter = input("Guess a letter: ").upper()
            if len(letter) !=1 and letter not in list(string.ascii_letters):
                print("invalid input")
            elif letter in letters_guessed:
                print("letter already guessed")
            else:
                break
        if letter in word:
            correct += 1
        print()
        letters_guessed.add(letter)
        j+=1
             
    return word_guessed

def main():
    word = choose_word()
    won = hangman(word)
    if won == True:
        print("Congratulations you have won")
    else:
        print("You lost. The word was", word)

if __name__ == "__main__":
    main()