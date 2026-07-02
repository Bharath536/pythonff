import json
import os

FILE_NAME = "contacts.json"


def load_contacts():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return {}


def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)


contacts = load_contacts()


while True:
    print("\n===== Contact Book =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Search Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter Name: ")
        phone = input("Enter Phone Number: ")
        contacts[name] = phone
        save_contacts(contacts)
        print("Contact Added Successfully.")

    elif choice == "2":
        if contacts:
            print("\nSaved Contacts:")
            for name, phone in contacts.items():
                print(f"{name} : {phone}")
        else:
            print("No Contacts Found.")

    elif choice == "3":
        name = input("Enter Name to Update: ")
        if name in contacts:
            new_phone = input("Enter New Phone Number: ")
            contacts[name] = new_phone
            save_contacts(contacts)
            print("Contact Updated Successfully.")
        else:
            print("Contact Not Found.")

    elif choice == "4":
        name = input("Enter Name to Delete: ")
        if name in contacts:
            del contacts[name]
            save_contacts(contacts)
            print("Contact Deleted Successfully.")
        else:
            print("Contact Not Found.")

    elif choice == "5":
        name = input("Enter Name to Search: ")
        if name in contacts:
            print(f"{name} : {contacts[name]}")
        else:
            print("Contact Not Found.")

    elif choice == "6":
        print("Thank You!")
        break

    else:
        print("Invalid Choice.")