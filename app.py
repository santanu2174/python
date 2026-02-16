import os

def create_file(filename):
    try:
        with open(filename, 'x') as f:
            print(f"File Name {filename} : Created successfully!")
    except FileExistsError:
        print(f'File name {filename} already exist!')

    except Exception as E:
        print("An error occured!")

def view_all_files():
    files = os.listdir()
    if not files:
        print("No file Found!")
    else:
        print(f"Files in directory!")
        for file in files:
            print(file)

def delete_file(filename):
    try:
        os.remove(filename)
        print(f"{filename} has been deleted successfully!")
    except FileNotFoundError:
        print(f"{filename} not found!")

    except Exception as E:
        print('An error occured!')

def read_file(filename):
    try:
        with open('sample.txt', 'r') as f:
            content = f.read()
            print(f"content of '{filename}' : \n{content}")
    except FileNotFoundError:
        print("file not found!")
    except Exception as e:
        print('An error occured!')

def edit_file(filename):
    try:
        with open('sample.txt', 'a') as f:
            content = input("enter data to add = ")
            f.write(content + "\n")
            print(f'Content added to {filename} successfully!')
    except FileNotFoundError:
        print('File not found')
    except Exception:
        print('An error occured!')

def main():
    while True:
        print('----File mangement App----')
        print("\nSelect- 1: Create File\n2: View All Files\n3: Delete File\n4: Read Files\n5: Edit File\n6: Exit app\n")
        try:
            choice = int(input("Enter Your Choice: "))
        except ValueError:
            print("Please enter a valid number")
            continue
        if choice == 1:
            filename = input('Enter the file name to create: ')
            create_file(filename)
        elif choice == 2:
            view_all_files()
        elif choice == 3:
            filename = input("Enter your file name to Delete file : ")           
            delete_file(filename)
        elif choice == 4:
            filename = input("Enter your file name to Read : ")
            read_file(filename)
        elif choice == 5:
            filename = input("Enter your file name to edit: ")
            edit_file(filename)
        elif choice == 6:
            print("Close the programme!")
            break   
        else:
            print("Invalid Input")

if __name__ == "__main__":
    main()