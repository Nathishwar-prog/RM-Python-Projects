import random
import time
from random import choice


def get_attempts():
    print("Please select the difficuty level : ","1. Easy (10 chances)","2. Medium (5 Chances)","3. Hard (3 chances)",sep="\n")

    while True:
        choice : int = int(input("Enter the choice (1/2/3):"))
        if choice == 1:
            return 10
        elif choice == 2:
            return 5
        elif choice == 3:
            return 3
        else:
            print("Invalid Choice . Please select 1,2, or 3.")

def play_game():
    print("Welcome to the Number Guessing Game!","I'm thinking of a number between 1 and 100",sep="\n")
    attempts_allowed = get_attempts()
    number_to_guess = random.randint(1,100)
    attempts = 0
    start_time = time.time()

    print(f"\nYou have {attempts_allowed} chances to guess the correct number. Let's start!")

    while attempts < attempts_allowed:
        try:
            guess_number : int = int(input("Enter your guess:"))
        except ValueError:
            print("Invalid Input: Please enter a number between 1 and 100.")
            continue
        attempts +=1
        if guess_number == number_to_guess:
            end_time = time.time()
            print(f"\nCongratulations! You guessed the correct number in {attempts} attempts.")
            print(f"Time taken: {round(end_time - start_time, 2)} seconds.")
            return attempts
        elif guess_number < number_to_guess:
            print("Incorrect! The number is greater than", guess_number)
        else:
            print("Incorrect! The number is less than", guess_number)

        if attempts == attempts_allowed:
            print(f"\nGame Over! The correct number was {number_to_guess}.")
            return None


def main():
    high_score = None

    while True:
        result = play_game()

        if result and (high_score is None or result < high_score):
            high_score = result
            print(f"New High Score! Fewest attempts: {high_score}")

        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye!")
            break


if __name__ == "__main__":
    main()





