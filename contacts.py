"""
Contact-Book
A simple command-line contact management system using Python and JSON.
"""

import json
from pathlib import Path

DATA_FILE = Path("contacts.json")


def load_data():
    """Load contacts from the JSON file."""
    if not DATA_FILE.exists():
        return []

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data if isinstance(data, list) else []
    except (json.JSONDecodeError, OSError):
        print("Warning: Could not read contacts.json. Starting with an empty contact list.")
        return []


def save_data(contacts):
    """Save contacts to the JSON file."""
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as file:
            json.dump(contacts, file, indent=4)
    except OSError as error:
        print(f"Error saving contacts: {error}")


def add_contact(contacts):
    """Add a new contact."""
    print("\n--- Add Contact ---")

    name = input("Enter name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return

    phone = input("Enter phone: ").strip()
    email = input("Enter email: ").strip()

    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }

    contacts.append(contact)
    save_data(contacts)
    print("Contact added successfully.")


def show_all(contacts):
    """Display all saved contacts."""
    print("\n--- All Contacts ---")

    if not contacts:
        print("No contacts found.")
        return

    for index, contact in enumerate(contacts, start=1):
        print(f"\n{index}.")
        print(f"   Name : {contact.get('name', '')}")
        print(f"   Phone: {contact.get('phone', '')}")
        print(f"   Email: {contact.get('email', '')}")


def search_contact(contacts):
    """Search contacts by name or phone number."""
    print("\n--- Search Contact ---")
    keyword = input("Enter name or phone to search: ").strip().lower()

    if not keyword:
        print("Search value cannot be empty.")
        return

    results = [
        contact for contact in contacts
        if keyword in contact.get("name", "").lower()
        or keyword in contact.get("phone", "").lower()
    ]

    if not results:
        print("No matching contact found.")
        return

    for index, contact in enumerate(results, start=1):
        print(f"\n{index}. {contact.get('name', '')}")
        print(f"   Phone: {contact.get('phone', '')}")
        print(f"   Email: {contact.get('email', '')}")


def update_contact(contacts):
    """Update an existing contact."""
    print("\n--- Update Contact ---")

    if not contacts:
        print("No contacts available.")
        return

    show_all(contacts)

    try:
        number = int(input("\nEnter contact number to update: "))
        if number < 1 or number > len(contacts):
            print("Invalid contact number.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    contact = contacts[number - 1]

    print("Press Enter to keep the existing value.")

    name = input(f"Name [{contact['name']}]: ").strip()
    phone = input(f"Phone [{contact['phone']}]: ").strip()
    email = input(f"Email [{contact['email']}]: ").strip()

    if name:
        contact["name"] = name
    if phone:
        contact["phone"] = phone
    if email:
        contact["email"] = email

    save_data(contacts)
    print("Contact updated successfully.")


def delete_contact(contacts):
    """Delete an existing contact."""
    print("\n--- Delete Contact ---")

    if not contacts:
        print("No contacts available.")
        return

    show_all(contacts)

    try:
        number = int(input("\nEnter contact number to delete: "))
        if number < 1 or number > len(contacts):
            print("Invalid contact number.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    deleted = contacts.pop(number - 1)
    save_data(contacts)
    print(f"Contact '{deleted['name']}' deleted successfully.")


def main():
    """Run the Contact-Book application."""
    contacts = load_data()

    while True:
        print("\n" + "=" * 40)
        print("           CONTACT-BOOK")
        print("=" * 40)
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        print("=" * 40)

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            show_all(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            update_contact(contacts)
        elif choice == "5":
            delete_contact(contacts)
        elif choice == "6":
            print("Thank you for using Contact-Book!")
            break
        else:
            print("Invalid choice. Please select 1-6.")


if __name__ == "__main__":
    main()
