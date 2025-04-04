import random

def get_user_choice():
    while True:
        choice = input("Enter your choice (rock/paper/scissors): ").lower()
        if choice in ['rock', 'paper', 'scissors']:
            return choice
        print("Invalid choice! Please try again.")

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    
    winning_combinations = {
        'rock': 'scissors',
        'paper': 'rock',
        'scissors': 'paper'
    }
    
    if winning_combinations[user_choice] == computer_choice:
        return "You win!"
    return "Computer wins!"

def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    print("--------------------------------")
    
    score = {'user': 0, 'computer': 0}
    
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        
        result = determine_winner(user_choice, computer_choice)
        print(result)
        
        if result == "You win!":
            score['user'] += 1
        elif result == "Computer wins!":
            score['computer'] += 1
            
        print(f"\nScore - You: {score['user']}, Computer: {score['computer']}")
        
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break
    
    print("\nFinal Score:")
    print(f"You: {score['user']}")
    print(f"Computer: {score['computer']}")
    print("\nThanks for playing!")

if __name__ == "__main__":
    play_game() 