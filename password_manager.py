import base64
import os
import getpass
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

PASSWORDS_FILE = "passwords.txt"

def view(f):
    with open(PASSWORDS_FILE, "r") as file:
        for line in file.readlines():
            data = line.rstrip()
            username, token = data.split("|")
            try:
                password = f.decrypt(token.encode()).decode()
                print("Username:", username, "| Password:", password)
            except Exception as e:
                print("Error decrypting password:", e)

def load_key():
    try:
        key_file = open ("key.key", "rb")
    except Exception as e:
        print("New key is required")
        master_pwd = getpass.getpass("Enter the master password: ").encode()
        salt = os.urandom(16)
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=480000,
        )
        key = base64.urlsafe_b64encode(kdf.derive(master_pwd))
        with open("key.key", "wb") as key_file:
            key_file.write(key)
    finally:
        with open ("key.key", "rb") as key_file:
            return key_file.read()


def add(f):
    username = input("Enter username: ")
    password = getpass.getpass("Enter password: ").encode()
    token = f.encrypt(password).decode()
    with open(PASSWORDS_FILE, "a") as file:
        file.write(username + "|" + token + "\n")

def main():
    key = load_key()        
    f = Fernet(key)
    file = open(PASSWORDS_FILE, "a")
    file.close()

    while True:
        operation = input("View/Add/Exit: ").lower()
        if operation == "view":
            view(f)
        elif operation == "add":
            add(f)
        elif operation == "exit":
            break
        else:
            print("Invalid input")

if __name__ == "__main__":
    main()