
# Quiz Time

Welcome to the Quiz Time project! This Python program is an interactive quiz game that allows users to answer multiple-choice questions and receive immediate feedback on their answers. It's a fun way to test your knowledge and practice Python programming.

## Author

This project was created by [Pratyush Kumar Jha](https://www.linkedin.com/in/pratyush-kumar-jha-b37a57235/).

## Features

- Interactive quiz with multiple-choice questions.
- Provides immediate feedback on the correctness of answers.
- Simple and engaging command-line interface.

## Installation

To run this program, you'll need to have Python installed on your machine. You can download Python from the official website: [python.org](https://www.python.org/).

1. Clone this repository to your local machine:

```sh
git clone https://github.com/UniteUniverse/Python-Programs.git
```

2. Navigate to the project directory:

```sh
cd Python-Programs/Project\ 13\ Quiz\ Time
```

## Usage

To start the quiz, run the `Project_13_Quiz_Time.py` script:

```sh
python Project_13_Quiz_Time.py
```

Follow the on-screen prompts to answer the quiz questions and receive feedback on your answers.

## Example

Here's an example of what the output might look like:

```sh
Welcome to Quiz Time!
Question 1: What is the capital of France?
a) London
b) Berlin
c) Paris
d) Madrid
Your answer: c
Correct!
```

## How the Code is Made

The Quiz Time code is made using Python's basic input and output functions, along with a list to store the questions and their respective choices. Here's a brief overview of how the code works:

1. **Storing Questions and Answers**: The questions and their multiple-choice options are stored in a list of dictionaries. Each dictionary contains a question, a list of choices, and the correct answer.

2. **Setting Up the Game**: The game welcomes the player and initializes the quiz.

3. **Game Loop**: A `for` loop is used to iterate through each question, displaying the question and the choices to the player.
    - The player's answer is compared to the correct answer.
    - Feedback is provided ("Correct!" or "Wrong, the correct answer is...").
    - The loop continues until all questions have been answered.

4. **Ending the Game**: Once all questions have been answered, the game thanks the player for participating and displays the final score.

## Contributing

If you'd like to contribute to this project, feel free to fork the repository and submit a pull request. All contributions are welcome!

## Contact

For any questions or feedback, you can reach out to the author, Pratyush Kumar Jha, through his [LinkedIn profile](https://www.linkedin.com/in/pratyush-kumar-jha-b37a57235/).
