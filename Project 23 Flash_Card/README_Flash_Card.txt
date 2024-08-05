
# Flash Card

Welcome to the Flash Card project! This Python program helps you study and memorize information using flash cards. The program uses a graphical user interface (GUI) created with the `tkinter` module to display flash cards for learning new information.

## Author

This project was created by [Pratyush Kumar Jha](https://www.linkedin.com/in/pratyush-kumar-jha-b37a57235/).

## Features

- Displays flash cards to help you study and memorize information.
- Simple and interactive GUI created with the `tkinter` module.
- Tracks which flash cards you have learned and which ones you need to review.
- Allows you to create and save your own sets of flash cards.

## Installation

To run this program, you'll need to have Python installed on your machine. You can download Python from the official website: [python.org](https://www.python.org/).

1. Clone this repository to your local machine:

```sh
git clone https://github.com/UniteUniverse/Python-Programs.git
```

2. Navigate to the project directory:

```sh
cd Python-Programs/Project\ 23\ Flash_Card
```

## Usage

To start the Flash Card program, run the `Project_23_Flash_Card.py` script:

```sh
python Project_23_Flash_Card.py
```

The program will open a window where you can view and interact with flash cards.

## Example

Here's an example of what the output might look like:

```sh
A window opens with a flash card displayed. You can flip the card to see the answer and mark the card as learned or review it later.
```

## How the Code is Made

The Flash Card code is made using Python's `tkinter` module for the GUI and `pandas` for managing the flash card data. Here's a brief overview of how the code works:

1. **Importing Modules**: The `tkinter` and `pandas` modules are imported to create the GUI and manage the flash card data.

2. **Loading Flash Card Data**: The flash card data is loaded from a CSV file into a pandas DataFrame.

3. **Setting Up the GUI**: The main window is set up with labels, buttons, and a canvas for displaying the flash cards.

4. **Displaying Flash Cards**: Functions are defined to display the flash cards and flip them to show the answer. The program tracks which flash cards have been learned and which ones need review.

5. **Handling User Input**: The user can interact with the flash cards using buttons to mark them as learned or to review them later. The program updates the flash card data accordingly.

6. **Saving Progress**: The program saves the progress by updating the flash card data file with the cards that have been learned and those that still need review.

## Contributing

If you'd like to contribute to this project, feel free to fork the repository and submit a pull request. All contributions are welcome!

## Contact

For any questions or feedback, you can reach out to the author, Pratyush Kumar Jha, through his [LinkedIn profile](https://www.linkedin.com/in/pratyush-kumar-jha-b37a57235/).
