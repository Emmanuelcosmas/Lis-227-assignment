import datetime

class Book:
    def __init__(self, title, author, genre, isbn):
        self.title = title
        self.author = author
        self.genre = genre
        self.isbn = isbn
        self.is_borrowed = False
        self.borrower_id = None
        self.borrow_date = None

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, genre, isbn):
        book = Book(title, author, genre, isbn)
        self.books.append(book)

    def add_inventory(self):
        popular_books = [
            ("The Catcher in the Rye", "J.D. Salinger", "Coming-of-age fiction", "9780316769488"),
            ("Pride and Prejudice", "Jane Austen", "Romance", "9780141439518"),
            ("Moby-Dick", "Herman Melville", "Adventure", "9780142437247"),
            ("The Hobbit", "J.R.R. Tolkien", "Fantasy", "9780618260300"),
            ("The Da Vinci Code", "Dan Brown", "Mystery", "9780307474278"),
            # Add more popular books here...
        ]

        for title, author, genre, isbn in popular_books:
            self.add_book(title, author, genre, isbn)

    def view_books(self):
        print("All Books in the Library:")
        for book in self.books:
            print(f"Title: {book.title}, Author: {book.author}, Genre: {book.genre}, ISBN: {book.isbn}, "
                  f"Borrowed: {'Yes' if book.is_borrowed else 'No'}")

    def search_book(self, title):
        found_books = [book for book in self.books if book.title.lower() == title.lower()]
        if found_books:
            print("Book(s) found:")
            for book in found_books:
                print(f"Title: {book.title}, Author: {book.author}, Genre: {book.genre}, ISBN: {book.isbn}, "
                      f"Borrowed: {'Yes' if book.is_borrowed else 'No'}")
        else:
            print("Book not found.")

    def borrow_book(self, title, borrower_id):
        for book in self.books:
            if book.title.lower() == title.lower():
                if not book.is_borrowed:
                    book.is_borrowed = True
                    book.borrower_id = borrower_id
                    book.borrow_date = datetime.date.today()
                    print(f"Book '{book.title}' has been borrowed by {borrower_id}.")
                    return
                else:
                    print(f"Book '{book.title}' is already borrowed.")
                    return
        print("Book not found.")

    def borrowed_books(self):
        borrowed_books_list = [book for book in self.books if book.is_borrowed]
        return borrowed_books_list

    def add_custom_book(self):
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        genre = input("Enter genre: ")
        isbn = input("Enter book ISBN: ")
        self.add_book(title, author, genre, isbn)
        print("Custom book added successfully.")


def main():
    library = Library()
    library.add_inventory()

    while True:
        print("\nWelcome to the Library Management System")
        print("1. View Books")
        print("2. Search Book")
        print("3. Borrow Book")
        print("4. View Borrowed Books")
        print("5. Add Custom Book")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            library.view_books()

        elif choice == '2':
            title = input("Enter book title to search: ")
            library.search_book(title)

        elif choice == '3':
            title = input("Enter book title to borrow: ")
            borrower_id = input("Enter your ID: ")
            library.borrow_book(title, borrower_id)

        elif choice == '4':
            print("\nBorrowed Books:")
            borrowed_books = library.borrowed_books()
            for book in borrowed_books:
                print(f"Title: {book.title}, Author: {book.author}, Genre: {book.genre}, "
                      f"ISBN: {book.isbn}, Borrower ID: {book.borrower_id}, Borrow Date: {book.borrow_date}")

        elif choice == '5':
            library.add_custom_book()

        elif choice == '6':
            print("Thank you for using the Library Management System.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
