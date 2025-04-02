def main():
    num: int = 7
    num = subtract_seven(num)
    print("this should be zero: ", num)

def subtract_seven(num):
    num = num - 7
    return num

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main() 