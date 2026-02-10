import random
import string


def get_length():
    while True:
        try:
            length = int(input("Enter desired password length: "))
            if length < 4:
                print("Password length should be at least 4 characters.")
            else:
                return length
        except ValueError:
            print("Please enter a valid number.")


def get_complexity():
    print("\nSelect password complexity:")
    print("1. Letters only")
    print("2. Letters and numbers")
    print("3. Letters, numbers, and symbols")

    choice = input("Enter choice (1/2/3): ").strip()
    return choice


def generate_password(length, complexity):
    letters = string.ascii_letters
    numbers = string.digits
    symbols = string.punctuation

    if complexity == "1":
        characters = letters
    elif complexity == "2":
        characters = letters + numbers
    else:
        characters = letters + numbers + symbols

    password = ""
    for _ in range(length):
        password += random.choice(characters)

    return password


def main():
    print("=== Password Generator ===")

    length = get_length()
    complexity = get_complexity()

    password = generate_password(length, complexity)

    print("\nGenerated Password:")
    print(password)


if __name__ == "__main__":
    main()
