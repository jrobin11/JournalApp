 # Memory Lane - Journal Application

## Description
Memory Lane is a user-friendly, command-line diary application tailored for elderly users to easily record and revisit their daily thoughts and memories. It is designed to run smoothly on basic computer systems, enabling users to write new entries, read old ones, and search through entries by dates or keywords. The app stores each entry in a simple text file format, ensuring accessibility and simplicity. By providing a digital space for reflective writing, Memory Lane aims to offer therapeutic benefits and a sense of nostalgia, enhancing the mental well-being of its users. This project also serves as a practical application of file system and mass-storage system concepts, demonstrating the real-world utility of these computing fundamentals.

## Setup and Installation
To set up the Memory Lane application, follow these steps:

### Prerequisites
- Python 3.x
- Access to a command-line interface


### Installation

1. **Cloning the Repository**

   First, clone the repository to your local machine using Git:

   ```bash
   git clone git@github.com:jrobin11/JournalApp.git
   cd JournalApp

### Installing Dependencies
- Memory Lane does not require external dependencies. It utilizes standard Python libraries.

### Running the Application
- To run Memory Lane, navigate to the project directory and execute the main script:

    ```bash
    python main.py

### Usage
- Upon running the application, users will be prompted to either log in as an admin, create a new user account, or log in as a returning user. The application provides various functionalities based on the user role:
  - Admins can:
    - View and manage user accounts
    - Create new users
    - Access user journals.
  - Regular Users:
    - write new journal entries
    - Read previous entries
    - Delete their entries
    - Search through their journal.
  - For more detailed instructions, follow the prompts provided by the application.

 # Understanding Mass-Storage Systems

Mass-Storage Systems refer to the storage of large amounts of data in a persistently accessible manner. In computing, this typically involves hard drives, SSDs, and other forms of non-volatile memory. These systems are crucial for storing data that needs to be retained over long periods, even when the system is powered off.

## Application of Mass-Storage Systems in Memory Lane

1. **Data Storage and Retrieval:**
    - **User Data:** Memory Lane stores user credentials and journal entries in a structured format on the mass storage of the host system (usually a hard drive or SSD). This approach ensures data persistence across sessions and reboots.
    - **Journal Entries:** Each journal entry is saved in a text file, identified by the user's name and the date of entry (formatted as MM-DD-YYYY.txt). This method makes it easy to retrieve entries by date, as well as to list all entries for a user.

2. **Directory Structure:**
    - The application maintains a directory named `journal_entries`, where each user has a dedicated subdirectory.
    - Within each user's subdirectory, journal entries are stored in separate text files. This organization mimics a basic file system hierarchy, leveraging the underlying mass storage's capability to manage directories and files.

3. **JSON for Credentials:**
    - User credentials are stored in a `credentials.json` file. This file acts as a simple database.
    - JSON (JavaScript Object Notation) is used for its human-readable format and ease of use within Python. It allows for a structured representation of user data, including usernames, hashed passwords, emails, and ages.

4. **Hashing for Security:**
    - Passwords are hashed using SHA-256, a cryptographic hash function. This ensures that actual passwords are not stored on the disk, enhancing security.
    - Hashing is a one-way process, crucial for securely storing passwords. When a user logs in, the entered password is hashed and compared with the stored hash.

5. **Admin and User Data Handling:**
    - **Admin Functions:** Admins have the ability to view, create, and delete user accounts. When an admin function is executed, the application interacts with the `credentials.json` file to perform the required operations.
    - **User Functions:** Users can create journal entries, read existing ones, delete entries, and search through their journals. Each of these actions involves reading from or writing to the mass storage system.

## Behind the Scenes: How Data is Managed

- **Writing Data:** When a journal entry is created or a new user is registered, the application writes to the mass storage. It either appends data to an existing file (in the case of journal entries) or updates the `credentials.json` file.
- **Reading Data:** Retrieval of journal entries involves reading the appropriate text files from the user's directory. For login and admin functionalities, the application reads the `credentials.json` file.
- **Searching and Listing:** To list entries or search through them, the application scans through the directory and files, reading their contents to find matches.

## Conclusion

In Memory Lane, mass storage is not just a passive repository of data but an active part of the application's functionality. It provides a reliable and persistent means to store and manage user data and journal entries, ensuring data integrity and security. The use of directories and files for storing journal entries, along with JSON for user credentials, demonstrates an effective use of the file system and mass-storage systems in a practical application. This setup, while simple, is robust enough to handle the core functionalities expected in a digital journal application, making it particularly suited for elderly users who value ease of use and reliability.
