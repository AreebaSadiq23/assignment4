import random

N_NUMBERS = 10
MIN_VALUE = 1
MAX_VALUE = 100

def main():
    # Generate and print 10 random numbers
    for i in range(N_NUMBERS):
        number = random.randint(MIN_VALUE, MAX_VALUE)
        print(number, end=" ")  # Print with space instead of newline
    print()  # Print newline at the end

if __name__ == '__main__':
    main() 