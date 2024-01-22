"""Module 3 project"""
# Standard library imports
import csv
import logging
from pathlib import Path
import json
import pandas as pd

# External library imports (requires virtual environment)
import requests


# Local module imports
import JBallard_utils  # lower case for consistency
import Jballard_projsetup # make this a lower case next time

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Data acquisition

def write_to_file(folder_name, filename, content, is_binary=False):
    mode = 'wb' if is_binary else 'w'
    encoding = None if is_binary else 'utf-8' # use utf-8 encoding for text files
    path = Path(folder_name)
    path.mkdir(parents=True, exist_ok=True) #Use this to create directory in the code rather than manual in the terminal
    with open(f"{folder_name}/{filename}", mode) as file:
        file.write(content)

def fetch_and_write_csv_data(csv_folder_name, csv_filename,csv_url):
    response = requests.get(url)
    if response.status_code == 200:
        if data_type == 'text' or data_type == 'csv':
            write_to_file(folder_name, filename, response.text)
        elif data_type == 'excel':
            write_to_file(folder_name, filename, response.content, is_binary=True)
       
    else:
        print(f"Failed to fetch {data_type} data: {response.status_code}")


def fetch_and_write_excel_data(excel_folder_name, excel_filename,excel_url):
    response = requests.get(url)
    if response.status_code == 200:
        if data_type == 'text' or data_type == 'csv':
            write_to_file(folder_name, filename, response.text)
        elif data_type == 'excel':
            write_to_file(folder_name, filename, response.content, is_binary=True)
       
    else:
        print(f"Failed to fetch {data_type} data: {response.status_code}")

def fetch_and_write_json_data(json_folder_name, json_filename,json_url):
    response = requests.get(url)
    if response.status_code == 200:
        if data_type == 'text' or data_type == 'csv':
            write_to_file(folder_name, filename, response.text)
        elif data_type == 'excel':
            write_to_file(folder_name, filename, response.content, is_binary=True)
       
    else:
        print(f"Failed to fetch {data_type} data: {response.status_code}")

def fetch_and_write_txt_data(folder_name, filename, url, data_type):
    response = requests.get(url)
    if response.status_code == 200:
        if data_type == 'text' or data_type == 'csv':
            write_to_file(folder_name, filename, response.text)
        elif data_type == 'excel':
            write_to_file(folder_name, filename, response.content, is_binary=True)
       
    else:
        print(f"Failed to fetch {data_type} data: {response.status_code}")

# process data and generate output

"""Function 1. Process Text Data: Process text with lists and sets to demonstrate proficiency in working with text files.
 Analyze text data to generate statistics like word count, frequency of words, etc., 
 and format these findings into a readable text file."""

def process_txt_file(txt_url, txt_filename):
    """Processes a text file to compute word count and word frequency.
    :param text_url: Path to the input text file text_url.
    :param txt_filename: Path to the output text file where the statistics will be saved txt_filename.
    """
    try:
        # Read the input file
        with open(txt_url, 'r', encoding='utf-8') as file:
            text_url = file.read()

        # Normalize the text to lowercase and split into words
        words = txt_url.lower().split()

        # Count the total number of words
        total_words = len(words)

        # Calculate the frequency of each word using a dictionary
        word_frequency = {}
        for word in words:
            word_frequency[word] = word_frequency.get(word, 0) + 1

        # Write the statistics to the output file
        with open(txt_filename, 'w', encoding='utf-8') as file:
            file.write(f"Total Words: {total_words}\n")
            file.write("Word Frequencies:\n")
            for word, freq in word_frequency.items():
                file.write(f"{word}: {freq}\n")

        print(f"Text data processed successfully. Output saved to {txt_filename.txt}")

    except IOError as e:
        print(f"I/O error({e.errno}): {e.strerror}")

# Example usage
process_txt_file('txt_url', 'txt_filename')

""" Function 2. Process CSV Data: Process CSV files with tuples to demonstrate proficiency in working with tabular data. 
Extract and analyze data from CSV files to produce meaningful statistics, summaries, or insights, 
and save the insights as text files."""

def process_csv_file(csv_url, csv_filename):
    try:
        # Read the CSV file
        df = pd.read_csv(csv_url)

        # Perform basic statistical analyses
        summary = df.describe()

        # Writing the results to a text file
        with open(csv_filename, 'w') as file:
            file.write("Basic Statistical Summary:\n")
            file.write(str(summary))

        print(f"Processed data written to {csv_filename}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
process_csv_file('csv_url', 'csv_filename.txt')


"""Function 3. Process Excel Data: Extract and analyze data from 
Excel files to produce meaningful statistics, summaries, or insights, 
and save the insights as text files. """

def process_excel_file(excel_url,  excel_file_name):
    try:
        # Read the Excel file
        df = pd.read_excel(excel_url)

        # Perform basic statistical analyses
        summary = df.describe()

        # Writing the results to a text file
        with open(excel_file_name, 'w') as file:
            file.write("Basic Statistical Summary:\n")
            file.write(str(summary))

        print(f"Processed data written to {excel_file_name}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
process_excel_file('excel_url', 'excel_file_name.txt')

"""Function 4. Process JSON Data: Process JSON data with dictionaries to 
demonstrate proficiency in working with labeled data. 
Parse the JSON data to extract relevant information and present it in a simplified, human-readable text format
"""

def process_json_file(json_url, json_filename):
    try:
        # Reading the JSON file
        with open(json_url, 'r') as file:
            data = json.load(file)

        # Process and extract relevant information
        processed_data = []
        for entry in data:
            summary = f"Name: {entry['name']}, Age: {entry['age']}, Email: {entry['email']}"
            processed_data.append(summary)

        # Writing the results to a text file
        with open(json_filename, 'w') as file:
            for line in processed_data:
                file.write(line + '\n')

        print(f"Processed data written to {json_filename}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
process_json_file('json_url', 'json_filename.txt')


#Implement excpetion Handling

def fetch_txt_data(folder_name, url):
    try:
        response = requests.get(url)
        response.raise_for_status()  
        # Will raise an HTTPError 
        # if the HTTP request returns an unsuccessful status code

        # Assuming the response content is text data
        file_path = Path(folder_name) / 'data.txt'
        with open(file_path, 'w') as file:
            file.write(response.text)
        print(f"Text data saved to {file_path}")

    except requests.exceptions.HTTPError as errh:
        print(f"Http Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"Oops: Something Else: {err}")
    except IOError as e:
        print(f"I/O error({e.errno}): {e.strerror}")

def main():
    ''' Main function to demonstrate module capabilities. '''

    print(f"Name: {yourname_attr.my_name_string}")

    txt_url = 'https://shakespeare.mit.edu/romeo_juliet/full.html'

    csv_url = 'https://raw.githubusercontent.com/MainakRepositor/Datasets/master/World%20Happiness%20Data/2020.csv' 

    excel_url = 'https://github.com/bharathirajatut/sample-excel-dataset/raw/master/cattle.xls' 
    
    json_url = 'http://api.open-notify.org/astros.json'

    txt_folder_name = 'data-txt'
    csv_folder_name = 'data-csv'
    excel_folder_name = 'data-excel' 
    json_folder_name = 'data-json' 

    txt_filename = 'data.txt'
    csv_filename = 'data.csv'
    excel_filename = 'data.xls' 
    json_filename = 'data.json' 

    fetch_and_write_txt_data(txt_folder_name, txt_filename, txt_url)
    fetch_and_write_csv_data(csv_folder_name, csv_filename,csv_url)
    fetch_and_write_excel_data(excel_folder_name, excel_filename,excel_url)
    fetch_and_write_json_data(json_folder_name, json_filename,json_url)

    process_txt_file(txt_folder_name,'data.txt', 'results_txt.txt')
    process_csv_file(csv_folder_name,'data.csv', 'results_csv.txt')
    process_excel_file(excel_folder_name,'data.xls', 'results_xls.txt')
    process_json_file(json_folder_name,'data.json', 'results_json.txt')

    # Find some data you care about. What format is it? How will you ingest the data?
    # What do you want to extract and write? What export format will you use?
    # Process at least TWO unique data sets and describe your work clearly.
    # Use the README.md and your code to showcase your ability to work with data.
