import random
import string

def main():
    #using string module to make a list of all characters
    characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")
    random.shuffle(characters)

    pass_length = int(input("what length password would you like: "))
    password = ""
    for i in range (pass_length):
        password += random.choice(characters)
    print(password)

if __name__ == "__main__":
    main()