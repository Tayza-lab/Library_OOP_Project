class Book:
    def __init__(self, book_id, title, author, copies=1):
        self.__book_id = book_id
        self.__title = title
        self.__author = author
        self.__copies = copies

    def get_book_id(self):
        return self.__book_id

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_copies(self):
        return self.__copies

    def borrow_book(self):
        if self.__copies > 0:
            self.__copies -= 1
            return True
        return False

    def return_book(self):
        self.__copies += 1

    def to_dict(self):
        return {
            "book_id": self.__book_id,
            "title": self.__title,
            "author": self.__author,
            "copies": self.__copies
        }

    @staticmethod
    def from_dict(data):
        return Book(data["book_id"], data["title"], data["author"], data["copies"])

    def __str__(self):
        return f"[{self.__book_id}] {self.__title} by {self.__author} (Copies: {self.__copies})"
