# Task 1
# In this program we show an example of using dictionaries to keep track of information in a phonebook.

def main():
    phonebook = {}
    while True:
        print("\nKashaf Phonebook Menu:")
        print("1. Add contact")
        print("2. Search contact")
        print("3. Delete contact")
        print("4. Exit")
        choice = input("Enter your choice(1, 2, 3, 4): ")

        if choice == "1":
           name = input("Enter contact name: ")
           phone_number = input("Enter contact phone number: ")
           phonebook[name] = phone_number
           print(f"Contact {name} added successfully.\n")
        elif choice == "2":
            name = input("Enter contact name: ")
            if name in phonebook:
                print(f"Contact {name} phone number is {phonebook[name]}.\n")
            else:
                   print(f"Contact {name} not found.\n")
        elif choice == "3":
            name = input("Enter contact name: ")
            if name in phonebook:
                del phonebook[name]
                print(f"Contact {name} deleted successfully.\n")
            else:
                print(f"Contact {name} not found.\n")
        elif choice == "4":
            print("Good Bye!!!")
            break
        else:
            print("Invalid choice. Please Choose valid option.\n")

    
if __name__ == '__main__':
    main()