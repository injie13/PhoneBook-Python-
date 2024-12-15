Phonebook App

Overview
The Phonebook App is a simple Python-based application that allows users to create, read, update, and delete (CRUD) contact information stored in a SQLite database. It is an interactive command-line application that makes it easy to manage contact data such as names, phone numbers, and addresses.

Features
Create Contacts: Add new contact information, including name, phone number, and address.
Read Contacts: Search for a specific contact or view all contacts in the database.
Update Contacts: Modify the phone number or address of an existing contact.
Delete Contacts: Remove a contact from the database.

Installation
Clone the Repository:
git clone <repository_url>
cd PhonebookApp

Set Up Environment:
Make sure you have Python installed on your system (Python 3.7 or later).
Install any necessary dependencies (if applicable):
pip install -r requirements.txt
Run the App:
python phone_book.py

Database Structure
The SQLite database MyContacts.db includes a single table contacts with the following structure:
Column Name | Data Type | Description
id            INTEGER     Primary Key, Auto-Incremented
name          TEXT        Name of the contact (required)
phone         TEXT        Phone number of the contact
address       TEXT        Address of the contact


Usage Instructions

Run the Program:
Execute the script phone_book.py in your terminal:
python phone_book.py

Interactive Menu:
Choose one of the following options:
C - Create a new contact.
R - Read/search for contacts by name.
U - Update an existing contact's details.
D - Delete a contact from the database.
Q - Quit the application.

Input Details:
When prompted, enter the required information (e.g., name, phone number, address).


Code Explanation
Key Functions
create(data):
Inserts new contact information into the database.
Validates and handles SQL syntax errors.

read(name=None):
Searches the database for contacts matching the given name and displays them in a JSON format.
Uses json.dumps to format results.

update(name):
Updates the phone number or address of a contact identified by their name.
Handles cases with multiple matching names.

delete(name):
Deletes a contact from the database by name.
Handles cases with multiple matching names.

Helper Functions:
_update_number(row): Prompts the user to input updated information for a contact.
_delete_number(row): Deletes a contact from the database based on the row ID.

main():
Runs the interactive menu and processes user inputs.

Error Handling
Catches and displays SQL errors (sqlite3.OperationalError and sqlite3.IntegrityError).
Validates user input to prevent crashes.


Sample Output
Example Interaction:

Select one of the following options: Create(C) Read(R) Update(U) Delete(D) or Quit(Q): C
Enter a name: John Doe
Enter a phone number: 123-456-7890
Enter a home address: 456 Elm St
New Record Added!

Select one of the following options: Create(C) Read(R) Update(U) Delete(D) or Quit(Q): R
Enter a name: John
{
  "results": [
    {
      "name": "John Doe",
      "mobile": "123-456-7890",
      "home": "456 Elm St"
    }
  ]
}

Known Issues
The current version uses raw SQL queries, which are susceptible to SQL injection. Switching to parameterized queries is recommended.
Requires input validation for better robustness.


Future Improvements
Add user authentication for secure access.
Implement a GUI using a Python framework like Tkinter or PyQt.
Add support for exporting and importing contacts in CSV or JSON format.
Enhance search functionality with advanced filters.
