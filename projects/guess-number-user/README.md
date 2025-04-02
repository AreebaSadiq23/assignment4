# Guess the Number Game (Computer vs User)

A number guessing game where the computer tries to guess the number that the user is thinking of.

## Description

In this game, the user thinks of a number between 1 and 100, and the computer tries to guess it. After each guess, the user provides feedback whether the guess was too high, too low, or correct. The computer uses this feedback to narrow down the range of possible numbers.

## Features

- Computer makes intelligent guesses based on user feedback
- Input validation for user responses
- Detection of cheating (if user changes their number)
- Tracks number of attempts
- User-friendly interface

## How to Play

1. Run the program:
   ```bash
   python guess_number_user.py
   ```

2. Think of a number between 1 and 100
3. Press Enter when you're ready
4. For each computer guess, respond with:
   - "yes" if the guess is correct
   - "higher" if your number is higher
   - "lower" if your number is lower
5. Keep responding until the computer guesses your number

## Example Game

```
Welcome to Guess the Number!
Think of a number between 1 and 100, and I'll try to guess it.
Press Enter when you're ready...

Attempt 1: I guess 50
Is my guess correct? (yes/higher/lower): lower
I'll guess lower next time.

Attempt 2: I guess 25
Is my guess correct? (yes/higher/lower): higher
I'll guess higher next time.

...

Attempt 5: I guess 37
Is my guess correct? (yes/higher/lower): yes

Great! I guessed your number in 5 attempts!
```

## Requirements

- Python 3.6 or higher (for f-string support) 