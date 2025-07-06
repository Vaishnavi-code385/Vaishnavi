class Book:
    def __init__(self, title, author, book_id):
        self.title = title
        self.author = author
        self.book_id = book_id
        self.available = True

    def __str__(self):
        status = "Available" if self.available else "Not Available"
        return f"{self.book_id} - {self.title} by {self.author} [{status}]"


class library:
    def __init__(self):
        self.books = []
        self.librarians = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to the library.")


    def borrow_book(self, book_id):
        for book in self.books:
            
                    return
                else:
                    print("Book is currently not available.")
                    return
        print("Book not found.")

    def return_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if not book.available:
                    book.available = True
                    print(f"Book '{book.title}' returned successfully.")
                    return
                else:
                    print("Book was not borrowed.")
                    return
        print("Book not found.")

    def search_book(self, keyword):
        found = False
        print(f"Search results for '{keyword}':")
        for book in self.books:
            if keyword.lower() in book.title.lower() or keyword.lower() in book.author.lower():
                print(book)
                found = True
        if not found:
            print("No matching books found.")

    def total_books(self):
        return len(self.books)

    def borrowed_books_count(self):
        return sum(not book.available for book in self.books)

    def available_books_count(self):
        return sum(book.available for book in self.books)

    def add_librarian(self, name):
        self.librarians.append(name)

    def total_librarians(self):
        return len(self.librarians)



library = Library()


library.add_librarian("A")
library.add_librarian("B")


library.add_book(Book(" Programming Python ", "Mark Lutz", 101))
library.add_book(Book(" Introduction to Python Programming ", "", 102))
library.add_book(Book("Deep Learning with Python ", "François Chollet", 103))


library.borrow_book(101)
library.borrow_book(101)  
library.return_book(101)


library.search_book("Deep learning with python")


print("\n Summary")
print("Total Books:", library.total_books())
print("Borrowed Books:", library.borrowed_books_count())
print("Available Books:", library.available_books_count())
print("Total Librarians:", library.total_librarians())
