def main():
    MENU = """    G - Get a valid score
    P - Print results
    S - Show stars
    Q - Quit"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = int(input("Enter score: "))
            get_valid_score(score)
        elif choice == "P":
            print(determine_status(score))
        elif choice == "S":
            print(print_stars(score))
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def get_valid_score(score):
    while score < 0 or score > 100:
        print("Invalid score")
        score = int(input("Enter score: "))
    return score

def determine_status(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def print_stars(score):
    return '*' * score


main()