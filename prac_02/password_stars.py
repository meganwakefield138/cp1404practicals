"""
CP1404 Practical

This program asks the user for a password and displays it with asterisks.
"""
"Define the minimum password length"
MIN_LENGTH = 8

def main():
   password = get_password()
   print_stars(password)

def get_password():
    password = input(f"Enter password (min. 8 characters): ")
    while len(password) < MIN_LENGTH:
        print("Password must be at least 8 characters.")
        password = input("Enter password again: ")
    return password

def print_stars(password):
    print("*" * len(password))

main()