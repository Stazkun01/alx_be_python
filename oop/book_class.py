# book_class.py

class Book:
    def __init__(self, title: str, author: str, year: int):
        """Initialize the Book instance with title, author, and publication year."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor: prints a message when the object is deleted."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """Informal string representation of the book."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Official string representation of the book, for debugging."""
        return f"Book('{self.title}', '{self.author}', {self.year})"
