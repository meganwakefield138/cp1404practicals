"""
CP1404/CP5632 - Practical

Capitalist Conrad wants a stock price simulator for a volatile stock.
The price starts off at $10.00, and, at the end of every day there is
a 50% chance it increases by 0 to 10%, and
a 50% chance that it decreases by 0 to 5%.
If the price rises above $1000, or falls below $0.01, the program should end.
The price should be displayed to the nearest cent (e.g. $33.59, not $33.5918232901)
"""

import random

# Constants
MAX_INCREASE = 0.175  # 17.5%
MAX_DECREASE = 0.05  # 5%
MIN_PRICE = 1.0
MAX_PRICE = 100.0
INITIAL_PRICE = 10.0
FILENAME = "output.txt"

price = INITIAL_PRICE
number_of_days = 0

out_file = open(FILENAME, "w")

while MIN_PRICE <= price <= MAX_PRICE:
    price_change = 0
    number_of_days += 1
    # generate a random integer of 1 or 2
    if random.randint(1, 2) == 1:
        price_change = random.uniform(0, MAX_INCREASE)
        print(f"Day {number_of_days}: price increases by {price_change}%", file=out_file)
    else:
        price_change = random.uniform(-MAX_DECREASE, 0)
        print(f"Day {number_of_days}: price decreases by {price_change}%", file=out_file)

    price *= (1 + price_change)
    print(f"On day {number_of_days} price is ${price:,.2f}", file=out_file)

out_file.close()