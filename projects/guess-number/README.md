# Guess the Number Game

A classic number guessing game where the computer thinks of a random number and the player tries to guess it within a limited number of attempts.

## Description

In this game, the computer generates a random number between 1 and 100. The player has 10 attempts to guess the correct number. After each guess, the computer provides feedback whether the guess was too high or too low.

## Features

- Random number generation
- Input validation
- Limited number of attempts (10)
- Helpful feedback after each guess
- Error handling for invalid inputs

## How to Play

1. Run the program:
   ```bash
   python guess_number.py
   ```

2. The computer will think of a number between 1 and 100
3. Enter your guess when prompted
4. You'll get feedback if your guess was too high or too low
5. Try to guess the number within 10 attempts!

## Example Game

```
Welcome to Guess the Number!
I'm thinking of a number between 1 and 100. You have 10 attempts to guess it.

Attempt 1/10
Enter your guess (1-100): 50
Too high! Try a lower number.

Attempt 2/10
Enter your guess (1-100): 25
Too low! Try a higher number.

...

Congratulations! You guessed the number in 4 attempts!
```

## Requirements

- Python 3.6 or higher (for f-string support) 