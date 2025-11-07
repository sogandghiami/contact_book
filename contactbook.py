from pathlib import Path
import json

filename = Path("contacts.json")

def read_contacts():
    if filename.exists():
        text = filename.read_text()
        if text.strip():
            return json.loads(text)
    return {}  

def save_contacts(data):
    filename.write_text(json.dumps(data, indent=4))

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")

    contacts = read_contacts()


    contacts[name] = {"phone": phone, "email": email}
    save_contacts(contacts)

    print(f"Contact '{name}' added successfully!")

def show_contacts():
    contacts = read_contacts()
    if not contacts:
        print("You have no contacts yet.")
    else:
        print("\nYour contacts:")
        for name, info in contacts.items():
            print(f"- {name}: {info['phone']} | {info['email']}")

def remove_contact():
    contacts = read_contacts()
    if not contacts:
        print("No contacts to remove.")
        return

    name = input("Enter the name of the contact to remove: ")

    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print(f"Contact '{name}' removed.")
    else:
        print("Contact not found.")

while True:
    print("\n--- Contact Manager ---")
    print("1. Show contacts")
    print("2. Add contact")
    print("3. Remove contact")
    print("4. Exit")

    choice = input("> ")

    if choice == "1":
        show_contacts()
    elif choice == "2":
        add_contact()
    elif choice == "3":
        remove_contact()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again.")


