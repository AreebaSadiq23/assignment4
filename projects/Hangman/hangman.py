import random

# List of words for the game
WORDS = [
    'python', 'programming', 'computer', 'algorithm', 'database',
    'network', 'software', 'developer', 'coding', 'interface',
    'variable', 'function', 'class', 'object', 'string'
]

def get_random_word():
    return random.choice(WORDS).lower()

def display_hangman(tries):
    stages = [
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     /
           -
        """,
        """
           --------
           |      |
           |     \\|/
           |      |
           |      |
           |
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|
           |      |
           |
           -
        """,
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |
           -
        """,
        """
           --------
           |      |
           |      O
           |
           |
           |
           -
        """,
        """
           --------
           |      |
           |      
           |
           |
           |
           -
        """
    ]
    return stages[tries]

def play_hangman():
    word = get_random_word()
    word_letters = set(word)  # letters in the word
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    used_letters = set()  # letters guessed by the user

    lives = 6

    # Getting user input
    while len(word_letters) > 0 and lives > 0:
        print("\nYou have", lives, "lives left and you've used these letters:", ' '.join(used_letters))

        # Display current word
        word_list = [letter if letter in used_letters else '_' for letter in word]
        print(display_hangman(lives))
        print("Current word:", ' '.join(word_list))

        # Get user input
        guess = input("Guess a letter: ").lower()
        if guess in alphabet - used_letters:
            used_letters.add(guess)
            if guess in word_letters:
                word_letters.remove(guess)
                print("Good guess!")
            else:
                lives = lives - 1
                print("Wrong guess!")
        elif guess in used_letters:
            print("You already used that letter. Try again!")
        else:
            print("Invalid character. Please enter a letter!")

    # Game over
    if lives == 0:
        print(display_hangman(lives))
        print("Sorry, you died! The word was", word)
    else:
        print("Congratulations! You guessed the word", word, "!!")

def main():
    print("Welcome to Hangman!")
    while True:
        play_hangman()
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break
    print("Thanks for playing!")

if __name__ == "__main__":
    main() 