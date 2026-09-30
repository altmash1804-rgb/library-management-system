# tests/test_library.py
# Unit tests for the Library Management System.
# Tests cover adding, searching, issuing, returning, filtering, and statistics.

import unittest
import sys
import os

# Add the project root to the path so we can import library modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# We patch the storage so tests never touch the real books.json file
from unittest.mock import patch

import library


# ---------------------------------------------------------------------------
# Helper: a fresh list of sample books used by many tests
# ---------------------------------------------------------------------------

def sample_books():
    return [
        {"id": "B001", "title": "Python Basics", "author": "John Smith",
         "category": "Programming", "status": "Available"},
        {"id": "B002", "title": "Data Structures", "author": "Jane Doe",
         "category": "Computer Science", "status": "Available"},
        {"id": "B003", "title": "Introduction to Algorithms", "author": "John Smith",
         "category": "Computer Science", "status": "Issued"},
    ]


# ---------------------------------------------------------------------------
# Tests: Add Book
# ---------------------------------------------------------------------------

class TestAddBook(unittest.TestCase):

    def test_add_new_book_success(self):
        """Adding a book with a unique ID should succeed."""
        with patch("library.load_books", return_value=[]), \
             patch("library.save_books") as mock_save:
            success, msg = library.add_book("B001", "Python Basics", "John Smith", "Programming")
            self.assertTrue(success)
            self.assertIn("added successfully", msg)
            mock_save.assert_called_once()

    def test_add_book_duplicate_id(self):
        """Adding a book with an already existing ID should fail."""
        existing = [{"id": "B001", "title": "Python Basics", "author": "John Smith",
                     "category": "Programming", "status": "Available"}]
        with patch("library.load_books", return_value=existing), \
             patch("library.save_books") as mock_save:
            success, msg = library.add_book("B001", "Another Book", "Author", "Category")
            self.assertFalse(success)
            self.assertIn("already exists", msg)
            mock_save.assert_not_called()

    def test_add_book_duplicate_id_case_insensitive(self):
        """Duplicate ID check should be case-insensitive (b001 == B001)."""
        existing = [{"id": "B001", "title": "Python Basics", "author": "John Smith",
                     "category": "Programming", "status": "Available"}]
        with patch("library.load_books", return_value=existing), \
             patch("library.save_books") as mock_save:
            success, msg = library.add_book("b001", "Another Book", "Author", "Category")
            self.assertFalse(success)
            mock_save.assert_not_called()

    def test_add_book_stores_correct_data(self):
        """The saved book should have all the right fields and status Available."""
        with patch("library.load_books", return_value=[]), \
             patch("library.save_books") as mock_save:
            library.add_book("B010", "Clean Code", "Robert Martin", "Programming")
            saved_list = mock_save.call_args[0][0]
            book = saved_list[0]
            self.assertEqual(book["id"], "B010")
            self.assertEqual(book["title"], "Clean Code")
            self.assertEqual(book["author"], "Robert Martin")
            self.assertEqual(book["category"], "Programming")
            self.assertEqual(book["status"], "Available")


# ---------------------------------------------------------------------------
# Tests: Search Book
# ---------------------------------------------------------------------------

class TestSearchBook(unittest.TestCase):

    def test_search_by_title(self):
        """Searching by title keyword should return matching books."""
        with patch("library.load_books", return_value=sample_books()):
            results = library.search_books("Python")
            self.assertEqual(len(results), 1)
            self.assertEqual(results[0]["id"], "B001")

    def test_search_by_author(self):
        """Searching by author name should return all books by that author."""
        with patch("library.load_books", return_value=sample_books()):
            results = library.search_books("John Smith")
            self.assertEqual(len(results), 2)

    def test_search_by_book_id(self):
        """Searching by exact Book ID should return the correct book."""
        with patch("library.load_books", return_value=sample_books()):
            results = library.search_books("B002")
            self.assertEqual(len(results), 1)
            self.assertEqual(results[0]["title"], "Data Structures")

    def test_search_case_insensitive(self):
        """Search should work regardless of uppercase or lowercase input."""
        with patch("library.load_books", return_value=sample_books()):
            results = library.search_books("python basics")
            self.assertEqual(len(results), 1)

    def test_search_partial_match(self):
        """A partial keyword should still find matching books."""
        with patch("library.load_books", return_value=sample_books()):
            results = library.search_books("data")
            self.assertEqual(len(results), 1)
            self.assertEqual(results[0]["id"], "B002")

    def test_search_no_results(self):
        """A search with no matches should return an empty list."""
        with patch("library.load_books", return_value=sample_books()):
            results = library.search_books("NONEXISTENT")
            self.assertEqual(len(results), 0)


# ---------------------------------------------------------------------------
# Tests: Issue Book
# ---------------------------------------------------------------------------

class TestIssueBook(unittest.TestCase):

    def test_issue_available_book(self):
        """Issuing an available book should succeed and change its status."""
        books = sample_books()
        with patch("library.load_books", return_value=books), \
             patch("library.save_books") as mock_save:
            success, msg = library.issue_book("B001")
            self.assertTrue(success)
            self.assertIn("issued successfully", msg)
            mock_save.assert_called_once()

    def test_issue_already_issued_book(self):
        """Issuing a book that is already issued should fail."""
        books = sample_books()
        with patch("library.load_books", return_value=books), \
             patch("library.save_books") as mock_save:
            # B003 is already Issued in sample_books()
            success, msg = library.issue_book("B003")
            self.assertFalse(success)
            self.assertIn("already issued", msg)
            mock_save.assert_not_called()

    def test_issue_nonexistent_book(self):
        """Issuing a Book ID that doesn't exist should return a failure message."""
        with patch("library.load_books", return_value=sample_books()), \
             patch("library.save_books") as mock_save:
            success, msg = library.issue_book("B999")
            self.assertFalse(success)
            self.assertIn("not found", msg)
            mock_save.assert_not_called()

    def test_issue_book_updates_status(self):
        """After issuing, the book's status in the saved data should be 'Issued'."""
        books = sample_books()
        with patch("library.load_books", return_value=books), \
             patch("library.save_books") as mock_save:
            library.issue_book("B001")
            saved_books = mock_save.call_args[0][0]
            b001 = next(b for b in saved_books if b["id"] == "B001")
            self.assertEqual(b001["status"], "Issued")


# ---------------------------------------------------------------------------
# Tests: Return Book
# ---------------------------------------------------------------------------

class TestReturnBook(unittest.TestCase):

    def test_return_issued_book(self):
        """Returning an issued book should succeed and change its status."""
        books = sample_books()
        with patch("library.load_books", return_value=books), \
             patch("library.save_books") as mock_save:
            # B003 is Issued
            success, msg = library.return_book("B003")
            self.assertTrue(success)
            self.assertIn("returned successfully", msg)
            mock_save.assert_called_once()

    def test_return_already_available_book(self):
        """Returning a book that is already available should fail."""
        books = sample_books()
        with patch("library.load_books", return_value=books), \
             patch("library.save_books") as mock_save:
            # B001 is Available
            success, msg = library.return_book("B001")
            self.assertFalse(success)
            self.assertIn("already available", msg)
            mock_save.assert_not_called()

    def test_return_nonexistent_book(self):
        """Returning a Book ID that doesn't exist should fail."""
        with patch("library.load_books", return_value=sample_books()), \
             patch("library.save_books") as mock_save:
            success, msg = library.return_book("B999")
            self.assertFalse(success)
            self.assertIn("not found", msg)
            mock_save.assert_not_called()

    def test_return_book_updates_status(self):
        """After returning, the book's status in the saved data should be 'Available'."""
        books = sample_books()
        with patch("library.load_books", return_value=books), \
             patch("library.save_books") as mock_save:
            library.return_book("B003")
            saved_books = mock_save.call_args[0][0]
            b003 = next(b for b in saved_books if b["id"] == "B003")
            self.assertEqual(b003["status"], "Available")


# ---------------------------------------------------------------------------
# Tests: Filter - Available and Issued Books
# ---------------------------------------------------------------------------

class TestFilterBooks(unittest.TestCase):

    def test_get_available_books(self):
        """get_available_books should return only books with status Available."""
        with patch("library.load_books", return_value=sample_books()):
            available = library.get_available_books()
            self.assertEqual(len(available), 2)
            for book in available:
                self.assertEqual(book["status"], "Available")

    def test_get_issued_books(self):
        """get_issued_books should return only books with status Issued."""
        with patch("library.load_books", return_value=sample_books()):
            issued = library.get_issued_books()
            self.assertEqual(len(issued), 1)
            self.assertEqual(issued[0]["id"], "B003")

    def test_available_books_empty_library(self):
        """get_available_books on an empty library should return an empty list."""
        with patch("library.load_books", return_value=[]):
            self.assertEqual(library.get_available_books(), [])

    def test_issued_books_empty_library(self):
        """get_issued_books on an empty library should return an empty list."""
        with patch("library.load_books", return_value=[]):
            self.assertEqual(library.get_issued_books(), [])


# ---------------------------------------------------------------------------
# Tests: Statistics
# ---------------------------------------------------------------------------

class TestStatistics(unittest.TestCase):

    def test_statistics_correct_counts(self):
        """Statistics should correctly count total, available, and issued books."""
        with patch("library.load_books", return_value=sample_books()):
            stats = library.get_statistics()
            self.assertEqual(stats["total"], 3)
            self.assertEqual(stats["available"], 2)
            self.assertEqual(stats["issued"], 1)

    def test_statistics_empty_library(self):
        """Statistics for an empty library should show all zeros."""
        with patch("library.load_books", return_value=[]):
            stats = library.get_statistics()
            self.assertEqual(stats["total"], 0)
            self.assertEqual(stats["available"], 0)
            self.assertEqual(stats["issued"], 0)

    def test_statistics_all_issued(self):
        """If all books are issued, available count should be 0."""
        all_issued = [
            {"id": "B001", "title": "Book A", "author": "Author A",
             "category": "Cat", "status": "Issued"},
            {"id": "B002", "title": "Book B", "author": "Author B",
             "category": "Cat", "status": "Issued"},
        ]
        with patch("library.load_books", return_value=all_issued):
            stats = library.get_statistics()
            self.assertEqual(stats["total"], 2)
            self.assertEqual(stats["available"], 0)
            self.assertEqual(stats["issued"], 2)


if __name__ == "__main__":
    unittest.main()
