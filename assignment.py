def add_student(students):
    roll = int(input("Enter roll number: "))
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    subject = input("Enter subject: ")
    students[roll] = (name, age, subject)
    print("Student added successfully!")


def update_student(students):
    roll = int(input("Enter roll number of the student to update: "))
    if roll in students:
        name = input("Enter new name: ")
        age = int(input("Enter new age: "))
        subject = input("Enter new subject: ")
        students[roll] = (name, age, subject)
        print("Student updated successfully!")
    else:
        print("Student not found!")


def delete_student(students):
    roll = int(input("Enter roll number of the student to delete: "))
    if roll in students:
        del students[roll]
        print("Student deleted successfully!")
    else:
        print("Student not found!")


def search_student(students):
    roll = int(input("Enter roll number of the student to search: "))
    if roll in students:
        print("Student found!")
        print(
            f"Name: {students[roll][0]}, Age: {students[roll][1]}, Subject: {students[roll][2]}"
        )
    else:
        print("Student not found!")


def print_students(students):
    print("List of students:")
    for roll in students:
        print(
            f"Roll number: {roll}, Name: {students[roll][0]}, Age: {students[roll][1]}, Subject: {students[roll][2]}"
        )


if __name__ == "__main__":
    students = {}
    while True:
        print("\n1. Add student")
        print("2. Update student")
        print("3. Delete student")
        print("4. Search student")
        print("5. Print students")
        print("6. Quit")
        option = int(input("Enter your option: "))
        if option == 1:
            add_student(students)
        elif option == 2:
            update_student(students)
        elif option == 3:
            delete_student(students)
        elif option == 4:
            search_student(students)
        elif option == 5:
            print_students(students)
        elif option == 6:
            break
        else:
            print("Invalid option!")
