Mail Merge
This Python script automates the process of creating personalized letters by merging a template letter with a list of names. It reads names from a file, replaces a placeholder in the template letter with each name, and saves the personalized letters to individual files.

How It Works
The script performs the following tasks:

Reads a list of names from a file.
Reads a template letter from a file.
Replaces the placeholder in the template letter with each name.
Saves the personalized letters to individual files.
Prerequisites
Python 3.x
Usage
Clone the repository:
git clone https://github.com/UniteUniverse/Python-Programs.git
cd Python-Programs/Project%2033%20Mail_Merge

Prepare your input files:
invited_names.txt: A file containing the list of names, each on a new line.
starting_letter.txt: A file containing the template letter with a placeholder [name].
Run the script:
python mail_merge.py

Script Details
Placeholder: The placeholder [name] in the template letter that will be replaced with each name from the list.
Input Files:
invited_names.txt: Contains the names to be merged into the template letter.
starting_letter.txt: Contains the template letter with the placeholder.
Output Files: The personalized letters will be saved in the Output/ReadyToSend/ directory with filenames in the format letter_for_[name].txt.
Author
Pratyush Kumar Jha
