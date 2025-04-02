import random

def get_user_feedback():
    """Get feedback from the user about the computer's guess."""
    while True:
        feedback = input("Is my guess correct? (yes/higher/lower): ").lower()
        if feedback in ['yes', 'higher', 'lower']:
            return feedback
        print("Please enter 'yes', 'higher', or 'lower'.")

def main():
    print("Welcome to Guess the Number!")
    print("Think of a number between 1 and 100, and I'll try to guess it.")
    input("Press Enter when you're ready...")
    
    min_num = 1
    max_num = 100
    attempts = 0
    
    while True:
        attempts += 1
        
        # Computer makes a guess
        guess = random.randint(min_num, max_num)
        print(f"\nAttempt {attempts}: I guess {guess}")
        
        # Get feedback from user
        feedback = get_user_feedback()
        
        if feedback == 'yes':
            print(f"\nGreat! I guessed your number in {attempts} attempts!")
            break
        elif feedback == 'higher':
            min_num = guess + 1
            print("I'll guess higher next time.")
        else:  # lower
            max_num = guess - 1
            print("I'll guess lower next time.")
        
        # Check if the range is invalid
        if min_num > max_num:
            print("\nHey! You must have changed your number! That's not fair!")
            break

if __name__ == "__main__":
    main() 