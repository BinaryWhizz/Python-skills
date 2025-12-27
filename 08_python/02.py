# Problems 

# Imagine you are managing a small library and need a system to track books and their availability. Each book has details like the title, author, and availability status (whether it's borrowed or not). You want to build a system that allows:

# 1) Adding books to the library.
# 2) Checking if a book is available.
# 3) Borrowing a book (marking it as borrowed).
# 4) Returning a book (marking it as available).
# 5) You will solve this using classes and objects.

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def check_availability(self):
        if self.available:
            print(f"'{self.title}' is available.")
        else:
            print(f"'{self.title}' is currently borrowed.")

    def borrow_book(self):
        if self.available:
            self.available = False
            print(f"You have borrowed '{self.title}'.")
        else:
            print(f"'{self.title}' is already borrowed.")

    def return_book(self):
        if not self.available:
            self.available = True
            print(f"You have returned '{self.title}'.")
        else:
            print(f"'{self.title}' was not borrowed.")


library = Book("To kill a Mockingbird", "Harper Lee")

# Check print statement step by step 

print(library.check_availability())
print(library.borrow())
print(library.check_availability())
print(library.return_book())
print(library.check_availability())
print(library.return_book())
