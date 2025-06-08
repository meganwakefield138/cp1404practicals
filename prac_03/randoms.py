"""
CP1404 - Practical

This file contains questions and answers for randoms.
"""
import random

print(random.randint(5, 20))
# What did you see on line 1?
# What was the smallest number you could have seen, what was the largest?

# The largest number I saw was 20 and the smallest was 5.

print(random.randrange(3, 10, 2))
# What did you see on line 2?
# What was the smallest number you could have seen, what was the largest?
# Could line 2 have produced a 4?

# The largest number I saw was 9 and the smallest was 3.
# Line 2 could have not produced a 4 because the number increased by 2 steps starting from 3.
# Thus, the only values line 2 can produce are 3, 5, 7, 9.

print(random.uniform(2.5, 5.5))
# What did you see on line 3?
# What was the smallest number you could have seen, what was the largest?

# I saw random decimal numbers between 2.5 and 5.5.
# The smallest number I could have seen was 2.5, and the largest was 5.5, however, it is rare to see the lower and upper limits due to how floating point numbers work.

# Write a code to produce a random integer between 1 and 100 inclusive.
print(random.randint(1, 100))