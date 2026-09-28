# Contact-Book Project Report

## 1. Project Title

**Contact-Book**

## 2. Introduction

Contact-Book is a Python-based command-line application designed to store and manage contact information. The program provides a simple text menu through which users can add, view, search, update, and delete contacts.

## 3. Objective

The main objective of this project is to demonstrate basic Python programming concepts in a practical application.

## 4. Technologies Used

- Python 3
- JSON
- Visual Studio Code
- Git and GitHub

## 5. Python Concepts Used

- Functions
- Lists
- Dictionaries
- Loops
- Conditional statements
- `input()`
- Exception handling using `try/except`
- File handling
- JSON data storage

## 6. Main Functions

### `load_data()`
Loads previously saved contacts from `contacts.json`.

### `save_data()`
Stores the current contact list in `contacts.json`.

### `add_contact()`
Adds a new contact containing name, phone, and email.

### `show_all()`
Displays all contacts.

### `search_contact()`
Searches contacts using a name or phone number.

### `update_contact()`
Allows the user to modify an existing contact.

### `delete_contact()`
Removes a selected contact.

### `main()`
Runs the application's menu and controls the program flow.

## 7. Data Storage

Contacts are stored as dictionaries inside a list and saved in JSON format.

Example:

```json
[
    {
        "name": "Rahul",
        "phone": "9876543210",
        "email": "rahul@example.com"
    }
]
```

## 8. Conclusion

The Contact-Book project demonstrates how basic Python programming concepts can be combined to create a useful command-line application. JSON file handling ensures that contacts remain available after the program is closed and opened again.
