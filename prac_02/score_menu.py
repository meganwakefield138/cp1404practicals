"""
score_menu.py

This program allows the user to interact with the score menu.
Users can enter a valid score (0-100), display the result category, and exit.
The program demonstrates function reuse and input validation
"""

def main():
    """Displays the score menu"""
    score = "10"
    print("Score Menu")
    choice = input("Enter your choice: ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_score()
        elif choice == "P":
            print(score)
        elif choice == "S":
            print_stars(score)
        else:
            print("Invalid choice. Please try again.")
        print("Score Menu")
        choice = input("Enter your choice: ").upper()
    print("Farewell!")

def get_score():
    score = input("Enter your score (0-100): ")
    while not score.isdigit() or int(score) < 0 or int(score) > 100:
        score = input("Invalid score. Please enter a valid score (0-100): ")
    return int(score)

def print_score(score):
    "Print the score"
    print(score)

def print_stars(score):
    "Print a number of stars equal to the score"
    print("*" * score)

main()