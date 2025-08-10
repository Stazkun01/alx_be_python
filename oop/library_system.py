# library_system.py

class Book:
    def __init__(self, title: str, author: str):
        """Initialize the book with title and author."""
        self.title = title
        self.author = author

    def __str__(self):
        """Return a human-readable representation of the book."""
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    def __init__(self, title: str, author: str, file_size: int):
        """
        Initialize the eBook.
        :param file_size: size in KB
        """
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        """Return a human-readable representation of the eBook."""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    def __init__(self, title: str, author: str, page_count: int):
        """
        Initialize the print book.
        :param page_count: number of pages
        """
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        """Return a human-readable representation of the print book."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    def __init__(self):
        """Initialize the library with an empty book list."""
        self.books = []

    def add_book(self, book: Book):
        """Add a book instance (Book, EBook, or PrintBook) to the library."""
        self.books.append(book)

    def list_books(self):
        """Print details of all books in the library."""
        for book in self.books:
            print(book)
