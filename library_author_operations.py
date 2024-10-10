# Library Author Operations

from connect_mysql import connect_database
from termcolor import colored
conn = connect_database()

class Author:
    def __init__(self, author_name, biography):
        self.author_name = author_name
        self.biography = biography

    def get_author_name(self):
        return self.author_name
    
    def get_books_written(self):
        return self.books_written
    
    def view_author_details(self):
        print(colored(f"\nAuthor: {self.author_name}", "cyan", attrs=["bold"]))
        print(colored(f"Biography: {self.biography}", "grey"))
        print(colored("-------------", "grey"))

class AuthorOperations:
    def __init__(self, authors):
        self.authors = authors

    def add_new_author(self):
        author_name = input("\nEnter the author name: ").title()
        biography = input(f"\nEnter a short biography of {author_name}: ")
        if conn is not None:
            cursor = conn.cursor()
            try:
                query = "INSERT INTO Authors(author_name, biography) VALUES (%s, %s)"
                cursor.execute(query, (author_name, biography))
                conn.commit()
                print("Author added successfully.")
            except Exception as e:
                print(f"Error: {e}")

            finally:
                cursor.close()
    
    def display_all_authors(self):
        if conn is not None:
            cursor = conn.cursor()
            try:
                query = "SELECT * FROM Authors"
                cursor.execute(query)
                authors = cursor.fetchall()
                print(colored(f"\nAuthors:", "cyan", attrs=["bold"]))
                for author in authors:
                    print(colored(f"\nAuthor ID: {author[0]} \nName: {author[1]} \nBiography: {author[2]}", "grey"))
                    print(colored(f"\n-----------", "grey"))
            except Exception as e:
                print(f"Error: {e}")

            finally:
                cursor.close()