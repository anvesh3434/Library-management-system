class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def __str__(self):
        return f"'{self.title}' by {self.author} (Borrowed: {self.is_borrowed})"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to the library.")

    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                print(f"Book '{title}' removed from the library.")
                return
        print(f"Book '{title}' not found in the library.")

    def display_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            print("Books in the library:")
            for book in self.books:
                print(book)

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title:
                if book.is_borrowed:
                    print(f"Book '{title}' is already borrowed.")
                else:
                    book.is_borrowed = True
                    print(f"You have borrowed '{title}'.")
                return
        print(f"Book '{title}' not found in the library.")

    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                if book.is_borrowed:
                    book.is_borrowed = False
                    print(f"You have returned '{title}'.")
                else:
                    print(f"Book '{title}' was not borrowed.")
                return
        print(f"Book '{title}' not found in the library.")


def main():
    library = Library()

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Display Books")
        print("4. Borrow Book")
        print("5. Return Book")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            book = Book(title, author)
            library.add_book(book)
        elif choice == '2':
            title = input("Enter book title to remove: ")
            library.remove_book(title)
        elif choice == '3':
            library.display_books()
        elif choice == '4':
            title = input("Enter book title to borrow: ")
            library.borrow_book(title)
        elif choice == '5':
            title = input("Enter book title to return: ")
            library.return_book(title)
        elif choice == '6':
            print("Exiting the Library Management System.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
