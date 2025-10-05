"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
A ValueError will occur when a string or a float is inputted instead of an integer, because the input statement is only taking integers

2. When will a ZeroDivisionError occur?
A ZeroDivisionError will occur when you choose any integer for the numerator, and then choose 0 for the denominator

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
You could add a while statement to check if 0 was inputted for the denominator and ask the user to choose something else

"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Please use a value other than 0 for the denominator")
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")