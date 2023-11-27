import os
import json
import datetime
import hashlib
import getpass

CREDENTIALS_PATH = "src/credentials.json"
JOURNAL_PATH = "journal_entries"
ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = 'admin'


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def read_credentials():
    if not os.path.exists(CREDENTIALS_PATH):
        return {}
    with open(CREDENTIALS_PATH, 'r') as file:
        return json.load(file)


def write_credentials(credentials):
    with open(CREDENTIALS_PATH, 'w') as file:
        json.dump(credentials, file, indent=4)


def admin_exists():
    credentials = read_credentials()
    return ADMIN_USERNAME in credentials


def admin_create_user():
    print("Enter 'cancel' at any prompt to go back, or just press Enter.")
    register_user()

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


def admin_view_user_journal(admin_username):
    if admin_username != ADMIN_USERNAME:
        print("Only the admin can view user journals.")
        return

    display_users()
    while True:
        username = input("Enter username to view their journal, or enter 'cancel' to go back: ")
        if username.lower() == 'cancel' or username == '':
            return
        if username in read_credentials():
            list_entries(username)
            break
        else:
            print("Invalid username. Please try again.")


def user_exists(username):
    credentials = read_credentials()
    return username in credentials


def register_user():
    credentials = read_credentials()

    while True:
        username = input("Create a username: ")
        if username.lower() == 'cancel' or username == '':
            return False
        if username in credentials:
            print("Username already exists. Please try a different username.")
            continue
        break

    while True:
        email = input("Enter your email: ")
        if email.lower() == 'cancel' or email == '':
            return False
        if any(user.get("email") == email for user in credentials.values()):
            print("Email already exists. Please use a different email.")
            continue
        break

    age = input("Enter your age: ")
    if age.lower() == 'cancel' or age == '':
        return False

    password = getpass.getpass("Create a password: ")
    if password == '':
        return False

    hashed_password = hash_password(password)
    credentials[username] = {"email": email, "age": age, "password": hashed_password}
    write_credentials(credentials)
    print("Registration successful.")
    return True


def login():
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")
    hashed_password = hash_password(password)

    credentials = read_credentials()
    if username in credentials and credentials[username]["password"] == hashed_password:
        return username
    return None


def display_users():
    print("List of Users:")
    credentials = read_credentials()
    for user in credentials:
        print(user)


def view_user_info():
    display_users()
    print("Enter 'cancel' to go back.")
    username = input("Enter username to view info: ")
    if username.lower() == 'cancel':
        return
    user_info = read_credentials().get(username)
    if user_info:
        print(f"Username: {username}\nEmail: {user_info['email']}\nAge: {user_info['age']}")
    else:
        print("User not found.")


def delete_user(admin_username):
    if admin_username != ADMIN_USERNAME:
        print("Only the admin can delete users.")
        return

    display_users()
    print("Enter 'cancel' to go back.")
    delete_username = input("Enter the username of the user to delete: ")
    if delete_username.lower() == 'cancel':
        return
    credentials = read_credentials()
    if delete_username in credentials:
        del credentials[delete_username]
        write_credentials(credentials)
        print(f"User {delete_username} has been deleted.")
    else:
        print("User not found.")


def delete_user_entry(username):
    journal_dir = f"{JOURNAL_PATH}/{username}"
    if not os.path.exists(journal_dir):
        print("No journal entries found.")
        return

    list_entries(username)
    print("Enter 'cancel' to go back.")
    entry_date = input("Enter the date of the entry you want to delete (MM-DD-YYYY): ")
    if entry_date.lower() == 'cancel':
        return
    entry_file = f"{journal_dir}/{entry_date}.txt"

    if os.path.exists(entry_file):
        os.remove(entry_file)
        print(f"Entry for {entry_date} deleted.")
    else:
        print("Entry not found for the specified date.")


def write_entry(username):
    today = datetime.date.today()
    filename = f"{JOURNAL_PATH}/{username}/{today.strftime('%m-%d-%Y')}.txt"
    title = input("Enter title for your journal entry: ").strip()
    mood = input("How are you feeling today? ").strip()
    content = input("Write your journal entry: ").strip()

    if not os.path.exists(f"{JOURNAL_PATH}/{username}"):
        os.makedirs(f"{JOURNAL_PATH}/{username}")

    with open(filename, "a") as file:
        file.write(f"Title: {title}\nMood: {mood}\nContent: {content}\n\n")

    print("Journal entry saved.")


def read_entry(username):
    date_input = input("Enter date (MM/DD/YYYY) to read entries: ")
    try:
        date = datetime.datetime.strptime(date_input, '%m/%d/%Y').date()
        filename = f"{JOURNAL_PATH}/{username}/{date.strftime('%m-%d-%Y')}.txt"
        if os.path.exists(filename):
            with open(filename, "r") as file:
                print(file.read())
        else:
            print("No entries found for this date.")
    except ValueError:
        print("Invalid date format. Please use MM/DD/YYYY.")


def view_mood_statistics(username):
    print("\nMood Statistics:")
    mood_count = {}
    user_path = os.path.join(JOURNAL_PATH, username)
    if os.path.isdir(user_path):
        for filename in os.listdir(user_path):
            file_path = os.path.join(user_path, filename)
            with open(file_path, "r") as file:
                entries = file.read().split('\n\n')
                for entry in entries:
                    lines = entry.split('\n')
                    mood_line = next((line for line in lines if line.startswith("Mood:")), None)
                    if mood_line:
                        mood = mood_line.split("Mood: ")[1]
                        mood_count[mood] = mood_count.get(mood, 0) + 1
    for mood, count in mood_count.items():
        print(f"{mood}: {count} time(s)")


def search_entries(username, keyword):
    found = False
    user_path = os.path.join(JOURNAL_PATH, username)
    print("\nSearch Results:")
    if os.path.isdir(user_path):
        for filename in os.listdir(user_path):
            file_path = os.path.join(user_path, filename)
            with open(file_path, "r") as file:
                entries = file.read().split('\n\n')
                for entry in entries:
                    if keyword.lower() in entry.lower():
                        title_line = next((line for line in entry.split('\n') if line.startswith("Title:")),
                                          "Title: Unknown")
                        title = title_line.split("Title: ")[1]
                        date = filename.replace('.txt', '')
                        print(f"Entry: {title} (Date: {date})")
                        found = True
    if not found:
        print("No entries found with that keyword.")


def list_entries(username):
    print("\nList of All Journal Entries for", username)
    journal_dir = f"{JOURNAL_PATH}/{username}"
    entries_dict = {}  # Ensure this dictionary is declared

    if os.path.exists(journal_dir):
        for filename in sorted(os.listdir(journal_dir)):
            date = filename.replace('.txt', '')
            print(f"\nDate: {date}")
            file_path = os.path.join(journal_dir, filename)

            with open(file_path, "r") as file:
                entries = file.read().strip().split('\n\n')  # Split entries by double newline
                for entry in entries:
                    lines = entry.split('\n')
                    title_line = next((line for line in lines if line.startswith("Title: ")), "Title: Unknown")
                    title = title_line.split("Title: ")[1]
                    print(f"  - {title}")
                    entries_dict[title] = entry

    entry_title = input("\nEnter the title of the entry you want to read: ").strip()

    if entry_title in entries_dict:
        print(f"\nReading Entry: {entry_title}")
        print(entries_dict[entry_title])
    else:
        print("Entry not found.")


def main():
    if not os.path.exists(JOURNAL_PATH):
        os.makedirs(JOURNAL_PATH)

    create_admin_account()

    while True:
        user_type = input(
            "Are you an admin (A), a new user (N), a returning user (R), or would you like to quit (Q)? [A/N/R/Q]: ").strip().lower()

        if user_type == 'a':
            username = login()
            if username == ADMIN_USERNAME:
                print(f"Welcome, Admin {username}!")
                while True:
                    print("\nAdmin Actions")
                    print("1. View User Info")
                    print("2. Delete a User")
                    print("3. Create a User")
                    print("4. View User Journals")
                    print("5. Exit")
                    admin_choice = input("Enter choice: ")

                    if admin_choice == '1':
                        view_user_info()
                    elif admin_choice == '2':
                        delete_user(username)
                    elif admin_choice == '3':
                        admin_create_user()
                    elif admin_choice == '4':
                        admin_view_user_journal(username)
                    elif admin_choice == '5':
                        break
                    else:
                        print("Invalid choice. Please try again.")
            else:
                print("Admin login failed.")

        elif user_type in ['n', 'r']:
            if user_type == 'n':
                if not register_user():
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
                    print("7. Exit")
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
                        break
                    else:
                        print("Invalid choice. Please try again.")
            else:
                print("Login failed. Please try again.")

        elif user_type == 'q':
            print("Exiting the program.")
            break

        else:
            print("Invalid selection. Please enter 'A', 'N', 'R', or 'Q'.")


if __name__ == "__main__":
    main()
