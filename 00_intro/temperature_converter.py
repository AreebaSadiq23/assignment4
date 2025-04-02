def main():
    print("Enter temperature in Fahrenheit: ", end="")
    try:
        fahrenheit = float(input())
    except ValueError:
        print("Error: Please enter a valid number")
        return

    celsius = (fahrenheit - 32) * 5.0/9.0

    print(f"Temperature: {fahrenheit}F = {celsius}C")

if __name__ == '__main__':
    main() 