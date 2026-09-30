# utils.py
# Small helper functions used across the project.


def print_separator():
    """Print a simple line separator for readability."""
    print("-" * 50)


def print_book(book):
    """
    Display a single book's details in a readable format.
    Takes a book dictionary and prints each field on its own line.
    """
    print(f"  Book ID  : {book['id']}")
    print(f"  Title    : {book['title']}")
    print(f"  Author   : {book['author']}")
    print(f"  Category : {book['category']}")
    print(f"  Status   : {book['status']}")


def print_book_list(books):
    """
    Display a list of books.
    Each book is separated by a line for easy reading.
    """
    for i, book in enumerate(books, start=1):
        print(f"\n  [{i}]")
        print_book(book)
        print_separator()
