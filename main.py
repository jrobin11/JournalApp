import os
import datetime
import hashlib
import getpass

# Path where the user credentials will be stored
CREDENTIALS_PATH = "credentials.txt"

# Path where the journal entries will be stored
JOURNAL_PATH = "journal_entries"

ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = 'admin'


# Function to hash a password
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


# Function to check if the admin account exists
def admin_exists():
    if not os.path.exists(CREDENTIALS_PATH):
        return False
    with open(CREDENTIALS_PATH, "r") as file:
        for line in file:
            if line.startswith(ADMIN_USERNAME + ","):
                return True
    return False


# verifying admin password -- hashed password
"""
def verify_admin_password():
    admin_hashed_password = hash_password(ADMIN_PASSWORD)
    print("Hashed Admin Password (for verification):", admin_hashed_password)
    with open(CREDENTIALS_PATH, "r") as file:
        for line in file:
            if line.startswith(ADMIN_USERNAME + ","):
                _, _, _, stored_password = line.strip().split(',')
                if stored_password == admin_hashed_password:
                    print("Admin password verified successfully.")
                else:
                    print("Admin password verification failed.")
                return

# Call this function to verify the admin password
verify_admin_password()
"""


# Function to create an admin account
def create_admin_account():
    hashed_password = hash_password(ADMIN_PASSWORD)
    with open(CREDENTIALS_PATH, "a") as file:
        file.write(f"{ADMIN_USERNAME},admin@example.com,admin,{hashed_password}\n")
    print("Admin account created.")


# Main startup sequence
if not admin_exists():
    create_admin_account()

if not os.path.exists(JOURNAL_PATH):
    os.makedirs(JOURNAL_PATH)


def view_user_info(username):
    with open(CREDENTIALS_PATH, "r") as file:
        for line in file:
            parts = line.strip().split(',')
            if len(parts) < 4:
                continue  # Skip lines that don't have enough values
            stored_username, email, age, _ = parts
            if stored_username == username:
                print(f"Username: {stored_username}\nEmail: {email}\nAge: {age}")
                return
    print("User not found.")


def view_edit_user_info(admin_username):
    if admin_username != ADMIN_USERNAME:
        print("Only the admin can view or edit user info.")
        return

    # List all users
    print("List of Users:")
    with open(CREDENTIALS_PATH, "r") as file:
        for line in file:
            username = line.split(',')[0]
            print(username)

    # Ask which user to edit
    username_to_edit = input("Enter the username to view/edit: ")
    view_user_info(username_to_edit)

    # Ask if the admin wants to edit this user's info
    edit_choice = input("Do you want to edit this user's info? (Y/N): ").strip().lower()
    if edit_choice == 'y':
        edit_user_info(username_to_edit)


def edit_user_info(username):
    with open(CREDENTIALS_PATH, "r") as file:
        lines = file.readlines()

    found = False
    with open(CREDENTIALS_PATH, "w") as file:
        for line in lines:
            stored_username, email, age, password = line.strip().split(',')
            if stored_username == username:
                new_email = input("Enter new email (leave blank to keep current): ").strip() or email
                new_age = input("Enter new age (leave blank to keep current): ").strip() or age
                line = f"{username},{new_email},{new_age},{password}\n"
                found = True
            file.write(line)

    if not found:
        print("User not found.")
    else:
        print("User information updated.")


def delete_user(admin_username):
    if admin_username != ADMIN_USERNAME:
        print("Only the admin can delete users.")
        return

    # List all users before deletion
    print("List of Users:")
    with open(CREDENTIALS_PATH, "r") as file:
        users = [line.split(',')[0] for line in file if line.strip()]
    for user in users:
        print(user)

    delete_username = input("Enter the username of the user to delete: ")

    # Proceed with deletion if the user exists
    if delete_username in users:
        with open(CREDENTIALS_PATH, "r") as file:
            lines = file.readlines()

        with open(CREDENTIALS_PATH, "w") as file:
            for line in lines:
                if line.startswith(delete_username + ","):
                    continue  # Skip the user to be deleted
                file.write(line)

        print(f"User {delete_username} has been deleted.")
    else:
        print(f"User {delete_username} not found.")


# Function to register a new user
def register_user():
    username = input("Create a username: ")
    email = input("Enter your email: ")
    age = input("Enter your age: ")
    password = getpass.getpass("Create a password: ")
    hashed_password = hash_password(password)

    if user_exists(username):
        print("Username already exists. Please try a different username.")
        return False

    with open(CREDENTIALS_PATH, "a") as file:
        file.write(f"{username},{email},{age},{hashed_password}\n")
    print("Registration successful.")
    return True


# Function to check if a user already exists
def user_exists(username):
    if not os.path.exists(CREDENTIALS_PATH):
        return False
    with open(CREDENTIALS_PATH, "r") as file:
        for line in file:
            if line.split(',')[0] == username:
                return True
    return False


# Function to check login credentials
def login():
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")
    hashed_password = hash_password(password)

    with open(CREDENTIALS_PATH, "r") as file:
        for line in file:
            parts = line.strip().split(',')
            if len(parts) < 4:
                # Skip lines that don't have enough values (for backward compatibility)
                continue
            stored_username, _, _, stored_password = parts
            if stored_username == username and stored_password == hashed_password:
                return username  # Return the username if login is successful
    return None


def write_entry():
    today = datetime.date.today()
    now = datetime.datetime.now()
    filename = f"{JOURNAL_PATH}/{today.strftime('%m-%d-%Y')}.txt"
    title = input("Enter title for your journal entry: ").strip()

    # New feature: Record mood
    mood = input("How are you feeling today (e.g., Happy, Sad, Neutral)? ").strip()

    print("Write your journal entry (type 'END' on a new line to finish):")

    with open(filename, "a") as file:
        file.write(f"\nTitle: {title}\n")
        file.write(f"Mood: {mood}\n")  # Save the mood
        file.write(f"Time: {now.strftime('%H:%M:%S')}\n")
        while True:
            line = input()
            if line.strip().lower() == "end":
                break
            file.write(line + "\n")
    print(f"Journal entry '{title}' saved.")


def read_entry(date):
    # Convert user input date to MM-DD-YYYY format for filename
    formatted_date = datetime.datetime.strptime(date, '%m/%d/%Y').strftime('%m-%d-%Y')
    filename = f"{JOURNAL_PATH}/{formatted_date}.txt"
    if os.path.exists(filename):
        with open(filename, "r") as file:
            entries = file.read().split('\nTitle: ')[1:]
        print(f"\nJournal Entries for {date}:")
        for i, entry in enumerate(entries):
            title = entry.split('\n')[0]
            print(f"{i + 1}. {title}")

        entry_number = int(input("\nEnter the number of the entry you want to read: ")) - 1
        if 0 <= entry_number < len(entries):
            entry_title = entries[entry_number].split('\n')[0]  # Extract the title outside the f-string
            print(f"\nReading Entry: {entry_title}")
            print(entries[entry_number])
        else:
            print("Invalid entry number.")
    else:
        print("No entry found for this date.")


def view_mood_statistics():
    print("\nMood Statistics:")
    mood_count = {}
    for filename in os.listdir(JOURNAL_PATH):
        with open(f"{JOURNAL_PATH}/{filename}", "r") as file:
            entries = file.read().split('\nTitle: ')[1:]
            for entry in entries:
                mood_line = entry.split('\n')[1]  # Assuming the second line contains the mood
                mood = mood_line.split(': ')[1]
                mood_count[mood] = mood_count.get(mood, 0) + 1

    for mood, count in mood_count.items():
        print(f"{mood}: {count} time(s)")


def search_entries(keyword):
    found = False
    print("\nSearch Results:")
    for filename in os.listdir(JOURNAL_PATH):
        with open(f"{JOURNAL_PATH}/{filename}", "r") as file:
            entries = file.read().split('\nTitle: ')[1:]
            for entry in entries:
                if keyword.lower() in entry.lower():
                    title = entry.split('\n')[0]
                    date = filename.replace('.txt', '').replace('-', '/')
                    print(f"Entry: {title} (Date: {date})")
                    found = True

    if not found:
        print("No entries found with that keyword.")


def list_entries():
    print("\nList of All Journal Entries:")
    for filename in sorted(os.listdir(JOURNAL_PATH)):
        date = filename.replace('.txt', '')
        print(f"\nDate: {date}")
        with open(f"{JOURNAL_PATH}/{filename}", "r") as file:
            entries = file.read().split('\nTitle: ')[1:]
            for i, entry in enumerate(entries):
                title = entry.split('\n')[0]
                print(f"  {i + 1}. {title}")


def main():
    while True:
        user_type = input("Are you an admin (A), a new user (N), or a returning user (R)? [A/N/R]: ").strip().lower()

        if user_type == 'a':  # Admin login
            while True:
                username = login()
                if username == ADMIN_USERNAME:
                    print(f"Welcome, Admin {username}!")
                    while True:
                        print("\nAdmin Actions")
                        print("1. View/Edit User Info")
                        print("2. Delete a User")
                        print("3. Exit")
                        admin_choice = input("Enter choice: ")

                        if admin_choice == '1':
                            view_edit_user_info(username)
                        elif admin_choice == '2':
                            delete_user(username)
                        elif admin_choice == '3':
                            break  # Break out of the admin loop
                        else:
                            print("Invalid choice. Please try again.")
                    break  # Break out of the admin login loop
                else:
                    print("Admin login failed. Please try again or enter 'exit' to leave.")
                    if input().lower() == 'exit':
                        return  # Exit the program

        elif user_type in ['n', 'r']:  # New or Returning User
            if user_type == 'n':
                if register_user():
                    print("Registration successful. Please log in.")
                else:
                    continue  # Continue at the start of the main loop

            while True:
                username = login()
                if username:
                    global JOURNAL_PATH
                    JOURNAL_PATH = f"journal_entries/{username}"
                    if not os.path.exists(JOURNAL_PATH):
                        os.makedirs(JOURNAL_PATH)
                    print(f"Welcome, {username}!")
                    break
                else:
                    print("Login failed. Please try again or enter 'exit' to leave.")
                    if input().lower() == 'exit':
                        return  # Exit the program

            # Regular user actions here
            while True:
                print("\nJournal App")
                print("1. Write new entry")
                print("2. Read an entry")
                print("3. View mood statistics")
                print("4. Search entries")
                print("5. List all entries")
                print("6. Exit")
                choice = input("Enter choice: ")

                if choice == '1':
                    write_entry()
                elif choice == '2':
                    date = input("Enter date (MM/DD/YYYY) to read: ")
                    try:
                        read_entry(date)
                    except ValueError:
                        print("Invalid date format. Please use MM/DD/YYYY.")
                elif choice == '3':
                    view_mood_statistics()
                elif choice == '4':
                    keyword = input("Enter keyword to search: ")
                    search_entries(keyword)
                elif choice == '5':
                    list_entries()
                elif choice == '6':
                    break  # Exit the journal app loop
                else:
                    print("Invalid choice. Please try again.")

        elif user_type == 'exit':
            break  # Exit the main loop, thus ending the program
        else:
            print("Invalid selection. Please enter 'A' for admin, 'N' for new user, 'R' for returning user, or 'exit' "
                  "to leave.")


if __name__ == "__main__":
    main()
