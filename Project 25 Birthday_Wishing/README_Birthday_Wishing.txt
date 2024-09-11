# Birthday Wishing Project

This Python project automates the process of sending birthday wishes via email. It reads birthday data from a CSV file, checks if today matches any birthdays, and sends a personalized email to the birthday person using pre-defined letter templates.

## Features

- Reads birthday data from a CSV file.
- Checks for birthdays matching the current date.
- Sends personalized birthday emails using SMTP.
- Uses random letter templates for variety.

## Requirements

- Python 3.x
- pandas
- smtplib

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/UniteUniverse/Python-Programs.git
    cd Project\ 25\ Birthday_Wishing
    ```

2. Install the required packages:
    ```bash
    pip install pandas
    ```

3. Set up your email credentials in the script:
    ```python
    my_email = "your_email@example.com"
    password = "your_password"
    ```

## Usage

1. Prepare your `birthdays.csv` file with the following columns:
    - `name`
    - `email`
    - `year`
    - `month`
    - `day`

2. Create letter templates in the `letter_templates` directory. Name them as `letter_1.txt`, `letter_2.txt`, etc. Use `[NAME]` as a placeholder for the recipient's name.

3. Run the script:
    ```bash
    python birthday_wisher.py
    ```

## Example

Here's an example of how your `birthdays.csv` might look:
```csv
name,email,year,month,day
John Doe,johndoe@example.com,1990,9,11
Jane Smith,janesmith@example.com,1985,9,11
```

And an example letter template (`letter_1.txt`):
```
Dear [NAME],

Wishing you a very Happy Birthday! May your day be filled with joy and happiness.

Best regards,
Your Friend
```

## Author

Pratyush Kumar Jha

## Contributing

Feel free to fork this repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.
