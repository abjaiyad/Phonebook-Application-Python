# I use a dictionary
phonebook = {}

# I need repetition
while True:

    print("\n===== PHONEBOOK MENU =====")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. Display All Contacts")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter Name: ")
        number = input("Enter Phone Number: ")

        if name in phonebook:
            print("Contact already exists.")
        
        else:
            phonebook[name] = number
            print("Contact Added Successfully.")
    
    elif choice == "2":
        name = input("Enter Name to Search: ")
        if name in phonebook:
            print("Phone Number:", phonebook[name])

        else:
            print("Contact Not Found.")

    elif choice == "3":
        name = input("Enter Name to Delete: ")
        if name in phonebook:
            del phonebook[name]
            print("Contact Deleted.")
        
        else:
            print("Contact Not Found.")
    
    elif choice == "4":
        if len(phonebook) == 0:
            print("Phonebook is Empty.")
        
        else:
            print("\nAll Contacts:")

            for name, number in  phonebook.items():
                print(name, ":", number)

    elif choice == "5":
        print("Thank You.")
        break

    else:
        print("Invalid Choice.")