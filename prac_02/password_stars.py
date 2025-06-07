"""
CP1404 Practical

This program asks the user for a password and displays it with asterisks.
"""
"Define the minimum password length"
MIN_LENGTH = 8

def main():
    password = input("Enter password (min. 8 characters): ")
    while len(password) < MIN_LENGTH:
        password = input("Password must be at least 8 characters. Enter password again: ")
    print("*" * len(password))

main()