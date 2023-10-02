"""
CP1404 - Prac 3
Use random functions
"""

# In python console:
dir(str)
import random
dir(random)
help(random.randint)
help(random.randrange)
import random
print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3
help(random.uniform)

# Q1: What did you see on line 1? What was the smallest number you could have seen, what was the largest?

# Q2: What did you see on line 2? What was the smallest number you could have seen, what was the largest? Could line 2
# have produced a 4?

# Q3: What did you see on line 3? What was the smallest number you could have seen, what was the largest?

# Q4: Write code, not a comment, to produce a random number between 1 and 100 inclusive.


# ANSWERS
# Q1: Use the method randint from the module: random. So generate (and display) a random integer from 5 to 20,
# including these end points. Smallest number = 5, largest number = 20.

# Q2. Use the method randrange from the module: random. Select and display a random integer from the range 3 to 10
# where the possible numbers start with the lowest value (3) and go up increments of two until the upper bound of the
# range is reached. I.e. possible numbers: [3, 5, 7, 9] so it is not possible for line 2 to have produced 4, smallest
# number = 3 and largest number = 9.

# Q3. Use the method uniform from the module random. Get and display a random floating point number in the range 2.5 to
# 5.5. Smallest number = 2.5 and largest number = 5.5

# Q4.
print(random.uniform(1, 100))




