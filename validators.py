# validators.py
# Simple input validation functions for the library system.


def is_valid_input(value):
    """
    Check that a text input is not empty after stripping whitespace.
    Returns True if the value has content, False if it is empty.
    """
    return value.strip() != ""


def is_valid_book_id_format(book_id):
    """
    Check that a Book ID is not empty.
    A Book ID just needs to be a non-empty string (e.g., B001, 101, LIB-01).
    Returns True if valid, False otherwise.
    """
    return book_id.strip() != ""
