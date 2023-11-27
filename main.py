# main.py
from admin_module import create_admin_account, admin_create_user,\
    admin_view_user_journal, delete_user, admin_view_user_info
from user_module import write_entry, read_entry, delete_user_entry,\
    view_mood_statistics, search_entries, delete_own_account
from shared_functions import login, register_user

def main():
    create_admin_account()  # This ensures the admin account is created at startup

    while True:
        print("Welcome to Journal App, please sign in.")
        user_type = input("Are you an admin (A), a new user (N), a returning user (R),"
                          " or would you like to log out (Q)? [A/N/R/Q]: ").strip().lower()

        if user_type == 'a':
            username = login()
            if username == 'admin':
                print(f"Welcome, Admin {username}!")
                while True:
                    print("\nAdmin Actions")
                    print("1. Create a User")
                    print("2. View User Info")
                    print("3. Delete a User")
                    print("4. View User Journals")
                    print("5. Log Out")
                    admin_choice = input("Enter choice: ")

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

        elif user_type in ['n', 'r']:
            if user_type == 'n':
                register_user()
                continue

            username = login()
            if username:
                print(f"Welcome, {username}!")
                while True:
                    print("\nJournal App")
                    print("1. Write new entry")
                    print("2. Read an entry")
                    print("3. View mood statistics")
                    print("4. Search entries")
                    print("5. List all entries")
                    print("6. Delete an entry")
                    print("7. Delete your account")
                    print("8. Log Out")
                    choice = input("Enter choice: ")

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
                        if delete_own_account(username):
                            break  # Exit the user menu if account deletion is successful
                    elif choice == '8':
                        break  # Logging out
                    else:
                        print("Invalid choice. Please try again.")
            else:
                print("Login failed. Please try again.")

        elif user_type == 'q':
            break  # Logging out of the program

        else:
            print("Invalid selection. Please enter 'A', 'N', 'R', or 'Q'.")


if __name__ == "__main__":
    main()
