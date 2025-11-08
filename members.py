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
        self.__borrowed_books.append(book.get_book_id())

    def return_book(self, book):
        if book.get_book_id() in self.__borrowed_books:
            self.__borrowed_books.remove(book.get_book_id())

    def list_borrowed_books(self):
        if not self.__borrowed_books:
            return "No books borrowed."
        return ", ".join(self.__borrowed_books)

    def to_dict(self):
        return {
            "member_id": self.__member_id,
            "name": self.__name,
            "borrowed_books": self.__borrowed_books
        }

    @staticmethod
    def from_dict(data):
        member = Member(data["member_id"], data["name"])
        member.__borrowed_books = data.get("borrowed_books", [])
        return member

    def __str__(self):
        return f"{self.__member_id} - {self.__name}"
