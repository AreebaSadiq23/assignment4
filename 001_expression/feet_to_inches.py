INCHES_IN_FOOT = 12  

def main():
    feet = float(input("Enter number of feet: "))
    
    # Convert feet to inches
    inches = feet * INCHES_IN_FOOT
    
    # Print the result
    print("That is", inches, "inches!")

if __name__ == '__main__':
    main() 