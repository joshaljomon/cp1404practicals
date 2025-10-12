import random

SMALLEST_NUMBER = 1
LARGEST_NUMBER = 45

number_of_picks = int(input("How many quick picks? "))

for i in range(number_of_picks):
    quick_pick = []

    while len(quick_pick) < 6:
        number = random.randint(SMALLEST_NUMBER, LARGEST_NUMBER)
        if number not in quick_pick:
            quick_pick.append(number)

    quick_pick.sort()

    for number in quick_pick:
        print(f"{number:2}", end= ' ')
    print()