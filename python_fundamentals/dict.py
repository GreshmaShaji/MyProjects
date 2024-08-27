contact_book = {
    "Alice" : 12335,
    "Bob" : 56789,
    "Charlie" : 53424
}

while True:
    print("\n Contact Book Menu:")
    print("1. Add a new contact")
    print("2. Update an existing contact")
    print("3. Delete an existing contact")
    print("4. view all contacts")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        #add a new contact
        name = input("Enter the contact's name: ")
        phone = input("Enter the phone number: ")
        contact_book[name] = phone
        print(f"Added contact: {name}-{phone} \n {contact_book}")

    elif choice == "2":
        #update an existing contact
        name = input("Enter the contact's name to update: ")
        if name in contact_book:
            new_phone = input(f"Enter the new phone numbe for{name}: ")
            contact_book[name] = new_phone
            print(f"Updated contact: {name} - {new_phone} \n {contact_book}")
        else:
            print("Contact not found. ")
    
    elif choice == "3":
        #Delete a contact
        name = input("Enter the name of the contact to delete : ")
        if name in contact_book:
            contact_book.pop(name)
            print(f"Deleted contact: {name} \n { contact_book}")
        else:
            print("Contact not found")

    elif choice == "4":
        #view all contacts
        for name, phone in  contact_book.items():
            print(f"{name}:{phone}")
    
    elif choice == "5":
        #exit the program
        print("Exiting the contact book. Goodbye!")
        break

    else:
        print("Invalid choice. Please select a valid option.")