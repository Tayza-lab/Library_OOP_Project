# HELLO TAYZA, LOOK AT HOW YOU COPY, PASTE EVERYTHING FROM GenAI, THAT IS UNACCEPTABLE. YOU CAN USE GenAI FOR BRAINSTORMING, 
# IMPROVING ENGLISH GRAMMATICAL FLOW, FLUENCY, AND TONE. NOT TO FULLY RELY ON IT.   
# Library_OOP_Project
K20231310 - Library GUI Project
Sure 😊 — here’s a **more natural, student-style README**.
It’s still well-written and clear, but sounds like something a **university student** would actually submit or include in a project folder.

---

📚 Library Management System (Python GUI + OOP)

This is my **Library Management System** project made using **Python, Tkinter, and Object-Oriented Programming (OOP)**.
The system lets you **add books, register members, and manage borrowing and returning books** through a nice graphical interface.
It also **saves data automatically** using JSON files, so everything is kept even after you close the program.

---

🧠 Project Description

The main goal of this project was to build a small but functional system that demonstrates **OOP concepts** like:

* Classes and objects
* Encapsulation
* Composition
* File handling for data storage

I also focused on making the interface look **modern and easy to use**, using only Tkinter (no extra libraries).

---

✨ Features

* 📘 Add new books with ID, title, author, and copies
* 👥 Register new library members
* 🔄 Borrow and return books
* 💾 Data automatically saved in `.json` files
* 🖥️ Aesthetic Tkinter GUI with color themes and icons
* 🔧 Simple and modular OOP structure

---

 🗂️ Project Structure

```
library_gui_project/
│
├── main.py                   # GUI interface (Tkinter)
│
├── models/
│   ├── book.py               # Book class
│   ├── member.py             # Member class
│   └── library.py            # Library class (handles data and persistence)
│
└── data/
    ├── books.json            # Auto-saved book data
    └── members.json          # Auto-saved member data
```

---

🖥️ How to Run the Project

1. Make sure you have **Python 3.8 or above** installed.
   Tkinter is already included with Python, so you don’t need to install anything extra.

2. Download or clone the project:

   ```bash
   git clone https://github.com/your-username/library_gui_project.git
   cd library_gui_project
   ```

3. Run the program:

   ```bash
   python main.py
   ```

4. The GUI window will open. From there, you can:

   * Add or view books
   * Add members
   * Borrow and return books

---

📦 How Data is Saved

All books and members are saved automatically in the `data` folder:

* `books.json` → stores all book details
* `members.json` → stores all registered members and which books they borrowed

Whenever you restart the app, it loads the data back, so you don’t lose your progress.

---
🧩 OOP Concepts Used

| Concept           | How It’s Used                                       |
| ----------------- | --------------------------------------------------- |
| **Encapsulation** | Private variables like `__book_id`, `__copies`      |
| **Composition**   | Library contains multiple Book and Member objects   |
| **Abstraction**   | GUI interacts with Library methods, not raw data    |
| **File Handling** | JSON used for saving and loading data automatically |

---

🎨 GUI Design

The interface has three main tabs:

1. **Books** – Add and view all books
2. **Members** – Register and view all members
3. **Borrow/Return** – Borrow or return books

It has a clean blue/purple color theme, simple icons, and neatly aligned input boxes to make it look professional.

---

🔮 Possible Future Improvements

* Add a search bar for books and members
* Add due dates and late return fines
* Include a dark mode switch
* Export data to Excel or CSV files
* Convert it to a web app using Flask or Django

---

👨‍💻 About the Author

**Your Name Here**
B.Sc. Computer Science – University Of Kyrenia
📧 nelsonneil731@gmail.com

This project was created for my **Python Programming / OOP course** as part of my university coursework.

---

🪪 License

This project is open-source and free to use for educational purposes.

---
