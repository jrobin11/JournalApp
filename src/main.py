# main.py
# This is the entry point of the Journal App where user interaction is handled.

# Import necessary functions from other modules
from admin_module import (
    create_admin_account, admin_create_user, admin_view_user_journal,
    delete_user, admin_view_user_info
)
from user_module import (
    write_entry, read_entry, delete_user_entry, view_mood_statistics,
    search_entries, delete_own_account
)
from shared_functions import (
    list_entries, read_credentials, write_credentials, login, register_user
)

# Function to print a menu with given options and a title
def print_menu(options, title="Menu"):
    # Print the menu header
    print("\n" + "=" * 30)
    print(f"{title}".center(30))
    print("=" * 30)
    # Print each menu option
    for key, value in options.items():
        print(f"{key}. {value}")

def main():
    # Ensures the admin account is created at startup
    create_admin_account()

    while True:
        # Welcome message and role selection
        print("\n" + "-" * 50)
        print("Welcome to Journal App".center(50))
        print("-" * 50)
        user_type = input("Select your role:\n1. Admin (A)\n2. New User (N)\n3. Returning User (R)\n4. Log Out (Q)\nYour choice [A/N/R/Q]: ").strip().lower()

        # Admin role functionalities
        if user_type == 'a':
            # Attempt to log in as admin
            username = login()
            if username == 'admin':
                print(f"\nWelcome, Admin {username}!")
                while True:
                    # Admin action options
                    admin_options = {
                        "1": "Create a User",
                        "2": "View User Info",
                        "3": "Delete a User",
                        "4": "View User Journals",
                        "5": "Log Out"
                    }
                    # Display the admin menu
                    print_menu(admin_options, "Admin Actions")
                    admin_choice = input("Enter choice: ")

                    # Execute the selected admin option
                    if admin_choice == '1':
                        admin_create_user()
                    elif admin_choice == '2':
                        admin_view_user_info()
                    elif admin_choice == '3':
                        delete_user(username)
                    elif admin_choice == '4':
                        admin_view_user_journal(username)
                    elif admin_choice == '5':
                        break  # Logging out
                    else:
                        print("Invalid choice. Please try again.")
            else:
                print("Admin login failed.")

        # New or Returning User functionalities
        elif user_type in ['n', 'r']:
            # Register a new user
            if user_type == 'n':
                register_user()
                continue

            # Attempt to log in as user
            username = login()
            if username:
                print(f"\nWelcome, {username}!")
                while True:
                    # User action options
                    user_options = {
                        "1": "Write new entry",
                        "2": "Read an entry",
                        "3": "View mood statistics",
                        "4": "Search entries",
                        "5": "List all entries",
                        "6": "Delete an entry",
                        "7": "Delete your account",
                        "8": "Log Out"
                    }
                    # Display the user menu
                    print_menu(user_options, "Journal App")
                    choice = input("Enter choice: ")

                    # Execute the selected user option
                    if choice == '1':
                        write_entry(username)
                    elif choice == '2':
                        read_entry(username)
                    elif choice == '3':
                        view_mood_statistics(username)
                    elif choice == '4':
                        keyword = input("Enter keyword to search: ")
                        search_entries(username, keyword)
                    elif choice == '5':
                        list_entries(username)
                    elif choice == '6':
                        delete_user_entry(username)
                    elif choice == '7':
                        # Attempt to delete the user's own account
                        if delete_own_account(username):
                            break  # Exit if account deletion is successful
                    elif choice == '8':
                        break  # Logging out
                    else:
                        print("Invalid choice. Please try again.")
            else:
                print("Login failed. Please try again.")

        # Exit the application
        elif user_type == 'q':
            print("\nLogging out of the program. Goodbye!")
            break

        else:
            print("Invalid selection. Please enter 'A', 'N', 'R', or 'Q'.")

# Check if the script is the main program and run it
if __name__ == "__main__":
    main()
