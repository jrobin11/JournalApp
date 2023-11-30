import os
import datetime
from shared_functions import list_entries, read_credentials, write_credentials

# Assuming the journal_entries directory is at the same level as the src directory
JOURNAL_PATH = os.path.join(os.path.dirname(__file__), '..', 'journal_entries')

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

def delete_user_entry(username):
    journal_dir = f"{JOURNAL_PATH}/{username}"
    if not os.path.exists(journal_dir):
        print("No journal entries found.")
        return

    list_entries(username)
    entry_date = input("Enter the date of the entry you want to delete (MM-DD-YYYY): ")
    entry_file = f"{journal_dir}/{entry_date}.txt"

    if os.path.exists(entry_file):
        os.remove(entry_file)
        print(f"Entry for {entry_date} deleted.")
    else:
        print("Entry not found for the specified date.")

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


def delete_own_account(username):
    print(f"Deleting account for {username}...")
    credentials = read_credentials()

    if username in credentials:
        del credentials[username]
        write_credentials(credentials)
        print("Your account has been successfully deleted.")
        return True  # Indicates account deletion was successful
    else:
        print("Account not found.")
        return False
