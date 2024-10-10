# Mini-Project: Library Management System with Database Integration

from connect_mysql import connect_database
from termcolor import colored
import library_book_operations
import library_user_operations
import library_author_operations
conn = connect_database()

def main():
    library = {}
    authors = {}
    users = {}
    current_loans = {}
    book_operations = library_book_operations.BookOperations(library, current_loans)
    user_operations = library_user_operations.UserOperations(users)
    author_operations = library_author_operations.AuthorOperations(authors)
    while True:
        try:
            print(colored("\nWelcome to the Library Management System! 🤓 📚", "cyan", attrs=["bold"]))
            print(colored("\n1. Book Operations \n2. User Operations \n3. Author Operations \n4. Quit\n", "dark_grey"))
            choice = input("Enter your choice: ")
            if choice == "1":
                print(colored("\n📚 Book Operations:", "cyan", attrs=["bold"]))
                print(colored("\n1. Add a new book \n2. Borrow a book \n3. Return a book \n4. Search for a book \n5. Display all books \n6. Quit\n", "dark_grey"))
                choice = input("Enter your choice: ")
                if choice == "1":
                    updated = book_operations.add_book()
                    library = updated
                elif choice == "2":
                    updated = book_operations.borrowed_books()
                    library = updated 
                elif choice == "3":
                    updated = book_operations.returned_books()
                    library = updated
                elif choice == "4":
                    book_operations.search_book()
                elif choice == "5":
                    book_operations.display_books()
                elif choice == "6":
                    print(colored("\nThank you for using the Library Management System! 👋\n", "cyan"))
                    break
                else:
                    print("\nInvalid choice.")
            elif choice == "2":
                print(colored("\n📚 User Operations:", "cyan", attrs=["bold"]))
                print(colored("\n1. Add a new user \n2. Display all users \n3. Quit\n", "dark_grey"))
                choice = input("Enter your choice: ")
                if choice == "1":
                    user_operations.add_new_user()
                elif choice == "2":
                    user_operations.display_all_users() 
                elif choice == "3":
                    print(colored("\nThank you for using the Library Management System! 👋\n", "cyan"))
                    break
                else:
                    print("\nInvalid choice.")
            elif choice == "3":
                print(colored("\n📚 Author Operations:", "cyan", attrs=["bold"]))
                print(colored("\n1. Add a new author \n2. Display all authors \n3. Quit\n", "dark_grey"))
                choice = input("Enter your choice: ")
                if choice == "1":
                    author_operations.add_new_author()
                elif choice == "2":
                    author_operations.display_all_authors() 
                elif choice == "3":
                    print(colored("\nThank you for using the Library Management System! 👋\n", "cyan"))
                    break
                else:
                    print("\nInvalid choice.")
            elif choice == "4":
                print(colored("\nThank you for using the Library Management System! 👋\n", "cyan"))
                break
            else:
                print("\nInvalid choice.")   
        except Exception as e:
            print(f"\nAn error occured: {e}")
        except ValueError:
            print("Please use only numbers for year.")

if __name__ == "__main__":
    main()