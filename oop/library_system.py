# Base Class
class Book:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year

    def __str__(self):
        return f"'{self.title}' by {self.author} ({self.publication_year})"

# Derived Class: PrintBook
class PrintBook(Book):
    def __init__(self, title, author, publication_year, page_count):
        super().__init__(title, author, publication_year)
        self.page_count = page_count

    def __str__(self):
        return f"Print Book: {super().__str__()} - {self.page_count} pages"

# Derived Class: EBook
class EBook(Book):
    def __init__(self, title, author, publication_year, file_size_mb):
        super().__init__(title, author, publication_year)
        self.file_size_mb = file_size_mb

    def __str__(self):
        return f"E-Book: {super().__str__()} - {self.file_size_mb}MB"


# New Class: Library
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        if not self.books:
            print("The library has no books.")
        else:
            print("Books in the Library:")
            for book in self.books:
                print(book)  # This will call the __str__ method of each Book
