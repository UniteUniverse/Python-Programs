
# Birthday Wishing

Welcome to the Birthday Wishing project! This Python program automatically sends birthday wishes to your friends and family using a graphical user interface (GUI) created with the `tkinter` module and email functionality through the `smtplib` module.

## Author

This project was created by [Pratyush Kumar Jha](https://www.linkedin.com/in/pratyush-kumar-jha-b37a57235/).

## Features

- Automatically sends birthday wishes via email.
- Simple and interactive GUI created with the `tkinter` module.
- Stores and retrieves birthday data from a CSV file.

## Installation

To run this program, you'll need to have Python installed on your machine. You can download Python from the official website: [python.org](https://www.python.org/).

You will also need the `pandas` and `smtplib` modules.

1. Clone this repository to your local machine:

```sh
git clone https://github.com/UniteUniverse/Python-Programs.git
```

2. Navigate to the project directory:

```sh
cd Python-Programs/Project\ 25\ Birthday_Wishing
```

3. Install the required modules if you don't have them already:

```sh
pip install pandas
```

## Usage

To start the Birthday Wishing program, run the `Project_25_Birthday_Wishing.py` script:

```sh
python Project_25_Birthday_Wishing.py
```

The program will open a window where you can add new birthdays and send birthday wishes automatically.

## Example

Here's an example of what the output might look like:

```sh
A window opens where you can enter new birthdays and send birthday wishes via email.
```

## How the Code is Made

The Birthday Wishing code is made using Python's `tkinter` module for the GUI, `pandas` for managing the birthday data, and `smtplib` for sending emails. Here's a brief overview of how the code works:

1. **Importing Modules**: The `tkinter`, `pandas`, and `smtplib` modules are imported to create the GUI, manage the birthday data, and send emails.

2. **Loading Birthday Data**: The birthday data is loaded from a CSV file into a pandas DataFrame.

3. **Setting Up the GUI**: The main window is set up with labels, entry fields, and buttons for adding birthdays and sending birthday wishes.

4. **Sending Birthday Wishes**: A function is defined to send birthday wishes via email using the `smtplib` module. The function retrieves the email addresses and birthday messages from the DataFrame.

5. **Handling User Input**: The user can enter new birthdays, and the program updates the CSV file accordingly. The user can also trigger the function to send birthday wishes.

## Contributing

If you'd like to contribute to this project, feel free to fork the repository and submit a pull request. All contributions are welcome!

## Contact

For any questions or feedback, you can reach out to the author, Pratyush Kumar Jha, through his [LinkedIn profile](https://www.linkedin.com/in/pratyush-kumar-jha-b37a57235/).
