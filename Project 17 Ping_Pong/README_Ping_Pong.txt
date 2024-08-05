
# Ping Pong Game

Welcome to the Ping Pong Game project! This Python program implements a classic Ping Pong game using the `turtle` module. Players can control the paddles to hit the ball back and forth, and the game keeps track of the score.

## Author

This project was created by [Pratyush Kumar Jha](https://www.linkedin.com/in/pratyush-kumar-jha-b37a57235/).

## Features

- Classic Ping Pong game mechanics.
- Uses the `turtle` module for graphics.
- Two-player mode with paddle controls.
- Keeps track of the players' scores.

## Installation

To run this program, you'll need to have Python installed on your machine. You can download Python from the official website: [python.org](https://www.python.org/).

You will also need the `turtle` module, which is included with Python's standard library.

1. Clone this repository to your local machine:

```sh
git clone https://github.com/UniteUniverse/Python-Programs.git
```

2. Navigate to the project directory:

```sh
cd Python-Programs/Project\ 17\ Ping_Pong
```

## Usage

To start the Ping Pong game, run the `Project_17_Ping_Pong.py` script:

```sh
python Project_17_Ping_Pong.py
```

The program will open a window and start the Ping Pong game. Use the 'W' and 'S' keys to control the left paddle and the Up and Down arrow keys to control the right paddle.

## Example

Here's an example of what the output might look like:

```sh
A window opens with a Ping Pong game. The players use the 'W' and 'S' keys to control the left paddle and the Up and Down arrow keys to control the right paddle. The game keeps track of the score as the ball bounces back and forth.
```

## How the Code is Made

The Ping Pong Game code is made using Python's `turtle` module for graphics. Here's a brief overview of how the code works:

1. **Importing Modules**: The `turtle` module is imported to create the graphics.

2. **Setting Up the Screen**: The screen is set up with a background color and title. The screen size is defined to create the boundaries of the game.

3. **Creating the Paddles and Ball**: The paddles and ball are created using turtle objects. Each paddle is controlled by different keys.

4. **Movement and Controls**: Functions are defined to move the paddles up and down. Key bindings are used to control the paddles.

5. **Game Loop**: A `while` loop is used to keep the game running. The ball moves forward, and its position is updated. Collision detection is implemented to check if the ball hits the paddles or the walls.

6. **Scoring**: The game keeps track of the players' scores. When the ball passes a paddle, the opposing player scores a point.

7. **Ending the Game**: The game continues until the players decide to close the window.

## Contributing

If you'd like to contribute to this project, feel free to fork the repository and submit a pull request. All contributions are welcome!

## Contact

For any questions or feedback, you can reach out to the author, Pratyush Kumar Jha, through his [LinkedIn profile](https://www.linkedin.com/in/pratyush-kumar-jha-b37a57235/).
