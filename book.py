import json

book_list=[ 
 {"book1_name":"programmimg python","Author":"Mark Lutz","book_id":"1" },
 {"book2_name":" Introduction to Python Programming","Author":"Guido van Rossum","book_id":"2"},
 {"book3_name":"Deep Learning with Python","Author":"François Chollet","book_id":"3"}   
]
search_book = input("Enter the book name:")

if (book_list)==search_book:
    print("book is available")

else:
    print("book is not available")



class Book:    
 def __init__(self, title, author, book_id):
        self.title = title
        self.author = author
        self.book_id = book_id
    
class library:
 
 def search_book(self, title):
      found = False
      for book in self.books:
         if self.title in book["title"]:
                print(f"Book found: {book['title']} by {book['author']}")
                found = True
                break
         if not found:
            print("Book not found.")
 
def __init__(self):
        self.books = book_list
        self.librarians = []

def add_librarian(self, name):
    self.librarians.append(name)

def add_book(self, title, author, book_id):
    new_book = Book(title, author, book_id)
    self.books.append(new_book)


library. add_book
[
 {"book1_name":"programmimg python","Author":"Mark Lutz","book_id":"1" },
 {"book2_name":" Introduction to Python Programming","Author":"Guido van Rossum","book_id":"2"},
 {"book3_name":"Deep Learning with Python","Author":"François Chollet","book_id":"3"}   
]

def borrow_book(self,book_id):
    for book in book_list:
     if book.book_id == book_id:
                if book.available:
                    book.available = False
                    print(f"You have borrowed '{book.title}'.")

def return_book(self,book_id):
      for book in book_list:
       if book.book_id==book_id:
            if book.available:
                  book.available=True
                  print(f"Book '{book.title}' returned successfully.")

lib = library()
search_book = input("Enter the book name:")
lib.search_book(search_book) 

lib.borrow_book("2")
lib.borrow_book("2")
lib.return_book("2")








