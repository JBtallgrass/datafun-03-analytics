"""Module 3 project"""
# Standard library imports
import csv
import pathlib 

# External library imports (requires virtual environment)
import requests  
import logging

# Local module imports
import JBallard_utils
import Jballard_projsetup

import requests

import requests

def fetch_and_write_txt_data(folder_name, filename, url):
    response = requests.get(url)  # Use the 'url' parameter here
    if response.status_code == 200:
        # Call your write function to save the response content
        pass # placeholder
    else:
        print(f"Failed to fetch data: {response.status_code}")

def fetch_and_write_excel_data(folder_name, filename, url):
    response = requests.get(url)
    if response.status_code == 200:
        # Call your write function to save the response content
        pass  # placeholder
    else:
        print(f"Failed to fetch Excel data: {response.status_code}")

