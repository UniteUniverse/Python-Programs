
# Motivational Quote

Welcome to the Motivational Quote project! This Python program displays a new motivational quote each day using a graphical user interface (GUI) created with the `tkinter` module. It's a great way to start your day with some inspiration.

## Author

This project was created by [Pratyush Kumar Jha](https://www.linkedin.com/in/pratyush-kumar-jha-b37a57235/).

## Features

- Displays a new motivational quote each day.
- Simple and interactive GUI created with the `tkinter` module.
- Retrieves quotes from an online API.

## Installation

To run this program, you'll need to have Python installed on your machine. You can download Python from the official website: [python.org](https://www.python.org/).

You will also need the `requests` module to fetch quotes from the online API.

1. Clone this repository to your local machine:

```sh
git clone https://github.com/UniteUniverse/Python-Programs.git
```

2. Navigate to the project directory:

```sh
cd Python-Programs/Project\ 24\ Motivational_Quote
```

3. Install the required `requests` module if you don't have it already:

```sh
pip install requests
```

## Usage

To start the Motivational Quote program, run the `Project_24_Motivational_Quote.py` script:

```sh
python Project_24_Motivational_Quote.py
```

The program will open a window displaying a motivational quote.

## Example

Here's an example of what the output might look like:

```sh
A window opens displaying a motivational quote for the day.
```

## How the Code is Made

The Motivational Quote code is made using Python's `tkinter` module for the GUI and `requests` module to fetch quotes from an online API. Here's a brief overview of how the code works:

1. **Importing Modules**: The `tkinter` and `requests` modules are imported to create the GUI and fetch quotes from the online API.

2. **Setting Up the GUI**: The main window is set up with labels to display the quote and buttons to refresh the quote or close the window.

3. **Fetching Quotes**: A function is defined to fetch a motivational quote from an online API using the `requests` module. The fetched quote is then displayed in the GUI.

4. **Handling User Interaction**: The user can refresh the quote by clicking a button, which triggers the function to fetch and display a new quote.

## Contributing

If you'd like to contribute to this project, feel free to fork the repository and submit a pull request. All contributions are welcome!

## Contact

For any questions or feedback, you can reach out to the author, Pratyush Kumar Jha, through his [LinkedIn profile](https://www.linkedin.com/in/pratyush-kumar-jha-b37a57235/).
