import os
students = []

def add_student():
    num_students = int(input("Enter the number of students: "))
    
    for i in range(num_students):
        student = {}
        student["name"] = input("Enter the name of the student: ")
        student["age"] = input("Enter the age of the student: ")
        student["gender"] = input("Enter the gender of the student: ")
        students.append(student)
        
def remove_student():
    name = input("Enter the name of the student to remove: ")
    for student in students:
        if student["name"] == name:
            students.remove(student)
            print("Student removed successfully")
            break
    else:
        print("Student not found")
        
def view_student():
    name = input("Enter the name of the student to view: ")
    for student in students:
        if student["name"] == name:
            print(f"Name: {student['name']}")
            print(f"Age: {student['age']}")
            print(f"Gender: {student['gender']}")
            break
    else:
        print("Student not found")
        
def display_all_students():
    for student in students:
        print(f"Name: {student['name']}")
        print(f"Age: {student['age']}")
        print(f"Gender: {student['gender']}")
        
def update_student():
    name = input("Enter the name of the student to update: ")
    for student in students:
        if student["name"] == name:
            student["name"] = input("Enter the name of the student: ")
            student["age"] = input("Enter the age of the student: ")
            student["gender"] = input("Enter gender of student")
    



def start():
    print("Welcome to Student Database")
    print("1. Add Student")
    print("2. Remove Student")
    print("3. View Student")
    print("4. Display all students")
    print("5. Update Student")
    print("6. Restart Program")
    print("7. Exit Program")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        add_student()
    elif choice == 2:
        remove_student()
    elif choice == 3:
        view_student()
    elif choice == 4:
        display_all_students()
    elif choice == 5:
        update_student()
    elif choice == 6:
        os.system("python3 student_database.py")
    elif choice == 7:
        os.exit()