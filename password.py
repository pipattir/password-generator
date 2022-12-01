import random
import string
print("Welcome to the password generator.")


def generator():
    print("0) Exit")
    print("1) Password with letters")
    print("2) Password with digits")
    print("3) Password with letters & digits")
    print("4) Password with letters, digits & special characters")
    choice = int(input("Select password type:\n"))
    # checking if user wants to exit
    if choice == 0:
        exit()
    # generating passwords until user wants to exit
    else:
        length = int(input("Input password length:\n"))
        # password with letters
        if choice == 1:
            result_str = ''.join(random.choice(string.ascii_letters) for i in range(length))
            print(result_str)
            generator()
        # Password with digits
        elif choice == 2:
            result_str = ''.join(random.choice(string.digits) for i in range(length))
            print(result_str)
            generator()
        # Password with letters & digits
        elif choice == 3:
            characters = string.ascii_letters + string.digits
            password = ''.join(random.choice(characters) for i in range(length))
            print(password)
            generator()
        # Password with letters, digits & special characters
        elif choice == 4:
            characters = string.ascii_letters + string.digits + string.punctuation
            password = ''.join(random.choice(characters) for i in range(length))
            print(password)
            generator()


generator()
