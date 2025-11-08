class Member:
    def __init__(self, member_id, name):
        self.__member_id = member_id
        self.__name = name
        self.__borrowed_books = []

    def get_member_id(self):
        return self.__member_id

    def get_name(self):
        return self.__name

    def borrow_book(self, book):
        self.__borrowed_books.append(book)

    def return_book(self, book):
        if book in self.__borrowed_books:
            self.__borrowed_books.remove(book)

    def list_borrowed_books(self):
        if not self.__borrowed_books:
            return "No books borrowed."
        return "\n".join([str(book) for book in self.__borrowed_books])

    def __str__(self):
        return f"{self.__member_id} - {self.__name}"
