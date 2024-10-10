# Library Book Operations

from connect_mysql import connect_database
from termcolor import colored
conn = connect_database()

users = {}

class Book:
    def __init__(self, title, author, genre, isbn, publication_date):
        self.title = title
        self.author = author
        self.genre = genre
        self.isbn = isbn
        self.publication_date = publication_date
        self.is_available = True

    def get_title(self):
        return self.title.title()
    
    def get_availability(self):
        return self.is_available
    
    def change_book_status(self):
        if self.is_available:
            self.is_available = False
        elif not self.is_available:
            self.is_available = True

    def display_book_information(self):
        print(colored(f"\nTitle: {self.title}", "cyan", attrs=["bold"]))
        print(colored(f"Author: {self.author} \nGenre: {self.genre} \nISBN: {self.isbn} \nPublication Date: {self.publication_date}", "grey"))
        if self.get_availability() == True:
            print(colored("Availability: Available", "grey"))
        else:
            print(colored("Availability: Borrowed", "grey"))
        print(colored("-------------", "grey"))

class BookOperations:
    def __init__(self, library, current_loans):
        self.library = library
        self.current_loans = current_loans

    def get_author_id(self, author_name):
        author_id = None
        if conn is not None:
            cursor = conn.cursor()
            try:
                query = "SELECT id FROM Authors WHERE author_name = %s"
                cursor.execute(query, (author_name,))
                author = cursor.fetchone()
                if author:
                    author_id = author[0]
                else:
                    print("Author not found in database.")
            except Exception as e:
                print(f"Error: {e}")

            finally:
                cursor.close()
        return author_id
    
    def update_book_availability(self, book_id):
        if conn is not None:
            cursor = conn.cursor()
            try:
                query_select = "SELECT availability FROM Books WHERE id = %s"
                cursor.execute(query_select, (book_id,))
                book = cursor.fetchone()
                if book:
                    availability = book[0]
                    if availability == 1:
                        availability = 0
                    else:
                        availability = 1
                    query = "UPDATE Books SET availability = %s WHERE id = %s"
                    cursor.execute(query, (availability, book_id))
            except Exception as e:
                print(f"Error: {e}")

            finally:
                cursor.close()

    def add_book(self):
        author = input("Enter the author name: ").title()
        author_id = self.get_author_id(author)
        if author_id is None:
            print("Author not found in database. Please add author in author operations.")
        else:
            title = input("\nEnter the book's title: ").title()
            genre = input("Enter the genre: ").title()
            isbn = input("Enter the isbn: ")
            publication_date = input("Enter the publication date YYYY-MM-DD: ")
            if conn is not None:
                cursor = conn.cursor()
                try:
                    query = "INSERT INTO Books(title, author_id, genre, isbn, publication_date, availability) VALUES (%s, %s, %s, %s, %s, %s)"
                    cursor.execute(query, (title, author_id, genre, isbn, publication_date, True))
                    conn.commit()
                    print("Book added successfully.")
                except Exception as e:
                    print(f"Error: {e}")

                finally:
                    cursor.close()
    
    def display_books(self):
        if conn is not None:
            cursor = conn.cursor()
            try:
                query = "SELECT * FROM Books"
                cursor.execute(query)
                books = cursor.fetchall()
                print(colored(f"\n📚 Books:", "cyan", attrs=["bold"]))
                for book in books:
                    print(colored(f"\nTitle: {book[1]} \nAuthor ID: {book[2]} \nGenre: {book[3]} \nISBN: {book[4]} \nPublication Date: {book[5]}", "grey"))
                    if book[6] == 1:
                        print(colored(f"Availability: Is Availabile", "grey"))
                    else:
                        print(colored(f"Availability: Not Availabile", "grey"))
                    print(colored(f"\n-------------", "grey"))
            except Exception as e:
                print(f"Error: {e}")

            finally:
                cursor.close()

    def get_user_id(self, user_name):
        user_id = None
        if conn is not None:
            cursor = conn.cursor()
            try:
                query = "SELECT id FROM Users WHERE user_name = %s"
                cursor.execute(query, (user_name,))
                user = cursor.fetchone()
                if user:
                    user_id = user[0]
                else:
                    print("User not found in database.")
            except Exception as e:
                print(f"Error: {e}")

            finally:
                cursor.close()
        return user_id
    
    def get_book_id(self, title):
        book_id = None
        if conn is not None:
            cursor = conn.cursor()
            try:
                query = "SELECT id FROM Books WHERE title = %s"
                cursor.execute(query, (title,))
                book = cursor.fetchone()
                if title:
                    book_id = book[0]
                else:
                    print("Author not found in database.")
            except Exception as e:
                print(f"Error: {e}")

            finally:
                cursor.close()
        return book_id
    
    def search_book(self):
        book = input("Enter the book title to search: ").title()
        book_id = self.get_book_id(book)
        if book_id is None:
            print("Book not found in database. Please add book in book operations.")
        else:
           if conn is not None:
                cursor = conn.cursor()
                try:
                    if book_id:
                        query = "SELECT title, author_id, genre, isbn, publication_date, availability FROM Books WHERE title = %s"
                        cursor.execute(query, (book,))
                        book_data = cursor.fetchone()
                        print(colored(f"\nBook:", "cyan", attrs=["bold"]))
                        print(colored(f"\nTitle: {book_data[0]} \nAuthor ID: {book_data[1]} \nGenre: {book_data[2]} \nISBN: {book_data[3]} \nPublication Date: {book_data[4]}", "grey"))
                        if book_data[5] == 1:
                            print(colored(f"Availability: Is Availabile", "grey"))
                        else:
                            print(colored(f"Availability: Not Availabile", "grey"))
                    else:
                        print("Book not found in database.")
                    
                except Exception as e:
                    print(f"Error: {e}")

                finally:
                    cursor.close()
    
    def borrowed_books(self):
        user = input("Enter the user name: ").title()
        user_id = self.get_user_id(user)
        book = input("Enter the book title: ").title()
        book_id = self.get_book_id(book)
        if user_id is None or book_id is None:
            print("User or book not found in database. Please add user or book in user operations or book operations.")
        else:
            borrow_date = input("\nEnter the date to borrow book YYYY-MM-DD: ")
            return_date = input("\nEnter the date to return book YYYY-MM-DD: ")
            if conn is not None:
                cursor = conn.cursor()
                try:
                    query = "INSERT INTO BorrowedBooks(user_id, book_id, borrow_date, return_date) VALUES (%s, %s, %s, %s)"
                    cursor.execute(query, (user_id, book_id, borrow_date, return_date))
                    conn.commit()
                    self.update_book_availability(book_id)
                    print("Book borrowed succeffully.")
                except Exception as e:
                    print(f"Error: {e}")

                finally:
                    cursor.close()

    def returned_books(self):
        book = input("Enter the book title: ").title()
        book_id = self.get_book_id(book)
        if book_id is None:
            print("Book not found in database. Please add book in book operations.")
        else:
           if conn is not None:
                cursor = conn.cursor()
                try:
                    if book_id:
                        query = "DELETE FROM BorrowedBooks WHERE book_id = %s"
                        cursor.execute(query, (book_id,))
                        conn.commit()
                        self.update_book_availability(book_id)
                        print("Book returned succeffully.")
                    else:
                        print("Book not found in database.")
                    
                except Exception as e:
                    print(f"Error: {e}")

                finally:
                    cursor.close()