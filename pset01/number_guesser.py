# ----------------------------------------------------------------------
# This is the file number_guesser.py

# The intent is to give you practice writing a complete, interactive
# Python program.

# Remove the comments in this file when you have completed your program.
# You can, and should, include your own comments, but please remove the
# comments that are here now.
# ----------------------------------------------------------------------
import random

def number_guesser():
    print("Welcome to the Number Guesser!")
    print("Guess a number between 1 and 1000.")
    print("Type 'exit' to quit the game.\n")

    while True:
        number = random.randint(1, 1000)
        attempts = 0

        while True:
            guess = input("Enter your guess: ").strip()

            if guess.lower() in ('exit'):
                print("Thanks for playing. Goodbye!")
                return

            if not guess.isdigit():
                print("Please enter a valid number.")
                continue

            guess = int(guess)
            attempts += 1

            if guess < number:
                print("Too low!")
            elif guess > number:
                print("Too high!")
            else:
                print(f"🎉 Congratulations! You guessed the number {number} in {attempts} attempts.\n")
                break  # Start a new game

if __name__ == "__main__":
    number_guesser()