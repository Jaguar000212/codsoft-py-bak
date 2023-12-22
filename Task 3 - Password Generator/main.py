import string
import random
from time import sleep
import os

def clear():
    # Clear the screen
    if os.name == "nt":
        # Windows
        os.system("cls")
    else:
        # Linux
        os.system("clear") 


def generator(length):
    # Create a list of characters to choose from
    characters = string.ascii_letters + string.digits + string.punctuation
    # Create a password variable
    password = ""
    # Loop through the length of the password
    for i in range(length):
        # Add a random character to the password
        password += random.choice(characters)
    # Print the password
    return password

def rerun():
    # Ask the user if they want to generate another password
    rerun = None
    while rerun is None:
        rerun = input("\nDo you want to generate another password? (y/n) ")
        # Check if the input is y or n
        if rerun.lower() != "y" and rerun.lower() != "n":
            print("Please enter y or n")
            rerun = None
    if rerun.lower() == "y":
        # rerun the program
        main()
    else:
        # Exit the program
        print("Thank you for using this program!\nEXITING...")
        sleep(2)
        exit()


def main():
    # Clear the screen
    clear()
    # Print the title
    print("Password Generator".center(50, "-"))
    print("\nWelcome to the Password Generator!")
    print("This program will generate a random password for you.")
    print("The password will contain letters, numbers and symbols.")
    print("You can choose the length of the password.\n")
    # Ask the user for the length of the password
    length = None
    while length is None:
        length = input("How long do you want your password to be? ")
        # Check if the input is a number
        try:
            length = int(length)    
            # Check if the input is greater than 0
            if length < 1:
                print("Please enter a number greater than 0")
                length = None
        except ValueError:
            print("Please enter a number")
            length = None

    # Print the password
    print(f"\nYour generated password is : {generator(length)}")
    # Ask the user if they want to generate another password
    rerun()

# Run the program
try:
    main()
# Check if the user pressed Ctrl+C
except KeyboardInterrupt:
    # Exit the program
    print("\n\nKeyboard Interrupted!\nFORCE QUITTING...")
    print("\nThank you for using this program!")
    sleep(2)
    exit()