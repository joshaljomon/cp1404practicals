"""
CP1404/CP5632 - Practical
Program for temperature conversion
"""

def main():
    MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            change_celsius_to_fahrenheit()
            print(f"Result: {fahrenheit:.2f} F")
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit : "))
            change_fahrenheit_to_celsius()
            print(f"Result: {celsius:.2f} C")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def change_celsius_to_fahrenheit():
    return celsius * 9.0 / 5 + 32


def change_fahrenheit_to_celsius():
    return 5 / 9 * (fahrenheit - 32)


main()
