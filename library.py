from models.book import Book
from models.member import Member

class Library:
    def __init__(self, name):
        self.name = name
        self.books = {}
        self.members = {}

    def add_book(self, book):
        self.books[book.get_book_id()] = book

    def register_member(self, member):
        self.members[member.get_member_id()] = member

    def borrow_book(self, member_id, book_id):
        member = self.members.get(member_id)
        book = self.books.get(book_id)
        if not member:
            return "Member not found!"
        if not book:
            return "Book not found!"
        if book.borrow_book():
            member.borrow_book(book)
            return f"{member.get_name()} borrowed '{book.get_title()}'"
        return "No copies available."

    def return_book(self, member_id, book_id):
        member = self.members.get(member_id)
        book = self.books.get(book_id)
        if not member or not book:
            return "Invalid member or book."
        member.return_book(book)
        book.return_book()
        return f"{member.get_name()} returned '{book.get_title()}'"
