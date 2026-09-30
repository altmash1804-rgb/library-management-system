# main.py
# Entry point of the Library Management System.
# Displays the menu and calls the appropriate library functions.

import library
from validators import is_valid_input, is_valid_book_id_format
from utils import print_separator, print_book, print_book_list


def show_menu():
    """Print the main menu options to the screen."""
    print("\n========================================")
    print("       LIBRARY MANAGEMENT SYSTEM")
    print("========================================")
    print("  1. Add Book")
    print("  2. View All Books")
    print("  3. Search Book")
    print("  4. Issue Book")
    print("  5. Return Book")
    print("  6. View Available Books")
    print("  7. View Issued Books")
    print("  8. Library Statistics")
    print("  9. Exit")
    print("========================================")


def add_book_menu():
    """Collect book details from the user and add the book."""
    print("\n--- Add New Book ---")

    # Collect and validate each field
    book_id = input("Enter Book ID (e.g., B001): ").strip()
    if not is_valid_book_id_format(book_id):
        print("Book ID cannot be empty.")
        return

    title = input("Enter Title: ").strip()
    if not is_valid_input(title):
        print("Title cannot be empty.")
        return

    author = input("Enter Author: ").strip()
    if not is_valid_input(author):
        print("Author cannot be empty.")
        return

    category = input("Enter Category: ").strip()
    if not is_valid_input(category):
        print("Category cannot be empty.")
        return

    # Try to add the book and show the result
    success, message = library.add_book(book_id, title, author, category)
    print(message)


def view_all_books_menu():
    """Display every book in the library."""
    print("\n--- All Books ---")
    books = library.get_all_books()

    if not books:
        print("No books found.")
        return

    print_separator()
    print_book_list(books)


def search_book_menu():
    """Search for books by ID, title, or author."""
    print("\n--- Search Book ---")
    keyword = input("Enter search keyword (ID, Title, or Author): ").strip()

    if not is_valid_input(keyword):
        print("Search keyword cannot be empty.")
        return

    results = library.search_books(keyword)

    if not results:
        print(f"No books found matching '{keyword}'.")
        return

    print(f"\nFound {len(results)} result(s):")
    print_separator()
    print_book_list(results)


def issue_book_menu():
    """Issue a book to a user by its Book ID."""
    print("\n--- Issue Book ---")
    book_id = input("Enter Book ID to issue: ").strip()

    if not is_valid_book_id_format(book_id):
        print("Book ID cannot be empty.")
        return

    success, message = library.issue_book(book_id)
    print(message)


def return_book_menu():
    """Return a previously issued book by its Book ID."""
    print("\n--- Return Book ---")
    book_id = input("Enter Book ID to return: ").strip()

    if not is_valid_book_id_format(book_id):
        print("Book ID cannot be empty.")
        return

    success, message = library.return_book(book_id)
    print(message)


def view_available_books_menu():
    """Display only the books that are currently available."""
    print("\n--- Available Books ---")
    books = library.get_available_books()

    if not books:
        print("No available books at the moment.")
        return

    print_separator()
    print_book_list(books)


def view_issued_books_menu():
    """Display only the books that are currently issued."""
    print("\n--- Issued Books ---")
    books = library.get_issued_books()

    if not books:
        print("No books are currently issued.")
        return

    print_separator()
    print_book_list(books)


def show_statistics_menu():
    """Display simple counts: total, available, and issued books."""
    print("\n--- Library Statistics ---")
    stats = library.get_statistics()
    print_separator()
    print(f"  Total Books     : {stats['total']}")
    print(f"  Available Books : {stats['available']}")
    print(f"  Issued Books    : {stats['issued']}")
    print_separator()


def main():
    """
    Main loop. Keep showing the menu until the user chooses to exit.
    Invalid input is caught and a helpful message is shown.
    """
    print("Welcome to the Library Management System!")

    while True:
        show_menu()
        choice = input("Enter your choice (1-9): ").strip()

        if choice == "1":
            add_book_menu()
        elif choice == "2":
            view_all_books_menu()
        elif choice == "3":
            search_book_menu()
        elif choice == "4":
            issue_book_menu()
        elif choice == "5":
            return_book_menu()
        elif choice == "6":
            view_available_books_menu()
        elif choice == "7":
            view_issued_books_menu()
        elif choice == "8":
            show_statistics_menu()
        elif choice == "9":
            print("\nThank you for using the Library Management System. Goodbye!")
            break
        else:
            # Handle any input that isn't a valid menu option
            print("Invalid choice. Please enter a number between 1 and 9.")


# Run the program only when this file is executed directly
if __name__ == "__main__":
    main()
