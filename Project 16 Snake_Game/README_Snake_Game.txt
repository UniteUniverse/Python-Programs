
# Snake Game

Welcome to the Snake Game project! This Python program implements the classic Snake game using the `turtle` module. The player controls a snake that moves around the screen, eating food to grow longer while avoiding collisions with the walls or itself.

## Author

This project was created by [Pratyush Kumar Jha](https://www.linkedin.com/in/pratyush-kumar-jha-b37a57235/).

## Features

- Classic Snake game mechanics.
- Uses the `turtle` module for graphics.
- Keeps track of the player's score.

## Installation

To run this program, you'll need to have Python installed on your machine. You can download Python from the official website: [python.org](https://www.python.org/).

You will also need the `turtle` module, which is included with Python's standard library.

1. Clone this repository to your local machine:

```sh
git clone https://github.com/UniteUniverse/Python-Programs.git
```

2. Navigate to the project directory:

```sh
cd Python-Programs/Project\ 16\ Snake_Game
```

## Usage

To start the Snake game, run the `Project_16_Snake_Game.py` script:

```sh
python Project_16_Snake_Game.py
```

The program will open a window and start the Snake game. Use the arrow keys to control the snake.

## Example

Here's an example of what the output might look like:

```sh
A window opens with a snake moving around the screen. The player uses the arrow keys to control the snake and eat food to grow longer while avoiding collisions.
```

## How the Code is Made

The Snake Game code is made using Python's `turtle` module for graphics and the `random` module to place the food at random locations. Here's a brief overview of how the code works:

1. **Importing Modules**: The `turtle` and `random` modules are imported to create the graphics and randomize food placement.

2. **Setting Up the Screen**: The screen is set up with a background color and title. The screen size is defined to create the boundaries of the game.

3. **Creating the Snake**: The snake is created using a list of turtle segments. Each segment is a turtle object, and the segments are linked together to form the snake.

4. **Creating the Food**: The food is created as a turtle object. Its position is randomized within the screen boundaries using the `random` module.

5. **Movement and Controls**: The snake's movement is controlled using functions that change the direction of the snake. The arrow keys are used to control the direction.

6. **Game Loop**: A `while` loop is used to keep the game running. The snake moves forward, and its position is updated. Collision detection is implemented to check if the snake collides with the walls or itself.

7. **Eating Food**: When the snake eats the food, a new segment is added to the snake, and the food is repositioned randomly.

8. **Ending the Game**: If a collision is detected, the game ends, and the player's score is displayed.

## Contributing

If you'd like to contribute to this project, feel free to fork the repository and submit a pull request. All contributions are welcome!

## Contact

For any questions or feedback, you can reach out to the author, Pratyush Kumar Jha, through his [LinkedIn profile](https://www.linkedin.com/in/pratyush-kumar-jha-b37a57235/).
