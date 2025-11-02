"""
Emails
Estimate: 15 mins
Actual: 18 mins
"""

def main():
    """Create dictionary of emails_to_names"""
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = get_name_from_email(email)
        confirmation = input(f"Is your name {name}? (Y/n) ")
        if confirmation.upper() !="Y" and confirmation != "":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")

    for email, name in email_to_name.items():
            print(f"{name} ({email})")


def get_name_from_email(email):
    """Get name from email"""
    username = email.split('@')[0]
    parts = username.split('.')
    name = " ".join(parts).title()
    return name


main()