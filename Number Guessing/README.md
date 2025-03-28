﻿# Number Guessing Game

## Description
This is a simple CLI-based number guessing game where the computer randomly selects a number, and the player has to guess it. The player has a limited number of attempts based on the chosen difficulty level.

## Features
- Difficulty levels:
  - Easy (10 chances)
  - Medium (5 chances)
  - Hard (3 chances)
- Feedback on whether the guessed number is higher or lower than the actual number.
- Timer to track how long it takes the player to guess the number.
- High score tracking based on the fewest attempts.
- Option to play multiple rounds until the player decides to quit.

## How to Play
1. Run the Python script.
2. Select a difficulty level by entering 1, 2, or 3.
3. Enter a guess between 1 and 100.
4. The game provides hints if the guess is incorrect.
5. The game ends when the correct number is guessed or when attempts run out.
6. The player can choose to play again after each round.

## Installation & Execution
1. Ensure you have Python installed (version 3.x recommended).
2. Clone or download the script.
3. Open a terminal/command prompt and navigate to the script location.
4. Run the script using:
   ```sh
   python number_guessing_game.py
   ```

## Requirements
- Python 3.x
- No additional dependencies required

## Example Output
```
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
Please select the difficulty level:
1. Easy (10 chances)
2. Medium (5 chances)
3. Hard (3 chances)
Enter your choice: 2

Great! You have selected the Medium difficulty level.
Let's start the game!

Enter your guess: 50
Incorrect! The number is less than 50.

Enter your guess: 25
Incorrect! The number is greater than 25.

Enter your guess: 30
Congratulations! You guessed the correct number in 3 attempts.
Time taken: 12.5 seconds.

Do you want to play again? (yes/no):
```

## Author
- Created by Nathishwar-prog -> https://github.com/Nathishwar-prog

## License
This project is open-source and free to use.


