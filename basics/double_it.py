def main():
    # Get initial number from user
    curr_value = int(input("Enter a number: "))
    
    # Keep doubling until we reach or exceed 100
    while curr_value < 100:
        print(curr_value, end=" ")  # Print current value with a space
        curr_value = curr_value * 2  # Double the current value
    
    print(curr_value)  # Print the final value with a newline

if __name__ == '__main__':
    main() 