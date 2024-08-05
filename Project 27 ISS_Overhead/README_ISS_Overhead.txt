
# ISS Overhead Notifier

Welcome to the ISS Overhead Notifier project! This Python program notifies you when the International Space Station (ISS) is overhead using a graphical user interface (GUI) created with the `tkinter` module and API calls to get the ISS position and your location.

## Author

This project was created by [Pratyush Kumar Jha](https://www.linkedin.com/in/pratyush-kumar-jha-b37a57235/).

## Features

- Notifies you when the ISS is overhead.
- Simple and interactive GUI created with the `tkinter` module.
- Retrieves the ISS position and your location using online APIs.

## Installation

To run this program, you'll need to have Python installed on your machine. You can download Python from the official website: [python.org](https://www.python.org/).

You will also need the `requests` and `datetime` modules.

1. Clone this repository to your local machine:

```sh
git clone https://github.com/UniteUniverse/Python-Programs.git
```

2. Navigate to the project directory:

```sh
cd Python-Programs/Project\ 27\ ISS_Overhead
```

3. Install the required modules if you don't have them already:

```sh
pip install requests
```

## Usage

To start the ISS Overhead Notifier, run the `Project_27_ISS_Overhead.py` script:

```sh
python Project_27_ISS_Overhead.py
```

The program will open a window and notify you if the ISS is currently overhead based on your location.

## Example

Here's an example of what the output might look like:

```sh
A window opens and displays a message indicating whether the ISS is currently overhead or not.
```

## How the Code is Made

The ISS Overhead Notifier code is made using Python's `tkinter` module for the GUI, `requests` to fetch the ISS position and your location, and `datetime` to handle the time calculations. Here's a brief overview of how the code works:

1. **Importing Modules**: The `tkinter`, `requests`, and `datetime` modules are imported to create the GUI, fetch data from APIs, and handle time calculations.

2. **Setting Up the GUI**: The main window is set up with labels and buttons to display the notification and refresh the status.

3. **Fetching Data**: Functions are defined to fetch the ISS position from the Open Notify API and the user's location from the IP Geolocation API using the `requests` module.

4. **Checking Overhead Status**: A function is defined to check if the ISS is overhead by comparing its position with the user's location and the current time. The result is displayed in the GUI.

5. **Handling User Interaction**: The user can refresh the status by clicking a button, which triggers the functions to fetch data and update the notification.

## Contributing

If you'd like to contribute to this project, feel free to fork the repository and submit a pull request. All contributions are welcome!

## Contact

For any questions or feedback, you can reach out to the author, Pratyush Kumar Jha, through his [LinkedIn profile](https://www.linkedin.com/in/pratyush-kumar-jha-b37a57235/).
