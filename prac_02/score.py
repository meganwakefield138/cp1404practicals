"""
CP1404 Practical

This program asks the user for a score and displays the result category.
"""
from random import random


def main():
    score = float(input("Enter score: "))
    result = get_score(score)
    print(f"Your result is {result}")

    "Generate a random score"
    import random
    random_score = random.randint(0, 100)
    random_result = get_score(random_score)
    print(f"Random score: {random_score} - {random_result}")

def get_score(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score > 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

main()