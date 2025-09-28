PASSWORD_LENGTH = 10


def main():
    password = get_password()
    print_stars(password)


def print_stars(password: str):
    print('*' * len(password))


def get_password() -> str:
    password = input("Enter a password: ")
    while len(password) < PASSWORD_LENGTH:
        password = input("Enter a password: ")
    return password


main()