import os

def create_file(filename):
    try:
        with open('filename', 'x') as f:
            print(f"File Name : {filename} created successfully!")
        except FileExistsError:
            print(f"File name {filename} already exist!")
        except Exception:
            print("Error occoured!")
def view_all_files():
    files = os.listdir()
    if not files:
        print("file not found!")
    else:
        print("files in directory!")
        for file in files:
            print(file)
    

def delete_file(filename):
    try:
        os.remove(filename)
        print(f"{filename} deleted successfully!")
    except FileNotFoundError:
        print(f"{filename} not found!")
    except Exception:
        print("error occured!")










def main():
    while True:
        print("---File manegement System----")
        print("\nSelect \n1-Add File\n2-View All Files\n3-Delete File\n4-Read File\n5-Edit File\n6-Exit App\n")

        choice = int(input("Enter your choice: "))
        if choice == 1:
            filename = input("Enter your file name: ")
            create_file(filename)
        elif choice == 2:
            print("All Files are: ")
            view_all_files()
        elif choice == 3:
            filename = input("Enter your file name to Delete: ")
            delete_file(filename)