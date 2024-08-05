
# Quizzler

Welcome to the Quizzler project! This Python program is a quiz game that tests your knowledge on various topics using a graphical user interface (GUI) created with the `tkinter` module. It fetches quiz questions from an online API and displays them in a fun, interactive format.

## Author

This project was created by [Pratyush Kumar Jha](https://www.linkedin.com/in/pratyush-kumar-jha-b37a57235/).

## Features

- Interactive quiz game with multiple-choice questions.
- Simple and engaging GUI created with the `tkinter` module.
- Fetches quiz questions from an online API.
- Keeps track of the score and provides feedback on answers.

## Installation

To run this program, you'll need to have Python installed on your machine. You can download Python from the official website: [python.org](https://www.python.org/).

You will also need the `requests` module to fetch quiz questions from the online API.

1. Clone this repository to your local machine:

```sh
git clone https://github.com/UniteUniverse/Python-Programs.git
```

2. Navigate to the project directory:

```sh
cd Python-Programs/Project\ 28\ Quizzler
```

3. Install the required `requests` module if you don't have it already:

```sh
pip install requests
```

## Usage

To start the Quizzler game, run the `Project_28_Quizzler.py` script:

```sh
python Project_28_Quizzler.py
```

The program will open a window displaying quiz questions and options for you to choose from. Your score will be updated based on your answers.

## Example

Here's an example of what the output might look like:

```sh
A window opens displaying a quiz question with multiple-choice answers. You select an answer, and the program provides feedback and updates your score.
```

## How the Code is Made

The Quizzler code is made using Python's `tkinter` module for the GUI and `requests` module to fetch quiz questions from an online API. Here's a brief overview of how the code works:

1. **Importing Modules**: The `tkinter` and `requests` modules are imported to create the GUI and fetch quiz questions from the online API.

2. **Setting Up the GUI**: The main window is set up with labels, buttons, and a canvas for displaying the quiz questions and options.

3. **Fetching Quiz Questions**: A function is defined to fetch quiz questions from an online API using the `requests` module. The fetched questions are stored for display.

4. **Displaying Questions**: Functions are defined to display the quiz questions and options. The program keeps track of the current question and updates the display accordingly.

5. **Handling User Interaction**: The user selects an answer, and the program provides feedback on whether the answer is correct. The score is updated based on the user's answers.

## Contributing

If you'd like to contribute to this project, feel free to fork the repository and submit a pull request. All contributions are welcome!

## Contact

For any questions or feedback, you can reach out to the author, Pratyush Kumar Jha, through his [LinkedIn profile](https://www.linkedin.com/in/pratyush-kumar-jha-b37a57235/).
