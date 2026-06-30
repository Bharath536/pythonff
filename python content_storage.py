contacts = {
    "Bharath": "9876543210",
    "Ravi": "9123456789",
    "Suresh": "9988776655"
}

name = input("Enter contact name: ")

if name in contacts:
    print("Phone Number:", contacts[name])
else:
    print("Contact not found")