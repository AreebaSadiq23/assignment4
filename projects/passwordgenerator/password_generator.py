import random
import string

def generate_password(length, use_uppercase=True, use_lowercase=True, use_numbers=True, use_special=True):
    # Define character sets
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    numbers = string.digits
    special = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    # Initialize the character pool
    char_pool = ""
    
    # Add selected character types to the pool
    if use_uppercase:
        char_pool += uppercase
    if use_lowercase:
        char_pool += lowercase
    if use_numbers:
        char_pool += numbers
    if use_special:
        char_pool += special
    
    # Ensure at least one character from each selected type
    password = []
    
    if use_uppercase:
        password.append(random.choice(uppercase))
    if use_lowercase:
        password.append(random.choice(lowercase))
    if use_numbers:
        password.append(random.choice(numbers))
    if use_special:
        password.append(random.choice(special))
    
    # Fill the rest of the password
    remaining_length = length - len(password)
    password.extend(random.choice(char_pool) for _ in range(remaining_length))
    
    # Shuffle the password
    random.shuffle(password)
    
    return ''.join(password)

def get_password_requirements():
    print("\nPassword Requirements:")
    print("1. Length (8-32 characters)")
    print("2. Character Types:")
    print("   - Uppercase letters (A-Z)")
    print("   - Lowercase letters (a-z)")
    print("   - Numbers (0-9)")
    print("   - Special characters (!@#$%^&*()_+-=[]{}|;:,.<>?)")
    
    while True:
        try:
            length = int(input("\nEnter password length (8-32): "))
            if 8 <= length <= 32:
                break
            print("Length must be between 8 and 32 characters!")
        except ValueError:
            print("Please enter a valid number!")
    
    print("\nSelect character types to include:")
    use_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
    use_lowercase = input("Include lowercase letters? (yes/no): ").lower() == 'yes'
    use_numbers = input("Include numbers? (yes/no): ").lower() == 'yes'
    use_special = input("Include special characters? (yes/no): ").lower() == 'yes'
    
    # Ensure at least one character type is selected
    if not any([use_uppercase, use_lowercase, use_numbers, use_special]):
        print("At least one character type must be selected!")
        return get_password_requirements()
    
    return length, use_uppercase, use_lowercase, use_numbers, use_special

def check_password_strength(password):
    strength = 0
    feedback = []
    
    # Check length
    if len(password) >= 12:
        strength += 2
    elif len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password is too short")
    
    # Check character types
    if any(c.isupper() for c in password):
        strength += 1
    else:
        feedback.append("No uppercase letters")
    
    if any(c.islower() for c in password):
        strength += 1
    else:
        feedback.append("No lowercase letters")
    
    if any(c.isdigit() for c in password):
        strength += 1
    else:
        feedback.append("No numbers")
    
    if any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password):
        strength += 1
    else:
        feedback.append("No special characters")
    
    # Determine strength level
    if strength >= 5:
        level = "Strong"
    elif strength >= 3:
        level = "Medium"
    else:
        level = "Weak"
    
    return level, feedback

def main():
    print("="*50)
    print("Welcome to Password Generator")
    print("="*50)
    
    while True:
        # Get password requirements
        length, use_uppercase, use_lowercase, use_numbers, use_special = get_password_requirements()
        
        # Generate password
        password = generate_password(length, use_uppercase, use_lowercase, use_numbers, use_special)
        
        # Check password strength
        strength, feedback = check_password_strength(password)
        
        # Display results
        print("\n" + "="*50)
        print("Generated Password:", password)
        print("Password Strength:", strength)
        if feedback:
            print("Suggestions for improvement:")
            for suggestion in feedback:
                print(f"- {suggestion}")
        print("="*50)
        
        # Ask if user wants to generate another password
        choice = input("\nGenerate another password? (yes/no): ").lower()
        if choice != 'yes':
            break
    
    print("\nThanks for using Password Generator!")

if __name__ == "__main__":
    main() 