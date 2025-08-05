from book_class import Book

def main():
    # Creating an instance of Book
    my_book = Book("1984", "George Orwell", 1949)

    # Demonstrating the __str__ method
    print(my_book)

    # Demonstrating the __repr__ method
    print(repr(my_book))

    # Deleting a book instance to trigger __del__
    del my_book

if __name__ == "__main__":
    main()
    
from books import Book, EBook, PrintBook

def main():
    classic_book = Book("Pride and Prejudice", "Jane Austen", 1813)
    classic_book.display()

    ebook = EBook("Snow Crash", "Neal Stephenson", 1992, "500KB")
    ebook.display()

    print_book = PrintBook("The Catcher in the Rye", "J.D. Salinger", 1951, 234)
    print_book.display()

if __name__ == "__main__":
    main()

from polymorphism_demo import Shape, Rectangle, Circle

def main():
    shapes = [
        Rectangle(10, 5),
        Circle(7)
    ]

    for shape in shapes:
        print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")

if __name__ == "__main__":
    main()
