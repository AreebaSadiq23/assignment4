import random

def get_guess():
    """Get a valid guess from the user."""
    while True:
        try:
            guess = int(input("Enter your guess (1-100): "))
            if 1 <= guess <= 100:
                return guess
            print("Please enter a number between 1 and 100.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10
    
    print("Welcome to Guess the Number!")
    print(f"I'm thinking of a number between 1 and 100. You have {max_attempts} attempts to guess it.")
    
    while attempts < max_attempts:
        attempts += 1
        print(f"\nAttempt {attempts}/{max_attempts}")
        
        # Get the player's guess
        guess = get_guess()
        
        # Check if the guess is correct
        if guess == secret_number:
            print(f"\nCongratulations! You guessed the number in {attempts} attempts!")
            return
        elif guess < secret_number:
            print("Too low! Try a higher number.")
        else:
            print("Too high! Try a lower number.")
    
    # If we get here, the player ran out of attempts
    print(f"\nGame Over! The number was {secret_number}.")

if __name__ == "__main__":
    main() 