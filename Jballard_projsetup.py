"""This module provides functions for creating a series of project folders. """

# Import required modules from Python Standard Library
import math
import statistics
import pathlib
import time
from pathlib import Path # added for consistnecy in using Path

# Import my modules
import JBallard_utils

# Function Definitions

def create_project_directory(directory_name: str) -> None:
    """Creates a project subdirectory."""
    pathlib.Path(directory_name).mkdir(exist_ok=True)

"""Function 1. For item in Range: Create a function to generate folders for a given range (e.g., years)."""

def create_folders_for_range(directory_name='data', start_year=2000, end_year=2023):
    """Creates annual data directories within a specified range."""
    if end_year < start_year:  # Parameter validation
        raise ValueError("End year must be greater than or equal to start year")
    create_project_directory(directory_name)
    for year in range(start_year, end_year + 1):
        year_directory = pathlib.Path(directory_name).joinpath(str(year))
        create_project_directory(year_directory)
        print(f"Created {year_directory}")

"""Function 2. For Item in List: Develop a function to create folders from a list of names."""

def create_folders_from_list(directory_name: str, folder_list: list):
    """Creates specified folders within a directory."""
    create_project_directory(directory_name)
    for folder in folder_list:
        folder_directory = pathlib.Path(directory_name).joinpath(folder)
        create_project_directory(folder_directory)

def create_custom_folders_from_list(names: list, to_lowercase: bool = False, remove_spaces: bool = False) -> None:
    """
    Creates folders from a list of names with options to modify the folder names.
    :param names: List of names for the folders.
    :param to_lowercase: If True, converts folder names to lowercase.
    :param remove_spaces: If True, removes spaces from folder names.
    """
    for name in names:
        if to_lowercase:
            name = name.lower()
        if remove_spaces:
            name = name.replace(' ', '')
        folder_name = name
        Path(folder_name).mkdir(exist_ok=True)
        print(f"Folder '{folder_name}' created.")

"""Function 3. List Comprehension: Create a function to create prefixed folders by transforming
a list of names and combining each with a prefix (e.g., "data-")."""

def create_prefixed_folders(names: list, prefix: str) -> None:
    """Creates folders with a specified prefix from a list of names."""
    for folder in [prefix + name for name in names]:
        Path(folder).mkdir(exist_ok=True)
        print(f"Folder '{folder}' created.")

"""Function 4. While Loop: Write a function to create folders periodically (e.g., one folder every 5 seconds)."""       

def create_folders_periodically(prefix: str, count: int, interval: int) -> None:
    """
    Creates a specified number of folders at regular intervals.
    :param prefix: The prefix for the folder names.
    :param count: The number of folders to create.
    :param interval: The time interval (in seconds) between creating each folder.
    """
    for i in range(1, count + 1):
        folder_name = f"{prefix}{i}"
        try:
            Path(folder_name).mkdir(exist_ok=True)
            print(f"Folder '{folder_name}' created.")
        except Exception as e:
            print(f"Error creating folder '{folder_name}': {e}")
            continue #skip to the next iteration

        if i != count:
            time.sleep(interval)

def main():
    ''' Main function to demonstrate module capabilities. '''

    # Print byline from imported module
    print(f"Byline: {JBallard_utils.byline}")

    # Call function 1 to create folders for a range (e.g. years)
    create_folders_for_range(start_year=2020, end_year=2023)

    # Call function 2 to create folders given a list
    folder_names = ['data-csv', 'data-excel', 'data-json']
    create_folders_from_list('data', folder_names)
    # Added option
    regions = ["North America", "South America", "Europe", "Asia", "Africa", "Oceania", "Middle East"]
    create_custom_folders_from_list(regions, to_lowercase=True, remove_spaces=True)
    
    # Call function 3 to create folders using comprehension
    folder_names = ['csv', 'excel', 'json']
    prefix = 'data-'
    create_prefixed_folders(folder_names, prefix)

    # Call function 4 to create folders periodically using while
    prefix = 'temp-'  # or any other prefix you desire
    count = 10  # Number of folders to be created
    interval = 5  # Time interval in seconds between each folder creation
    create_folders_periodically(prefix, count, interval)

# Execute the main function
if __name__ == '__main__':
    main() 
    
