# shared_functions.py
import json
import os
import hashlib
import getpass

CREDENTIALS_PATH = "credentials.json"
JOURNAL_PATH = "../journal_entries"

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

def login():
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")
    hashed_password = hash_password(password)

    credentials = read_credentials()
    if username in credentials and credentials[username]["password"] == hashed_password:
        return username
    return None

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

def display_users():
    print("List of Users:")
    credentials = read_credentials()
    for user in credentials:
        print(user)

def list_entries(username):
    journal_dir = f"{JOURNAL_PATH}/{username}"
    entries_dict = {}

    if os.path.exists(journal_dir):
        for filename in sorted(os.listdir(journal_dir)):
            date = filename.replace('.txt', '')
            print(f"\nDate: {date}")
            file_path = os.path.join(journal_dir, filename)

            with open(file_path, "r") as file:
                entries = file.read().strip().split('\n\n')
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
