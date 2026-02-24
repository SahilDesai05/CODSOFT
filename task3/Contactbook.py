import json

# Global filename for persistence
CONTACTS_FILE = "contacts_data.json"

def load_data():
    """Tries to open the file and load existing contacts"""
    try:
        with open(CONTACTS_FILE, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        # Return empty dict if file doesn't exist or is corrupted
        return {}

def save_data(contacts):
    """Saves the dictionary to our JSON file"""
    with open(CONTACTS_FILE, 'w') as f:
        json.dump(contacts, f, indent=4)

def main():
    # Start by loading our saved contacts
    contacts = load_data()

    while True:
        print("\n--- PERSONAL CONTACT BOOK ---")
        print("1. Add Contact")
        print("2. View All")
        print("3. Search")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("\nSelect an option: ")

        if choice == '1':
            # Add Contact Logic
            phone = input("Enter Phone Number: ").strip()
            if phone in contacts:
                print("Error: This number already exists!")
            else:
                name = input("Enter Name: ")
                email = input("Enter Email: ")
                address = input("Enter Address: ")
                contacts[phone] = {
                    "name": name, 
                    "email": email, 
                    "address": address
                }
                print(f"Contact for {name} saved successfully.")

        elif choice == '2':
            # View Contacts (Name and Phone only as requested)
            if not contacts:
                print("Your contact book is empty.")
            else:
                print("\n--- CONTACT LIST ---")
                for phone, info in contacts.items():
                    print(f"Name: {info['name']} | Phone: {phone}")

        elif choice == '3':
            # Search by Name or Phone
            query = input("Search (Name or Phone): ").lower()
            found = False
            for phone, info in contacts.items():
                if query in phone or query in info['name'].lower():
                    print(f"\nFound: {info['name']}")
                    print(f"Phone: {phone}\nEmail: {info['email']}\nAddress: {info['address']}")
                    found = True
            if not found:
                print("No contact found matching that search.")

        elif choice == '4':
            # Update Logic
            phone = input("Enter the Phone Number of the contact to update: ")
            if phone in contacts:
                print("Keep blank to keep current details.")
                name = input(f"New Name [{contacts[phone]['name']}]: ") or contacts[phone]['name']
                email = input(f"New Email [{contacts[phone]['email']}]: ") or contacts[phone]['email']
                address = input(f"New Address [{contacts[phone]['address']}]: ") or contacts[phone]['address']
                
                contacts[phone] = {"name": name, "email": email, "address": address}
                print("Contact updated!")
            else:
                print("Number not found.")

        elif choice == '5':
            # Delete Logic
            phone = input("Enter Phone Number to delete: ")
            if phone in contacts:
                confirm = input(f"Delete {contacts[phone]['name']}? (y/n): ")
                if confirm.lower() == 'y':
                    del contacts[phone]
                    print("Contact removed.")
            else:
                print("Not found.")

        elif choice == '6':
            # Save and close
            save_data(contacts)
            print("Changes saved. Closing...")
            break
        
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
