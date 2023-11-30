import os
import datetime
from shared_functions import list_entries, read_credentials, write_credentials

# Define the path to the journal entries directory, relative to the current file's location.
JOURNAL_PATH = os.path.join(os.path.dirname(__file__), '..', 'journal_entries')


# Function to allow a user to write a new journal entry.
def write_entry(username):
    # Capture the current date to create a uniquely dated entry file.
    today = datetime.date.today()
    filename = f"{JOURNAL_PATH}/{username}/{today.strftime('%m-%d-%Y')}.txt"

    # Prompt the user for entry details: title, mood, and content.
    title = input("Enter title for your journal entry: ").strip()
    mood = input("How are you feeling today? ").strip()
    content = input("Write your journal entry: ").strip()

    # Ensure the user's journal directory exists; if not, create it.
    if not os.path.exists(f"{JOURNAL_PATH}/{username}"):
        os.makedirs(f"{JOURNAL_PATH}/{username}")

    # Write the user's entry to the file, appending if the file already exists.
    with open(filename, "a") as file:
        file.write(f"Title: {title}\nMood: {mood}\nContent: {content}\n\n")
    print("Journal entry saved.")


# Function to read and display a journal entry from a specific date.
def read_entry(username):
    date_input = input("Enter date (MM/DD/YYYY) to read entries: ")
    try:
        # Parse the user-provided date and format it to match the file naming convention.
        date = datetime.datetime.strptime(date_input, '%m/%d/%Y').date()
        filename = f"{JOURNAL_PATH}/{username}/{date.strftime('%m-%d-%Y')}.txt"

        # If an entry for the given date exists, read and print its contents.
        if os.path.exists(filename):
            with open(filename, "r") as file:
                print(file.read())
        else:
            print("No entries found for this date.")
    except ValueError:
        print("Invalid date format. Please use MM/DD/YYYY.")


# Function to delete a specific journal entry for a user.
def delete_user_entry(username):
    # Check if the journal directory for the user exists.
    journal_dir = f"{JOURNAL_PATH}/{username}"
    if not os.path.exists(journal_dir):
        print("No journal entries found.")
        return

    # List existing entries and prompt the user for the date of the entry to delete.
    list_entries(username)
    entry_date = input("Enter the date of the entry you want to delete (MM-DD-YYYY): ")
    entry_file = f"{journal_dir}/{entry_date}.txt"

    # If the specified entry exists, delete it.
    if os.path.exists(entry_file):
        os.remove(entry_file)
        print(f"Entry for {entry_date} deleted.")
    else:
        print("Entry not found for the specified date.")


# Function to compute and display statistics about the user's journal entries, particularly the mood.
def view_mood_statistics(username):
    print("\nMood Statistics:")
    mood_count = {}

    # Access the user's journal directory and process each entry file.
    user_path = os.path.join(JOURNAL_PATH, username)
    if os.path.isdir(user_path):
        for filename in os.listdir(user_path):
            file_path = os.path.join(user_path, filename)
            with open(file_path, "r") as file:
                entries = file.read().split('\n\n')  # Split the content by entries.
                for entry in entries:
                    # Extract the mood line and update the count for each mood.
                    lines = entry.split('\n')
                    mood_line = next((line for line in lines if line.startswith("Mood:")), None)
                    if mood_line:
                        mood = mood_line.split("Mood: ")[1]
                        mood_count[mood] = mood_count.get(mood, 0) + 1

    # Print the count of each mood found in the entries.
    for mood, count in mood_count.items():
        print(f"{mood}: {count} time(s)")


# Function to search for journal entries that contain a specific keyword.
def search_entries(username, keyword):
    found = False
    user_path = os.path.join(JOURNAL_PATH, username)
    print("\nSearch Results:")

    # Go through each entry file in the user's journal directory.
    if os.path.isdir(user_path):
        for filename in os.listdir(user_path):
            file_path = os.path.join(user_path, filename)
            with open(file_path, "r") as file:
                entries = file.read().split('\n\n')  # Split the content by entries.
                for entry in entries:
                    # Check if the entry contains the keyword and print the title and date if it does.
                    if keyword.lower() in entry.lower():
                        title_line = next((line for line in entry.split('\n') if line.startswith("Title:")),
                                          "Title: Unknown")
                        title = title_line.split("Title: ")[1]
                        date = filename.replace('.txt', '')
                        print(f"Entry: {title} (Date: {date})")
                        found = True

    # If no entries containing the keyword were found, notify the user.
    if not found:
        print("No entries found with that keyword.")


# Function to allow a user to delete their own account.
def delete_own_account(username):
    print(f"Deleting account for {username}...")
    credentials = read_credentials()

    # Check if the user exists in the credentials and delete if present.
    if username in credentials:
        del credentials[username]
        write_credentials(credentials)
        print("Your account has been successfully deleted.")
        return True  # Indicates account deletion was successful
    else:
        print("Account not found.")
        return False
