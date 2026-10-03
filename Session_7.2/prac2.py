# Create a dictionary-based program to manage contacts.
contacts={}
while True:
    print("1. Add Contacts")
    print("2. Delete Contact")
    print("3. Search Contact")
    print("4. Display Contact")
    print("5. Exit")

    choice=int(input("Enter your choice: "))
    if choice == 1:
        print("Add Contacts")
        name=input("Enter name:")
        mobile_no=input("Enter mobile number:")

        contacts[name]=mobile_no
        print("Contact added successfully")

    elif choice == 2:
        print("Delete Contact")
        name=input("Enter name to delete contact:")
        del contacts[name]
        print(f"The contact with name {name} is deleted")

    elif choice == 3:
        print("Search Contact")
        name=input("Enter name to search contact:")
        if name in contacts:
            print("Contact found:",contacts[name])
        else:
            print("Contact not found")
    elif choice == 4:
        print("\nContacts:")
        for name, mobile_no in contacts.items():
            print(name, ":", mobile_no)

    elif choice == 5:
        print("Exiting....")
        break

    else:
        print("Invalid choice.")