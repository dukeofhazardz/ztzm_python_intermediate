from turtle import title


class LibraryItem:
    def __init__(self, title, author):
        self.__title = title
        self.__author = author

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_info(self):
        return f"Title: {self.__title}, Author: {self.__author}"


class Book(LibraryItem):
    def __init__(self, title, author, pages):
        super().__init__(title, author)
        self.pages = pages

    def get_info(self):
        return f"{super().get_info()}, Pages: {self.pages}"


class DVD(LibraryItem):
    def __init__(self, title, author, duration):
        super().__init__(title, author)
        self.duration = duration

    def get_info(self):
        return f"{super().get_info()}, Duration: {self.duration} mins"

items = [
    Book("Python Basics", "John Doe", 350),
    DVD("Learning Python", "Jane Smith", 90)
]

for item in items:
    print(item.get_info())