from collections import defaultdict

# Data structure to store contacts grouped by category
contacts = defaultdict(list)


def add_contact():
    name = input("Enter Name: ")
    group = input("Enter Group (e.g. Family, Friends): ")

    contacts[group].append(name)
    print("Contact added successfully.\n")


def view_contacts():
    if not contacts:
        print("No contacts available.\n")
        return

    for group, names in contacts.items():
        print(f"\n{group}:")
        for name in names:
            print(f"- {name}")
    print()


def delete_contact():
    name = input("Enter Name to delete: ")
    found = False

    for group in list(contacts.keys()):
        if name in contacts[group]:
            contacts[group].remove(name)
            found = True

            # Remove group if empty
            if not contacts[group]:
                del contacts[group]

            print("Contact deleted successfully.\n")
            break

    if not found:
        print("Contact not found.\n")


def main():
    while True:
        print("Welcome to Contact Group Manager\n")
        print("1. Add Contact\n")
        print("2. View Contacts\n")
        print("3. Delete Contact\n")
        print("4. Exit\n")

        choice = input("Choose an option: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            delete_contact()
        elif choice == "4":
            print("Exiting Contact Group Manager.")
            break
        else:
            print("Invalid option. Please try again.\n")


if __name__ == "__main__":
    main()
