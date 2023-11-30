# Project Report

## Memory Lane - Journal Application
Author: Jahidul Robin Mitkumar Patel

### ABSTRACT
Memory Lane is a command-line diary application designed to enhance the mental well-being of elderly users. This project demonstrates the application of computing concepts in creating user-friendly software that facilitates reflective writing and memory preservation. The software is developed in Python and uses a simple file system for data storage, ensuring ease of use and accessibility. Key functionalities include user registration, journal entry creation, and entry management. This project aligns with CMPSC 472's focus on practical software development and user-centric design.

### INTRODUCTION
Memory Lane is a user-friendly, command-line diary application tailored for elderly users to easily record and revisit their daily thoughts and memories. It is designed to run smoothly on basic computer systems, enabling users to write new entries, read old ones, and search through entries by dates or keywords. The app stores each entry in a simple text file format, ensuring accessibility and simplicity. By providing a digital space for reflective writing, Memory Lane aims to offer therapeutic benefits and a sense of nostalgia, enhancing the mental well-being of its users. This project also serves as a practical application of file system and mass-storage system concepts, demonstrating the real-world utility of these computing fundamentals.

### OBJECTIVES
The primary goals of Memory Lane include:
- Providing a simple, accessible platform for the elderly to document their daily experiences.
- Facilitating mental well-being through reflective writing.
- Demonstrating the application of file system management in a real-world software project.

### SYSTEM REQUIREMENTS
Following are the system requirements of the application:
1. Unix/Linux operating system (tested and programmed on Ubuntu 20)
2. Python 3

### SETUP AND INSTALLATION

#### Cloning the Repository
To clone the repository to your local machine, use the following Git command:
```bash
git clone git@github.com:jrobin11/JournalApp.git
cd JournalApp
```
Installing Dependencies
Memory Lane does not require external dependencies. It utilizes standard Python libraries.

Running the Application
To run Memory Lane, navigate to the project directory and execute the main script:
```bash
python main.py
```

### BACKGROUND
A brief review of existing literature reveals a growing need for digital tools that cater to the elderly. Studies indicate that engaging in reflective writing and memory sharing can significantly enhance mental health in older adults. This project aligns with CMPSC 472's objectives by applying theoretical knowledge in a practical, user-centered context.

### USAGE
Upon running the application, users will be prompted to either log in as an admin, create a new user account, or log in as a returning user. The application provides various functionalities based on the user role.

- For Admin Users:
  1. View and manage user accounts
  2. Create new users
  3. Access user journals.

- For Regular Users:
- 1. Write new journal entries
  2. Read previous entries
  3. Delete their entries
  4. Search through their journal.

For more detailed instructions, follow the prompts provided by the application.

### SIGNIFICANCE OF THE PROJECT
The Journal Application, Memory Lane, stands out as a meaningful project that significantly contributes to enhancing the life of the elderly. At its heart, the application is more than just a tool for recording daily experiences; it is a companion that offers emotional support and cognitive stimulation, which are vital components of elderly care.

The significance of the project is multi-faceted. Firstly, it provides an avenue for self-expression and reflection, allowing users to document their thoughts, feelings, and memories. This can be incredibly therapeutic, serving as a form of self-care and helping to maintain mental health. For many elderly individuals, reminiscing through journaling can strengthen cognitive functions and offer a sense of accomplishment and purpose.

Secondly, Memory Lane includes mood tracking functionalities that encourage users to engage actively with their emotional well-being. By reflecting on their mood over time, users can identify patterns and triggers, potentially aiding in early detection of emotional health issues. Such features empower the elderly to take charge of their mental health and seek support when needed.

Moreover, the project addresses the need for user-friendly technology that is tailored to the capabilities and needs of the elderly. The simple and intuitive design minimizes the learning curve, making technology more accessible and less intimidating. This inclusivity not only bridges the digital divide but also fosters a sense of connection and empowerment.

Finally, the project’s significance extends to the social sphere. By potentially integrating sharing features in the future, Memory Lane can help the elderly stay connected with their family and friends, sharing their life stories and maintaining social ties. Such social engagement is crucial in combating loneliness and isolation, which are common challenges faced by the elderly population.

### METHODOLOGY
The project adopted an agile development methodology, which fostered a flexible and iterative approach to the software's design and implementation. Python was chosen as the primary programming language due to its readability and simplicity, which aligns with the project’s aim of creating an accessible application for the elderly. The development team utilized Git for version control, enabling efficient collaboration and tracking of changes throughout the project lifecycle. Regular meetings were a cornerstone of the process, allowing for consistent communication regarding progress, hurdles, and iterative feedback integration. A user-centric design philosophy was paramount, guiding the development to ensure that the application remained intuitive and navigable for the elderly demographic.

### SOFTWARE DESIGN AND IMPLEMENTATION
The software's architecture is characterized by a modular design, facilitating ease of maintenance and scalability. Each module has a focused responsibility—user authentication, journal entry processing, or administrative functions—enhancing the clarity and separation of concerns within the codebase. The user interface eschews complexity in favor of a command-line interface, a deliberate choice to cater to elderly users who may prefer straightforward interactions over more complex graphical user interfaces. Core functionalities are comprehensive, spanning user registration, secure login processes, journal entry creation, reading, searching, and management, as well as mood tracking. Administrative features allow for the oversight of user accounts, ensuring the system’s integrity and the privacy of user data.

### UNDERSTANDING MASS-STORAGE SYSTEMS

#### Application of Mass-Storage Systems in Memory Lane

##### Data Storage and Retrieval:
User Data: Memory Lane stores user credentials and journal entries in a structured format on the mass storage of the host system (usually a hard drive or SSD). This approach ensures data persistence across sessions and reboots.
Journal Entries: Each journal entry is saved in a text file, identified by the user's name and the date of entry (formatted as MM-DD-YYYY.txt). This method makes it easy to retrieve entries by date, as well as to list all entries for a user.
##### Directory Structure:
The application maintains a directory named journal_entries, where each user has a dedicated subdirectory.
Within each user's subdirectory, journal entries are stored in separate text files. This organization mimics a basic file system hierarchy, leveraging the underlying mass storage's capability to manage directories and files.
##### JSON for Credentials:
User credentials are stored in a credentials.json file. This file acts as a simple database.
JSON (JavaScript Object Notation) is used for its human-readable format and ease of use within Python. It allows for a structured representation of user data, including usernames, hashed passwords, emails, and ages.
##### Hashing for Security:
Passwords are hashed using SHA-256, a cryptographic hash function. This ensures that actual passwords are not stored on the disk, enhancing security.
Hashing is a one-way process, crucial for securely storing passwords. When a user logs in, the entered password is hashed and compared with the stored hash.
##### Admin and User Data Handling:
Admin Functions: Admins have the ability to view, create, and delete user accounts. When an admin function is executed, the application interacts with the credentials.json file to perform the required operations.
User Functions: Users can create journal entries, read existing ones, delete entries, and search through their journals. Each of these actions involves reading from or writing to the mass storage system.

### BEHIND THE SCENES: HOW DATA IS MANAGED
- Writing Data: When a journal entry is created or a new user is registered, the application writes to the mass storage. It either appends data to an existing file (in the case of journal entries) or updates the credentials.json file.
- Reading Data: Retrieval of journal entries involves reading the appropriate text files from the user's directory. For login and admin functionalities, the application reads the credentials.json file.
- Searching and Listing: To list entries or search through them, the application scans through the directory and files, reading their contents to find matches.

### STRUCTURE OF THE CODE
- main.py: Serves as the central hub, orchestrating the flow of the application. It handles user role selection (Admin, New User, Returning User) and directs users to the appropriate functionalities. Central controller that prompts for user roles and delegates actions to either the user_module.py or admin_module.py based on the selection.
- shared_functions.py: Contains functions used across different parts of the application, including user authentication (login and registration), credential management, and listing journal entries. This module acts as a utility belt shared by both user and admin modules, offering common functionalities like user registration, login, and credential management.
- user_module.py: Dedicated to user-specific functionalities. It includes features for writing, reading, deleting journal entries, viewing mood statistics, searching entries, and deleting a user's own account. Handles all user-level interactions with the journal, including entry creation, reading, and mood analysis. It relies on shared_functions.py for user authentication and entry listing.
- admin_module.py: Focuses on administrative functions, such as creating and managing user accounts, viewing user information, and accessing user journals. Administers user account management, such as creating and deleting user accounts, and provides the ability to view user journal entries. It also utilizes shared_functions.py for user data operations.

![image](https://github.com/jrobin11/JournalApp/assets/62670195/6f54ba40-110a-429f-adf6-a51c356e8767)

The arrows indicate the direction of interaction, showing how main.py communicates with the user and admin modules, and how both these modules, in turn, make use of the shared functions provided by shared_functions.py. This structured approach ensures a separation of concerns, with each module focusing on a specific aspect of the application's functionality.

### FUNCTIONALITIES AND TEST RESULTS
(This section should detail the functionalities provided by the application and any test results that validate the performance and reliability of those functionalities.)

### DISCUSSION
The development of the Journal Application, Memory Lane, involved a series of challenges and learning experiences that were instrumental in achieving a product that is both functional and user-centric. Throughout the project, key issues were encountered, such as ensuring the intuitive usability for the elderly, maintaining data integrity, and implementing a secure yet simple authentication system.
One of the primary challenges was the design of a user interface that would cater to the elderly demographic, who may not be as familiar with digital applications. This was addressed by adopting a straightforward command-line interface with clear instructions, reducing cognitive load and potential frustration. Another significant concern was the security of user data, particularly sensitive journal entries. To tackle this, we implemented SHA-256 hashing for passwords, although the static nature of the admin credentials remains an area for improvement.
The project also faced the task of efficient data handling, as the application needed to manage a potentially large number of journal entries. The file-based system was chosen for its simplicity and ease of use, which proved sufficient for current needs but may require a more scalable solution like a database system in the future.
Additionally, the process highlighted the importance of testing and validation. Rigorous testing was conducted to ensure each module functioned correctly, leading to the discovery and fixing of several bugs that could have impacted user experience. This iterative process of testing and refinement has been invaluable.
The application of course learnings to a real-world project like Memory Lane has been thoroughly enlightening. Concepts such as modular programming were directly applied to enhance code maintainability and readability. The project also provided insights into practical issues such as error handling and user input validation, which are often overlooked in theoretical learning.

### CONCLUSION
In Memory Lane, the concept of mass storage transcends being merely a passive data repository, playing an integral role in the application's functionality. It offers a reliable and enduring solution for storing and managing user data and journal entries, thereby ensuring data integrity and security. The strategic use of directories and files for journal entries, coupled with JSON for user credentials, exemplifies an efficient and practical application of file system and mass storage technologies.

This simplistic yet robust approach aligns seamlessly with the core functionalities expected in a digital journal application, making it particularly appealing to elderly users who prioritize ease of use and dependability. Moreover, the project encapsulates a harmonious blend of technical proficiency and user-centric design, reflecting the successful application of course learnings in creating a meaningful digital solution.

Looking ahead, Memory Lane has the potential to evolve into a more advanced platform. By integrating recommendations for future enhancements such as an interactive GUI, advanced security measures, and cloud-based storage, the application can further elevate its user experience and adapt to the changing needs of its audience. This project not only stands as a significant achievement in addressing the specific needs of the elderly through technology but also sets a foundation for continued innovation in socially impactful software development.

### RECOMMENDATIONS FOR FUTURE WORK
While the current iteration of the journal application successfully meets its initial objectives, there are several avenues for future enhancements that could significantly elevate its utility, especially for the elderly user base. First, incorporating a more interactive and visually appealing graphical user interface (GUI) would greatly enhance user experience, making the application more accessible and engaging for users who might be less familiar with text-based interfaces. Integrating voice recognition technology could also be a key development, allowing users to dictate their journal entries, which is particularly beneficial for those with limited mobility or difficulty typing. Additionally, implementing advanced security features such as two-factor authentication would provide users with increased confidence in the privacy and safety of their personal entries. The application could also benefit from a cloud-based storage system, ensuring data persistence and accessibility across different devices. This feature would be particularly useful for users who switch between devices or require backup functionalities. Social features like sharing entries with designated family members or friends could also be explored, fostering a sense of community and shared experience among users. Moreover, expanding the mood analysis feature to include trend analysis over time could offer valuable insights into the user's emotional well-being, potentially serving as a tool for mental health monitoring. Lastly, considering the integration of accessibility features like text-to-speech and customizable text sizes would make the application more inclusive, catering to users with varying degrees of visual impairment. These enhancements would not only improve the overall functionality and appeal of the application but also ensure its adaptability to the evolving needs and preferences of its elderly user base.
