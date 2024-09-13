100 Movies to Watch
This Python script scrapes a list of the top 100 movies from a web page and saves them to a text file. It uses the BeautifulSoup library to parse the HTML content and extract the movie titles.

How It Works
The script performs the following tasks:

Fetches the web page containing the list of top 100 movies using the requests library.
Parses the HTML content of the web page using BeautifulSoup.
Extracts the movie titles from the HTML elements.
Writes the movie titles to a text file in reverse order.
Prerequisites
Python 3.x
requests library
beautifulsoup4 library
You can install the required libraries using:

pip install requests beautifulsoup4

Usage
Clone the repository:
git clone https://github.com/UniteUniverse/Python-Programs.git
cd Python-Programs/Project%2034%20100_movies_to_watch_start

Run the script:
python movies_scraper.py

Script Details
URL: The URL of the web page containing the list of top 100 movies.
BeautifulSoup: Used to parse the HTML content and extract movie titles.
Reverse Order: The movie titles are saved in reverse order to the text file.
Author
Pratyush Kumar Jha
