# admin_module.py
# This module contains functions related to admin actions in the Journal App.

# Importing necessary functions from shared_functions module for various operations.
from shared_functions import read_credentials, write_credentials, \
    display_users, list_entries, register_user, hash_password

# Constants for admin username and password.
ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = 'admin'

# Function to check if the admin account already exists in the credentials.
def admin_exists():
    credentials = read_credentials()
    return ADMIN_USERNAME in credentials

# Function to create an admin account if it doesn't exist.
def create_admin_account():
    if not admin_exists():
        credentials = read_credentials()
        # Hashing admin password for secure storage.
        hashed_password = hash_password(ADMIN_PASSWORD)
        # Storing admin credentials in the credentials dictionary.
        credentials[ADMIN_USERNAME] = {
            "email": "admin@example.com",
            "age": "admin",
            "password": hashed_password
        }
        # Writing the updated credentials back to the JSON file.
        write_credentials(credentials)
        print("Admin account created.")

# Function to allow admin to create a new user account.
def admin_create_user():
    print("Admin creating a new user...")
    register_user()

# Function to allow admin to view user information.
def admin_view_user_info():
    # Displays list of users for admin to choose from.
    display_users()
    username = input("Enter username to view info, or 'cancel' to return: ")
    if username.lower() == 'cancel':
        return

    credentials = read_credentials()
    # Retrieving and displaying the selected user's information.
    user_info = credentials.get(username)
    if user_info:
        print(f"Username: {username}\nEmail: {user_info['email']}\nAge: {user_info['age']}")
    else:
        print("User not found.")

# Function to allow admin to view user journals.
def admin_view_user_journal(admin_username):
    if admin_username != ADMIN_USERNAME:
        print("Only the admin can view user journals.")
        return

    display_users()
    username = input("Enter username to view their journal, or 'cancel' to return: ")
    if username.lower() == 'cancel':
        return

    if username in read_credentials():
        list_entries(username)
    else:
        print("Username not found. Please try again.")

# Function to allow admin to delete a user account.
def delete_user(admin_username):
    if admin_username != ADMIN_USERNAME:
        print("Only the admin can delete users.")
        return

    display_users()
    delete_username = input("Enter the username of the user to delete, or 'cancel' to return: ")
    if delete_username.lower() == 'cancel':
        return

    credentials = read_credentials()
    if delete_username in credentials:
        # Deleting the user from the credentials dictionary.
        del credentials[delete_username]
        # Writing the updated credentials back to the JSON file.
        write_credentials(credentials)
        print(f"User {delete_username} has been deleted.")
    else:
        print("User not found.")
