
# Turtle Race

Welcome to the Turtle Race project! This Python program simulates a race between multiple turtles using the `turtle` module. Each turtle moves forward by a random amount, and the first turtle to reach the finish line wins. It's a fun way to learn about the `turtle` module and random number generation in Python.

## Author

This project was created by [Pratyush Kumar Jha](https://www.linkedin.com/in/pratyush-kumar-jha-b37a57235/).

## Features

- Simulates a race between multiple turtles.
- Uses the `turtle` module for graphics.
- Randomizes each turtle's movement to create an unpredictable race.

## Installation

To run this program, you'll need to have Python installed on your machine. You can download Python from the official website: [python.org](https://www.python.org/).

You will also need the `turtle` module, which is included with Python's standard library.

1. Clone this repository to your local machine:

```sh
git clone https://github.com/UniteUniverse/Python-Programs.git
```

2. Navigate to the project directory:

```sh
cd Python-Programs/Project\ 15\ Turtle_Race
```

## Usage

To start the turtle race, run the `Project_15_Turtle_Race.py` script:

```sh
python Project_15_Turtle_Race.py
```

The program will open a window and start the turtle race.

## Example

Here's an example of what the output might look like:

```sh
A window opens with multiple turtles lined up at the start line. Each turtle moves forward by a random amount until one of them crosses the finish line.
```

## How the Code is Made

The Turtle Race code is made using Python's `turtle` module for graphics and the `random` module for random movement. Here's a brief overview of how the code works:

1. **Importing Modules**: The `turtle` and `random` modules are imported to create the graphics and randomize movements.

2. **Setting Up the Race**: The screen and turtles are set up. Each turtle is given a unique color and positioned at the starting line.

3. **Starting the Race**: A `while` loop is used to repeatedly move each turtle forward by a random amount.
    - The `random` module is used to determine how far each turtle moves forward.
    - The loop continues until one of the turtles crosses the finish line.

4. **Determining the Winner**: Once a turtle crosses the finish line, the race ends, and the program announces the winner.

5. **Ending the Program**: The `turtle.done()` function is called to keep the window open and display the results.

## Contributing

If you'd like to contribute to this project, feel free to fork the repository and submit a pull request. All contributions are welcome!

## Contact

For any questions or feedback, you can reach out to the author, Pratyush Kumar Jha, through his [LinkedIn profile](https://www.linkedin.com/in/pratyush-kumar-jha-b37a57235/).
