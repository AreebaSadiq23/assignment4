def add_many_numbers(numbers):
    """
    Takes in a list of numbers and returns the sum of those numbers.
    """
    total_so_far = 0
    for number in numbers:
        total_so_far += number

    return total_so_far

def main():
    numbers = [1, 2, 3, 4, 5]  # Make a list of numbers
    sum_of_numbers = add_many_numbers(numbers)  # Find the sum of the list
    print(sum_of_numbers)  # Print out the sum above

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main() 