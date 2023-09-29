"""CP1404 Prac 02"""

minimum_length = 8
password = input(f"Password (minimum {minimum_length} characters): ")
while len(password) < minimum_length:
    print(f"Invalid password, minimum length is {minimum_length} characters")
    password = input(f"Password (minimum {minimum_length} characters): ")
print('*' * len(password))
