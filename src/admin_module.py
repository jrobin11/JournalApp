# admin_module.py
from shared_functions import read_credentials, write_credentials, \
    display_users, list_entries, register_user, hash_password

ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = 'admin'

def admin_exists():
    credentials = read_credentials()
    return ADMIN_USERNAME in credentials

def create_admin_account():
    if not admin_exists():
        credentials = read_credentials()
        credentials[ADMIN_USERNAME] = {
            "email": "admin@example.com",
            "age": "admin",
            "password": hash_password(ADMIN_PASSWORD)
        }
        write_credentials(credentials)
        print("Admin account created.")

def admin_create_user():
    print("Admin creating a new user...")
    register_user()

def admin_view_user_info():
    display_users()
    username = input("Enter username to view info, or 'cancel' to return: ")
    if username.lower() == 'cancel':
        return

    credentials = read_credentials()
    user_info = credentials.get(username)
    if user_info:
        print(f"Username: {username}\nEmail: {user_info['email']}\nAge: {user_info['age']}")
    else:
        print("User not found.")

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
        del credentials[delete_username]
        write_credentials(credentials)
        print(f"User {delete_username} has been deleted.")
    else:
        print("User not found.")
