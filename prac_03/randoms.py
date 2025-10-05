"""
What did you see on line 1?
A random number between 5 and 20 inclusive. The numbers I received were 13, 20, 20, 14.
The smallest possible number I could have seen would be 5, the largest being 20.

What did you see on line 2?
A random number from the range 3-10, but the numbers were always 2 numbers apart from one another. The numbers I received were 5, 5, 7, 9.
The smallest possible number I could have seen is 5, the largest being 9.

What did you see on line 3?
A random number that included decimals, which meant the 'small' range from 2.5-5.5 is a very large number. The numbers received were too long to put here.
The smallest possible number I could have seen is 2.5, the largest being 5.5.
"""
import random

number = random.randint(1, 100)
print(number)