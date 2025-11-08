import tkinter as tk
from tkinter import ttk, messagebox
from models.library import Library
from models.book import Book
from models.member import Member

# ---------- Color Theme ----------
BG_COLOR = "#F5F6FA"
HEADER_COLOR = "#273C75"
BUTTON_COLOR = "#40739E"
TEXT_COLOR = "white"
ACCENT_COLOR = "#9C88FF"

class LibraryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("📚 Library Management System")
        self.root.geometry("850x600")
        self.root.configure(bg=BG_COLOR)
        self.library = Library("University Library")

        self.style = ttk.Style()
        self.set_theme()
        self.create_header()
        self.create_tabs()

    # ---------- THEME ----------
    def set_theme(self):
        self.style.theme_use("clam")

        self.style.configure(
            "TNotebook",
            background=BG_COLOR,
            borderwidth=0
        )

        self.style.configure(
            "TNotebook.Tab",
            font=("Segoe UI", 11, "bold"),
            padding=[15, 8],
            background=ACCENT_COLOR,
            foreground=TEXT_COLOR
        )

        self.style.map(
            "TNotebook.Tab",
            background=[("selected", HEADER_COLOR)],
            foreground=[("selected", "white")]
        )

        self.style.configure(
            "TButton",
            font=("Segoe UI", 10, "bold"),
            background=BUTTON_COLOR,
            foreground=TEXT_COLOR,
            borderwidth=0,
            padding=6
        )

        self.style.map(
            "TButton",
            background=[("active", ACCENT_COLOR)]
        )

    # ---------- HEADER ----------
    def create_header(self):
        header = tk.Frame(self.root, bg=HEADER_COLOR, height=70)
        header.pack(fill="x")

        title = tk.Label(
            header,
            text="📚 Library Management System",
            bg=HEADER_COLOR,
            fg="white",
            font=("Segoe UI", 20, "bold")
        )
        title.pack(pady=10)

    # ---------- TABS ----------
    def create_tabs(self):
        notebook = ttk.Notebook(self.root)
        notebook.pack(fill="both", expand=True, padx=10, pady=10)

        self.tab_books = ttk.Frame(notebook)
        self.tab_members = ttk.Frame(notebook)
        self.tab_borrow = ttk.Frame(notebook)

        notebook.add(self.tab_books, text="📖 Books")
        notebook.add(self.tab_members, text="👥 Members")
        notebook.add(self.tab_borrow, text="🔄 Borrow / Return")

        self.create_books_tab()
        self.create_members_tab()
        self.create_borrow_tab()

    # ---------- BOOKS TAB ----------
    def create_books_tab(self):
        frame = self.tab_books
        frame.configure(padding=20)

        tk.Label(frame, text="Add a New Book", font=("Segoe UI", 13, "bold")).grid(row=0, column=0, columnspan=2, pady=10)

        labels = ["Book ID:", "Title:", "Author:", "Copies:"]
        self.book_entries = {}

        for i, label_text in enumerate(labels):
            tk.Label(frame, text=label_text, font=("Segoe UI", 10)).grid(row=i+1, column=0, sticky="e", padx=5, pady=5)
            entry = ttk.Entry(frame, width=30)
            entry.grid(row=i+1, column=1, padx=5, pady=5)
            self.book_entries[label_text] = entry

        ttk.Button(frame, text="➕ Add Book", command=self.add_book).grid(row=5, column=0, columnspan=2, pady=10)

        ttk.Separator(frame, orient="horizontal").grid(row=6, column=0, columnspan=2, sticky="ew", pady=10)

        tk.Label(frame, text="📚 Available Books", font=("Segoe UI", 13, "bold")).grid(row=7, column=0, columnspan=2, pady=5)

        self.book_list = tk.Listbox(frame, width=60, height=10, font=("Consolas", 10))
        self.book_list.grid(row=8, column=0, columnspan=2, pady=10)
        self.refresh_books()

    def add_book(self):
        bid = self.book_entries["Book ID:"].get()
        title = self.book_entries["Title:"].get()
        author = self.book_entries["Author:"].get()
        copies = int(self.book_entries["Copies:"].get() or 1)

        if not bid or not title or not author:
            messagebox.showerror("Error", "All fields are required!")
            return

        self.library.add_book(Book(bid, title, author, copies))
        self.refresh_books()
        messagebox.showinfo("Success", f"Book '{title}' added successfully!")

    def refresh_books(self):
        self.book_list.delete(0, tk.END)
        for book in self.library.books.values():
            self.book_list.insert(tk.END, str(book))

    # ---------- MEMBERS TAB ----------
    def create_members_tab(self):
        frame = self.tab_members
        frame.configure(padding=20)

        tk.Label(frame, text="Register New Member", font=("Segoe UI", 13, "bold")).grid(row=0, column=0, columnspan=2, pady=10)

        tk.Label(frame, text="Member ID:", font=("Segoe UI", 10)).grid(row=1, column=0, sticky="e", padx=5, pady=5)
        tk.Label(frame, text="Name:", font=("Segoe UI", 10)).grid(row=2, column=0, sticky="e", padx=5, pady=5)

        self.member_id = ttk.Entry(frame, width=30)
        self.member_name = ttk.Entry(frame, width=30)
        self.member_id.grid(row=1, column=1, padx=5, pady=5)
        self.member_name.grid(row=2, column=1, padx=5, pady=5)

        ttk.Button(frame, text="👤 Register Member", command=self.register_member).grid(row=3, column=0, columnspan=2, pady=10)

        ttk.Separator(frame, orient="horizontal").grid(row=4, column=0, columnspan=2, sticky="ew", pady=10)

        tk.Label(frame, text="👥 Registered Members", font=("Segoe UI", 13, "bold")).grid(row=5, column=0, columnspan=2, pady=5)

        self.member_list = tk.Listbox(frame, width=60, height=10, font=("Consolas", 10))
        self.member_list.grid(row=6, column=0, columnspan=2, pady=10)
        self.refresh_members()

    def register_member(self):
        mid = self.member_id.get()
        name = self.member_name.get()

        if not mid or not name:
            messagebox.showerror("Error", "Both fields are required!")
            return

        self.library.register_member(Member(mid, name))
        self.refresh_members()
        messagebox.showinfo("Success", f"Member '{name}' registered successfully!")

    def refresh_members(self):
        self.member_list.delete(0, tk.END)
        for member in self.library.members.values():
            self.member_list.insert(tk.END, str(member))

    # ---------- BORROW / RETURN TAB ----------
    def create_borrow_tab(self):
        frame = self.tab_borrow
        frame.configure(padding=20)

        tk.Label(frame, text="Borrow or Return Book", font=("Segoe UI", 13, "bold")).grid(row=0, column=0, columnspan=2, pady=10)

        tk.Label(frame, text="Member ID:", font=("Segoe UI", 10)).grid(row=1, column=0, sticky="e", padx=5, pady=5)
        tk.Label(frame, text="Book ID:", font=("Segoe UI", 10)).grid(row=2, column=0, sticky="e", padx=5, pady=5)

        self.borrow_mid = ttk.Entry(frame, width=30)
        self.borrow_bid = ttk.Entry(frame, width=30)
        self.borrow_mid.grid(row=1, column=1, padx=5, pady=5)
        self.borrow_bid.grid(row=2, column=1, padx=5, pady=5)

        ttk.Button(frame, text="📘 Borrow Book", command=self.borrow_book).grid(row=3, column=0, pady=10)
        ttk.Button(frame, text="📗 Return Book", command=self.return_book).grid(row=3, column=1, pady=10)

    def borrow_book(self):
        mid = self.borrow_mid.get()
        bid = self.borrow_bid.get()
        msg = self.library.borrow_book(mid, bid)
        self.refresh_books()
        messagebox.showinfo("Result", msg)

    def return_book(self):
        mid = self.borrow_mid.get()
        bid = self.borrow_bid.get()
        msg = self.library.return_book(mid, bid)
        self.refresh_books()
        messagebox.showinfo("Result", msg)


# ---------- RUN APP ----------
if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryApp(root)
    root.mainloop()
