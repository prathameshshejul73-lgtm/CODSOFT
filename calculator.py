def get_number(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Please enter a valid number.")


def get_operation():
    print("\nChoose operation:")
    print(" +  Addition")
    print(" -  Subtraction")
    print(" *  Multiplication")
    print(" /  Division")

    op = input("Enter operation symbol: ").strip()
    if op in ["+", "-", "*", "/"]:
        return op
    else:
        print("Invalid operation selected.")
        return None


def calculate(num1, num2, op):
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "*":
        return num1 * num2
    elif op == "/":
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2


def main():
    print("=== Simple Calculator ===")

    while True:
        first = get_number("Enter first number: ")
        second = get_number("Enter second number: ")
        operation = get_operation()

        if operation:
            result = calculate(first, second, operation)
            print(f"\nResult: {result}")

        again = input("\nDo you want to calculate again? (y/n): ").lower()
        if again != "y":
            print("Calculator closed. Bye 👋")
            break


if __name__ == "__main__":
    main()
