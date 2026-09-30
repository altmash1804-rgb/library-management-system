# Library Management System

A simple command-line Library Management System built with Python 3 for a first-year Python Essentials college project.

---

## Project Description

This project allows a user to manage books in a library through a text-based menu in the terminal. The user can add books, search for them, issue and return them, and view basic statistics. All data is saved locally in a JSON file so it persists between sessions.

---

## Objectives

- Demonstrate basic Python programming concepts
- Build a working CLI application using only the Python Standard Library
- Practice file handling, functions, dictionaries, lists, and exception handling
- Write unit tests using the `unittest` module

---

## Features

1. Add a new book
2. View all books
3. Search books by ID, title, or author
4. Issue a book
5. Return a book
6. View available books
7. View issued books
8. View library statistics (total, available, issued)
9. Exit the program

---

## Technologies Used

- Python 3
- Python Standard Library only (`json`, `os`, `unittest`, `unittest.mock`)
- Command Line Interface (CLI)
- JSON file for local data storage

No external packages, no GUI, no database, no internet connection required.

---

## Project Structure

```
library-management-system/
│
├── main.py           # Entry point - runs the menu
├── library.py        # All library operations (add, search, issue, return, stats)
├── storage.py        # Load and save data using JSON
├── validators.py     # Simple input validation functions
├── utils.py          # Helper display functions
├── README.md         # This file
├── statement.md      # Problem statement
├── requirements.txt  # No external dependencies
├── .gitignore        # Python generated files to ignore
│
├── data/
│   └── books.json    # Local storage for book data
│
└── tests/
    ├── __init__.py
    └── test_library.py   # Unit tests
```

---

## Requirements

- Python 3.6 or newer
- No external packages needed

---

## Installation / Setup

1. Download or clone the project folder.
2. Make sure Python 3 is installed on your computer.
3. No additional installation steps are needed.

To check your Python version:

```bash
python --version
```

---

## How to Run

Open a terminal in the project folder and run:

```bash
python main.py
```

The main menu will appear in the terminal.

---

## How to Use the Menu

```
========================================
       LIBRARY MANAGEMENT SYSTEM
========================================
  1. Add Book
  2. View All Books
  3. Search Book
  4. Issue Book
  5. Return Book
  6. View Available Books
  7. View Issued Books
  8. Library Statistics
  9. Exit
========================================
```

Type a number (1 to 9) and press **Enter** to choose an option.

- The menu keeps showing until you choose **9. Exit**.
- If you type something that is not a valid option, the program shows a message and asks again.

---

## Testing Instructions

Run all unit tests with verbose output:

```bash
python -m unittest discover -s tests -v
```

Check that all Python files compile without errors:

```bash
python -m py_compile main.py library.py storage.py validators.py utils.py
```

---

## Example Usage

**Adding a book:**

```
Enter your choice (1-9): 1

--- Add New Book ---
Enter Book ID (e.g., B001): B006
Enter Title: The C Programming Language
Enter Author: Brian Kernighan
Enter Category: Programming
Book 'The C Programming Language' added successfully!
```

**Searching for a book:**

```
Enter your choice (1-9): 3

--- Search Book ---
Enter search keyword (ID, Title, or Author): python

Found 1 result(s):
--------------------------------------------------
  [1]
  Book ID  : B001
  Title    : Python Basics
  Author   : John Smith
  Category : Programming
  Status   : Available
--------------------------------------------------
```

**Viewing statistics:**

```
Enter your choice (1-9): 8

--- Library Statistics ---
--------------------------------------------------
  Total Books     : 5
  Available Books : 4
  Issued Books    : 1
--------------------------------------------------
```
