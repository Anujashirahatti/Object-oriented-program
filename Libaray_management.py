
class Library:
    def __init__(self):
        self.books = []

    def display_books(self):
        if self.books:
            print("Available books in the library:")
            for book in self.books:
                print(f"- {book}")
        else:
            print("No books are currently available in the library.")

    def lend_book(self, book_name):  
        if book_name in self.books:
            self.books.remove(book_name)  # Corrected variable
            print(f"You have borrowed '{book_name}'.")
        else:
            print(f"Sorry, '{book_name}' is not available in the library.")

    def add_book(self, book_name):
        self.books.append(book_name)
        print(f"'{book_name}' has been added to the library.")

    def return_book(self, book_name):
        self.books.append(book_name)  
        print(f"Thank you for returning '{book_name}'.")

library = Library()
library.add_book("Python Programming")
library.add_book("Data Structures")
library.add_book("Machine Learning")

library.display_books()

library.lend_book("Python Programming")

library.display_books()

library.return_book("Machine Learning")

library.display_books()
