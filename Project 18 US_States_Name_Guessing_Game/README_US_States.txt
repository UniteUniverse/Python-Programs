
# US States Name Guessing Game

Welcome to the US States Name Guessing Game project! This Python program challenges you to name all the US states using the `turtle` module for the graphical interface. It's a fun and educational way to learn and test your knowledge of US geography.

## Author

This project was created by [Pratyush Kumar Jha](https://www.linkedin.com/in/pratyush-kumar-jha-b37a57235/).

## Features

- Interactive game to guess the names of US states.
- Uses the `turtle` module for a graphical interface.
- Displays the map of the US and tracks correctly guessed states.

## Installation

To run this program, you'll need to have Python installed on your machine. You can download Python from the official website: [python.org](https://www.python.org/).

You will also need the `turtle` module, which is included with Python's standard library.

1. Clone this repository to your local machine:

```sh
git clone https://github.com/UniteUniverse/Python-Programs.git
```

2. Navigate to the project directory:

```sh
cd Python-Programs/Project\ 18\ US_States_Name_Guessing_Game
```

## Usage

To start the US States Name Guessing Game, run the `Project_18_US_States_Name_Guessing_Game.py` script:

```sh
python Project_18_US_States_Name_Guessing_Game.py
```

The program will open a window displaying the map of the US. Type the names of the states to guess them. Correct guesses will be displayed on the map.

## Example

Here's an example of what the output might look like:

```sh
A window opens with a map of the US. The player types the name of a state, and if correct, the state name is displayed on the map.
```

## How the Code is Made

The US States Name Guessing Game code is made using Python's `turtle` module for graphics and the `pandas` module to manage the data. Here's a brief overview of how the code works:

1. **Importing Modules**: The `turtle` and `pandas` modules are imported to create the graphics and manage the state data.

2. **Setting Up the Screen**: The screen is set up with the map of the US as the background.

3. **Loading State Data**: The state names and their coordinates are loaded from a CSV file using the `pandas` module.

4. **Game Loop**: A `while` loop is used to repeatedly prompt the player to enter a state name.
    - The player's guess is compared to the list of state names.
    - If the guess is correct, the state name is displayed on the map at the correct coordinates.
    - The loop continues until all states are guessed or the player decides to exit.

5. **Ending the Game**: Once the game ends, the program displays the list of states that were not guessed.

## Contributing

If you'd like to contribute to this project, feel free to fork the repository and submit a pull request. All contributions are welcome!

## Contact

For any questions or feedback, you can reach out to the author, Pratyush Kumar Jha, through his [LinkedIn profile](https://www.linkedin.com/in/pratyush-kumar-jha-b37a57235/).
