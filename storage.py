# storage.py
# Handles loading and saving book data using a JSON file.

import json
import os

# Path to the data file where books are stored
DATA_FILE = "data/books.json"


def load_books():
    """
    Load books from the JSON file.
    Returns an empty list if the file does not exist or has invalid data.
    """
    # If the file doesn't exist yet, return an empty list
    if not os.path.exists(DATA_FILE):
        return []

    try:
        with open(DATA_FILE, "r") as f:
            content = f.read().strip()
            # Handle an empty file safely
            if not content:
                return []
            return json.loads(content)
    except json.JSONDecodeError:
        # The file has invalid JSON - start fresh rather than crashing
        print("Warning: Data file is corrupted. Starting with an empty library.")
        return []
    except IOError:
        print("Warning: Could not read data file. Starting with an empty library.")
        return []


def save_books(books):
    """
    Save the list of books to the JSON file.
    Creates the data folder if it doesn't exist.
    """
    # Make sure the data folder exists before writing
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)

    try:
        with open(DATA_FILE, "w") as f:
            json.dump(books, f, indent=4)
    except IOError:
        print("Error: Could not save data. Changes may not be saved.")
