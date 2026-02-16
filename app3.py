contact = {}


def create_contact(name,phone,email,address):
    contact[name] = [phone,email,address]
    print(f"Contact {name} added successfully!")

def view_contact():
    if contact:
        for name,info in contact.items():
            print(f'Name: {name}')
            print(f'phone: {info[0]}')
            print(f'email: {info[1]}')
            print(f'address: {info[2]}')
    else:
        print("No contact found!")

def edit_contact(name):
    if name in contact:
        print("what you want to edit : 1.phone\n2.email\n3.address\n")
        edit_choice = int(input("enter your choice: "))
        if edit_choice == 1:
            new_phone = input("Enter new phone number: ")
            contact[name][0] = new_phone
            print("phone number updated succefully!")
        elif edit_choice == 2:
            new_email = input("enter New Email: ")
            contact[name][1] = new_email
            print("email updated successfully!")
        elif edit_choice == 3:
            new_address = input('Enter new address: ')
            contact[name][2] = new_address
            print("address updated successfully!")
        else:
            print("invalid choice!")
    else:
        print("name not found!")


def delete_contact(name):
    if name in contact:
        del contact[name]
        print(f"{name} has been deleted successfully!")
    else:
        print("name not found!")

def search_contact(name):
    if name in contact:
        print(f"Name: {name}")
        print(f"Phone: {contact[name][0]}")
        print(f"Email: {contact[name][1]}")
        print(f"Address: {contact[name][2]}")
    else:
        print("name not fond!")

def count_contact():
    print(f"Total Contacts: {len(contact)}")


def main():
    while True:
        print("----Contact Book App----")
        print("\n1. Create contact\n2. View Contact\n3. Edit contact\n4.Delete Contact\n5. Search Contact\n6. Count contact\n7. exit\n")
        try:
            choice = int(input("enter your choice: "))
        except ValueError:
            print("please enter valid choice")
        except Exception as e:
            print("An error occured!")
        if choice == 1:
            name = input("Enter Your name: ")
            phone = input("Enter your phone number: ")
            email = input("Enter your email: ")
            address = input("Enter your address: ")
            create_contact(name,phone,email,address)
        elif choice == 2:
            view_contact()
        elif choice == 3:
            name = input("Enter Your name for edit: ")
            edit_contact(name)
        elif choice == 4:
            name = input("Enter Your name for delete: ")
            delete_contact(name)
        elif choice == 5:
            name = input("Enter Your name for search: ")
            search_contact(name)
        elif choice == 6:
            count_contact()
        elif choice == 7:
            print("Exit the programme!")
            break
        else:
            print("Invalid Input")

if __name__ == "__main__":
    main()
            
            