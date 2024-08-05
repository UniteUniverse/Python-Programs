
# Weather Forecast

Welcome to the Weather Forecast project! This Python program provides weather forecasts for any city using a graphical user interface (GUI) created with the `tkinter` module. It fetches weather data from an online API and displays the current weather conditions and forecast.

## Author

This project was created by [Pratyush Kumar Jha](https://www.linkedin.com/in/pratyush-kumar-jha-b37a57235/).

## Features

- Provides current weather conditions and forecast for any city.
- Simple and interactive GUI created with the `tkinter` module.
- Retrieves weather data from an online API.

## Installation

To run this program, you'll need to have Python installed on your machine. You can download Python from the official website: [python.org](https://www.python.org/).

You will also need the `requests` module to fetch weather data from the online API.

1. Clone this repository to your local machine:

```sh
git clone https://github.com/UniteUniverse/Python-Programs.git
```

2. Navigate to the project directory:

```sh
cd Python-Programs/Project\ 29\ Weather_Forecast
```

3. Install the required `requests` module if you don't have it already:

```sh
pip install requests
```

## Usage

To start the Weather Forecast program, run the `Project_29_Weather_Forecast.py` script:

```sh
python Project_29_Weather_Forecast.py
```

The program will open a window where you can enter a city name and get the current weather conditions and forecast.

## Example

Here's an example of what the output might look like:

```sh
A window opens where you can enter a city name. The program displays the current weather conditions and forecast for the specified city.
```

## How the Code is Made

The Weather Forecast code is made using Python's `tkinter` module for the GUI and `requests` module to fetch weather data from an online API. Here's a brief overview of how the code works:

1. **Importing Modules**: The `tkinter` and `requests` modules are imported to create the GUI and fetch weather data from the online API.

2. **Setting Up the GUI**: The main window is set up with labels, entry fields, and buttons to enter a city name and fetch the weather data.

3. **Fetching Weather Data**: A function is defined to fetch the weather data from an online API using the `requests` module. The fetched data is then displayed in the GUI.

4. **Displaying Weather Data**: Functions are defined to display the current weather conditions and forecast based on the fetched data.

5. **Handling User Interaction**: The user can enter a city name and click a button to fetch and display the weather data for the specified city.

## Contributing

If you'd like to contribute to this project, feel free to fork the repository and submit a pull request. All contributions are welcome!

## Contact

For any questions or feedback, you can reach out to the author, Pratyush Kumar Jha, through his [LinkedIn profile](https://www.linkedin.com/in/pratyush-kumar-jha-b37a57235/).
