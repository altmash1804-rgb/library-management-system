# library.py
# Handles all library operations: add, view, search, issue, return, statistics.

from storage import load_books, save_books
from validators import is_valid_input, is_valid_book_id_format


def get_all_books():
    """Return the full list of books from storage."""
    return load_books()


def add_book(book_id, title, author, category):
    """
    Add a new book to the library.
    Returns (True, message) on success, (False, message) on failure.
    """
    books = load_books()

    # Check if Book ID already exists
    for book in books:
        if book["id"].lower() == book_id.lower():
            return False, f"Book ID '{book_id}' already exists. Please use a different ID."

    # Build the new book as a simple dictionary
    new_book = {
        "id": book_id.strip(),
        "title": title.strip(),
        "author": author.strip(),
        "category": category.strip(),
        "status": "Available"
    }

    books.append(new_book)
    save_books(books)
    return True, f"Book '{title}' added successfully!"


def search_books(keyword):
    """
    Search books by ID, title, or author.
    The search is case-insensitive.
    Returns a list of matching books.
    """
    books = load_books()
    keyword = keyword.lower().strip()
    results = []

    for book in books:
        # Check if the keyword appears in ID, title, or author
        if (keyword in book["id"].lower() or
                keyword in book["title"].lower() or
                keyword in book["author"].lower()):
            results.append(book)

    return results


def issue_book(book_id):
    """
    Issue a book by its ID.
    Returns (True, message) on success, (False, message) on failure.
    """
    books = load_books()

    for book in books:
        if book["id"].lower() == book_id.lower():
            if book["status"] == "Issued":
                return False, f"Book '{book['title']}' is already issued."
            # Mark the book as Issued and save
            book["status"] = "Issued"
            save_books(books)
            return True, f"Book '{book['title']}' has been issued successfully."

    return False, f"Book ID '{book_id}' not found."


def return_book(book_id):
    """
    Return a book by its ID.
    Returns (True, message) on success, (False, message) on failure.
    """
    books = load_books()

    for book in books:
        if book["id"].lower() == book_id.lower():
            if book["status"] == "Available":
                return False, f"Book '{book['title']}' is already available (not issued)."
            # Mark the book as Available and save
            book["status"] = "Available"
            save_books(books)
            return True, f"Book '{book['title']}' has been returned successfully."

    return False, f"Book ID '{book_id}' not found."


def get_available_books():
    """Return a list of books that are currently available."""
    books = load_books()
    return [book for book in books if book["status"] == "Available"]


def get_issued_books():
    """Return a list of books that are currently issued."""
    books = load_books()
    return [book for book in books if book["status"] == "Issued"]


def get_statistics():
    """
    Return basic library statistics as a dictionary.
    Shows total, available, and issued book counts.
    """
    books = load_books()
    total = len(books)
    available = sum(1 for book in books if book["status"] == "Available")
    issued = sum(1 for book in books if book["status"] == "Issued")

    return {
        "total": total,
        "available": available,
        "issued": issued
    }
