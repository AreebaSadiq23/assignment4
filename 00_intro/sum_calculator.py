def main():
    # Prompt user for first number
    print("Enter the first number:")
    try:
        num1 = int(input())
    except ValueError:
        print("Error: Please enter a valid integer")
        return

    # Prompt user for second number
    print("Enter the second number:")
    try:
        num2 = int(input())
    except ValueError:
        print("Error: Please enter a valid integer")
        return

    # Calculate sum
    total = num1 + num2

    # Print result
    print(f"The sum of {num1} and {num2} is: {total}")

if __name__ == "__main__":
    main() 