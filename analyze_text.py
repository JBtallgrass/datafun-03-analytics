"""Python outline"""

""" Start a data analytics project."""

# Start with imports from the Python Standard Library
import pathlib
import os
import time

# Import
import requests
import logging

# Configure logging - change level to DEBUG and re-run, to ERROR and rerun 
logging.basicConfig(
  filename='text_analysis.log', 
  level=logging.INFO, 
  filemode='w', 
  format='%(name)s.%(levelname)s.%(message)s'
)

# Get a configured logger instance and name it logger
logger = logging.getLogger()


# Set url
url = 'https://www.gutenberg.org/ebooks/1112.txt.utf-8'
logger.debug(f"Requesting URL: {url}") 

# Request response object
response = requests.get(url)
logger.debug(f"Response object: {response}")

if response.status_code == 200:
    text = response.text.lower()
    logger.info("Fetched text successfully.")
else:
    logger.error(f"Failed to fetch text. Status code: {response.status_code}")
    text = ""


# Define function here


# Define main() funtion here
def main():
    '''Main Function.'''
    pass # placeholder for code to be added later



if __name__ =='__main__':
    main()
