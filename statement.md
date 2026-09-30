# Problem Statement

## Library Management System

### Problem Statement

Libraries need a simple way to keep track of their books. Without any system, it is easy to lose track of which books are available, which are issued, and to whom. Managing books manually on paper is slow and prone to errors.

This project solves that problem by providing a simple terminal-based system where a librarian or student can manage books quickly and efficiently using a computer.

---

### Scope

This system is limited to:

- Managing a collection of books stored locally on one computer
- Adding new books to the system
- Viewing all books or filtering by availability
- Searching for books by title, author, or Book ID
- Issuing books (marking them as unavailable)
- Returning books (marking them as available again)
- Displaying basic statistics about the library
- Saving all data to a local JSON file so it is not lost when the program closes

This system does **not** include:

- User accounts or login
- Multiple librarians
- Reservation or waiting lists
- Fine calculation
- Networking or cloud features
- A graphical interface

---

### Target Users

- First-year computer science or IT students learning Python
- A single librarian or lab assistant managing a small book collection
- Anyone who needs a simple local book tracking tool

---

### High Level Features

| Feature               | Description                                        |
|-----------------------|----------------------------------------------------|
| Add Book              | Add a new book with ID, title, author, and category |
| View All Books        | Display the full list of books                     |
| Search Book           | Find books by keyword in ID, title, or author      |
| Issue Book            | Mark a book as issued (unavailable)                |
| Return Book           | Mark a book as available again                     |
| View Available Books  | Show only books that are currently available        |
| View Issued Books     | Show only books that are currently issued           |
| Library Statistics    | Show total, available, and issued book counts       |
| Data Persistence      | Save and load data automatically using a JSON file  |
