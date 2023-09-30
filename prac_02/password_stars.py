"""CP1404 Prac 02"""


def main():
    """Password check"""
    minimum_length = 8
    password = get_password(minimum_length)
    print_password_as_asterisks(password)


def print_password_as_asterisks(password):
    print('*' * len(password))


def get_password(minimum_length):
    password = input(f"Password (minimum {minimum_length} characters): ")
    while len(password) < minimum_length:
        print(f"Invalid password, minimum length is {minimum_length} characters")
        password = input(f"Password (minimum {minimum_length} characters): ")
    return password


main()
