
# Hirst Painting

Welcome to the Hirst Painting project! This Python program creates a digital artwork inspired by the dot paintings of artist Damien Hirst. Using the `turtle` module, the program generates a grid of colored dots to simulate a Hirst-style painting.

## Author

This project was created by [Pratyush Kumar Jha](https://www.linkedin.com/in/pratyush-kumar-jha-b37a57235/).

## Features

- Generates a grid of colored dots to simulate a Hirst-style painting.
- Uses the `turtle` module for graphics.
- Randomizes colors for each dot to create a unique artwork every time.

## Installation

To run this program, you'll need to have Python installed on your machine. You can download Python from the official website: [python.org](https://www.python.org/).

You will also need the `turtle` module, which is included with Python's standard library.

1. Clone this repository to your local machine:

```sh
git clone https://github.com/UniteUniverse/Python-Programs.git
```

2. Navigate to the project directory:

```sh
cd Python-Programs/Project\ 14\ Hirst
```

## Usage

To create the Hirst-style painting, run the `Project_14_Hirst.py` script:

```sh
python Project_14_Hirst.py
```

The program will open a window and draw the artwork using the `turtle` module.

## Example

Here's an example of what the output might look like:

```sh
A window opens with a grid of colored dots, creating a Hirst-style painting.
```

## How the Code is Made

The Hirst Painting code is made using Python's `turtle` module for graphics and the `random` module for color generation. Here's a brief overview of how the code works:

1. **Importing Modules**: The `turtle` and `random` modules are imported to create the graphics and randomize colors.

2. **Setting Up the Turtle**: The turtle is set up with a screen and a turtle object. The speed of the turtle is set to the maximum to draw the painting quickly.

3. **Creating the Dot Grid**: A nested loop is used to create a grid of dots. The outer loop iterates over rows, and the inner loop iterates over columns.
    - The turtle moves to the correct position for each dot.
    - A random color is chosen using the `random` module.
    - The turtle draws a dot with the chosen color.

4. **Ending the Program**: Once the grid is complete, the `turtle.done()` function is called to keep the window open.

## Contributing

If you'd like to contribute to this project, feel free to fork the repository and submit a pull request. All contributions are welcome!

## Contact

For any questions or feedback, you can reach out to the author, Pratyush Kumar Jha, through his [LinkedIn profile](https://www.linkedin.com/in/pratyush-kumar-jha-b37a57235/).
