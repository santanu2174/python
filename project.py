student_grade = {}

#Add s new student
def add_student(name,grade):
    student_grade[name] = grade  #[santanu] = 100
    print(f"Added {name} with a {grade}")

#update student
def update_student(name,grade):
    if name in student_grade:
        student_grade[name] = grade
        print("{name} with marks are updated {grade}")

    else:
        print("name is not found!")

#delete student
def del_student(name):
    if name in student_grade:
        del student_grade[name]
        print(f"{name} is successfully deleted!")
    else:
        print("not found!")

#view all
def display_all_student():
    if student_grade:
        for name, grade in student_grade.items():
            print(f"{name}: {grade}")
    else:
        print("no data found")

def main():
    while True:
        print("\n----Student Grade Management System----")
        print("\nSelect 1-ADD Student\n2-Update Student\n3-Delete Student\n4-List All Student\n5-Exit\n")

        choice = int(input("Enter Your choice: "))
        if choice == 1:
            name = input("Enter student name: ")
            grade = int(input("Enter student grade: "))
            add_student(name,grade)
        elif choice == 2:
            name = input("Enter student name: ")
            grade = int(input("Enter student grade: "))
            update_student(name, grade)
        elif choice == 3:
            name = input("enter student name: ")
            del_student(name)
        elif choice == 4:
            print("List of all students")
            display_all_student()
        elif choice == 5:
            print("exit the pogramme")
            break
        else:
            print("invalid inputs")

if __name__ == "__main__":
    main()




            




