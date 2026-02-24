import json
import os

FILE_NAME = "library.json"


class Book:
    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "copies": self.copies
        }

    @staticmethod
    def from_dict(data):
        return Book(data["title"], data["author"], data["copies"])


class Library:
    def __init__(self):
        self.books = []
        self.load_books()

    def load_books(self):
        if os.path.exists(FILE_NAME):
            with open(FILE_NAME, "r") as file:
                data = json.load(file)
                self.books = [Book.from_dict(book) for book in data]

    def save_books(self):
        with open(FILE_NAME, "w") as file:
            json.dump([book.to_dict() for book in self.books], file, indent=4)

    def add_book(self):
        print("> Add Book")
        title = input("Title: ")
        author = input("Author: ")
        copies = int(input("Copies: "))

        new_book = Book(title, author, copies)
        self.books.append(new_book)
        self.save_books()

        print("Book added to library.\n")

    def remove_book(self):
        title = input("Enter title to remove: ")
        for book in self.books:
            if book.title.lower() == title.lower():
                self.books.remove(book)
                self.save_books()
                print("Book removed from library.\n")
                return
        print("Book not found.\n")

    def view_books(self):
        if not self.books:
            print("Library is empty.\n")
            return

        print("\nLibrary Inventory:")
        for book in self.books:
            print(f"{book.title} by {book.author} | Copies: {book.copies}")
        print()


def main():
    library = Library()

    while True:
        print("1. Add Book")
        print("2. Remove Book")
        print("3. View Books")
        print("4. Exit\n")

        choice = input("Choose an option: ")

        if choice == "1":
            library.add_book()
        elif choice == "2":
            library.remove_book()
        elif choice == "3":
            library.view_books()
        elif choice == "4":
            print("Exiting Library System.")
            break
        else:
            print("Invalid option.\n")


if __name__ == "__main__":
    main()