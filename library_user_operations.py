# Library User Operations

from connect_mysql import connect_database
from termcolor import colored
import re
conn = connect_database()

class User:
    def __init__(self, user_name, user_phone_number, user_email, user_library_id):
        self.user_name = user_name
        self.__user_phone_number = user_phone_number
        self.__user_email = user_email
        self.__user_library_id = user_library_id

    def get_user_name(self):
        return self.user_name
    
    # def get_user_phone_number(self):
    #     return self.__user_phone_number
    
    # def get_user_email(self):
    #     return self.__user_email
    
    def get_user_library_id(self):
        return self.__user_library_id
    
    def get_books_borrowed(self):
        return self.books_borrowed
    
    def set_books_borrowed(self):
        return self.books_borrowed
    
    def view_user_details(self):
        print(colored(f"\nName: {self.user_name}", "cyan", attrs=["bold"]))
        print(colored(f"Phone: {self.__user_phone_number} \nEmail: {self.__user_email} \nLibraray ID: {self.__user_library_id}", "grey"))
        print(colored("-------------", "grey"))

class UserOperations:
    def __init__(self, users):
        self.users = users

    def add_new_user(self):
        user_name = input("\nEnter the name of the new user: ").title()
        user_library_id = input("\nEnter the library ID of the new user: ")
        if conn is not None:
            cursor = conn.cursor()
            try:
                query = "INSERT INTO Users(user_name, user_library_id) VALUES (%s, %s)"
                cursor.execute(query, (user_name, user_library_id))
                conn.commit()
                print("User added successfully.")
            except Exception as e:
                print(f"Error: {e}")

            finally:
                cursor.close()
    

    def display_all_users(self):
        if conn is not None:
            cursor = conn.cursor()
            try:
                query = "SELECT * FROM Users"
                cursor.execute(query)
                users = cursor.fetchall()
                print(colored(f"\nUsers:", "cyan", attrs=["bold"]))
                for user in users:
                    print(colored(f"\nUser ID: {user[0]} \nName: {user[1]} \nLibrary ID: {user[2]}", "grey"))
                    print(colored(f"\n-----------", "grey"))
            except Exception as e:
                print(f"Error: {e}")

            finally:
                cursor.close()