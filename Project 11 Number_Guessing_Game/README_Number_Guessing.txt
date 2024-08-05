
# Number Guessing Game

Welcome to the Number Guessing Game project! This Python program allows you to play a game where you have to guess a randomly generated number within a specified range. It's a fun way to practice Python programming and understand basic game logic.

## Author

This project was created by [Pratyush Kumar Jha](https://www.linkedin.com/in/pratyush-kumar-jha-b37a57235/).

## Features

- Generates a random number within a specified range.
- Prompts the user to guess the number and provides feedback.
- Simple and interactive command-line interface.

## Installation

To run this program, you'll need to have Python installed on your machine. You can download Python from the official website: [python.org](https://www.python.org/).

1. Clone this repository to your local machine:

```sh
git clone https://github.com/UniteUniverse/Python-Programs.git
```

2. Navigate to the project directory:

```sh
cd Python-Programs/Project\ 11\ Number_Guessing_Game
```

## Usage

To start the number guessing game, run the `Project_11_Number_Guessing_Game.py` script:

```sh
python Project_11_Number_Guessing_Game.py
```

Follow the on-screen prompts to guess the number and receive feedback until you guess correctly.

## Example

Here's an example of what the output might look like:

```sh
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
Make a guess: 50
Too low.
Make a guess: 75
Too high.
Make a guess: 60
Correct! You guessed the number in 3 attempts.
```

## How the Code is Made

The Number Guessing Game code is made using Python's basic input and output functions, along with the `random` module to generate a random number. Here's a brief overview of how the code works:

1. **Importing the `random` Module**: The `random` module is imported to generate a random number within a specified range.

2. **Setting Up the Game**: The game welcomes the player and sets the range for the random number (e.g., between 1 and 100).

3. **Generating the Random Number**: A random number is generated using `random.randint(1, 100)` and stored in a variable.

4. **Game Loop**: A `while` loop is used to repeatedly prompt the player to guess the number until they guess correctly.
    - The player's guess is compared to the random number.
    - Feedback is provided ("Too low", "Too high", or "Correct").
    - The loop keeps track of the number of attempts.

5. **Ending the Game**: Once the player guesses correctly, the game congratulates the player and displays the number of attempts taken.

## Contributing

If you'd like to contribute to this project, feel free to fork the repository and submit a pull request. All contributions are welcome!

## Contact

For any questions or feedback, you can reach out to the author, Pratyush Kumar Jha, through his [LinkedIn profile](https://www.linkedin.com/in/pratyush-kumar-jha-b37a57235/).
