class Book:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year

    def __str__(self):
        return f"'{self.title}' by {self.author} ({self.publication_year})"


# Derived Class: PrintBook
class PrintBook(Book):
    def __init__(self, title, author, publication_year, pages):
        super().__init__(title, author, publication_year)
        self.pages = pages

    def __str__(self):
        return f"Print Book: {super().__str__()} - {self.pages} pages"


# Derived Class: EBook
class EBook(Book):
    def __init__(self, title, author, publication_year, file_size_mb):
        super().__init__(title, author, publication_year)
        self.file_size_mb = file_size_mb

    def __str__(self):
        return f"E-Book: {super().__str__()} - {self.file_size_mb}MB"
