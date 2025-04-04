import time
import os

def clear_screen():
    # Clear screen command for Windows
    os.system('cls' if os.name == 'nt' else 'clear')

def get_time_input():
    while True:
        try:
            hours = int(input("Enter hours (0-23): "))
            minutes = int(input("Enter minutes (0-59): "))
            seconds = int(input("Enter seconds (0-59): "))
            
            if (0 <= hours <= 23 and 
                0 <= minutes <= 59 and 
                0 <= seconds <= 59):
                return hours, minutes, seconds
            else:
                print("Invalid time values! Please try again.")
        except ValueError:
            print("Please enter valid numbers!")

def format_time(hours, minutes, seconds):
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

def countdown(hours, minutes, seconds):
    # Convert everything to seconds
    total_seconds = hours * 3600 + minutes * 60 + seconds
    
    while total_seconds > 0:
        clear_screen()
        
        # Calculate current hours, minutes, seconds
        current_hours = total_seconds // 3600
        current_minutes = (total_seconds % 3600) // 60
        current_seconds = total_seconds % 60
        
        # Display the countdown
        print("\n" + "="*50)
        print("Countdown Timer")
        print("="*50)
        print(f"\nTime Remaining: {format_time(current_hours, current_minutes, current_seconds)}")
        print("\n" + "="*50)
        
        # Wait for one second
        time.sleep(1)
        
        # Decrease total seconds
        total_seconds -= 1
    
    clear_screen()
    print("\n" + "="*50)
    print("Time's Up!")
    print("="*50)

def main():
    while True:
        clear_screen()
        print("\n" + "="*50)
        print("Welcome to Countdown Timer")
        print("="*50 + "\n")
        
        # Get time input from user
        hours, minutes, seconds = get_time_input()
        
        # Start countdown
        countdown(hours, minutes, seconds)
        
        # Ask if user wants to run another timer
        choice = input("\nDo you want to run another timer? (yes/no): ").lower()
        if choice != 'yes':
            break
    
    print("\nThanks for using Countdown Timer!")

if __name__ == "__main__":
    main() 