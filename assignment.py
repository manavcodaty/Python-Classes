def new_student(db):
    roll_number = input("Enter roll number: ")
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    subject = input("Enter subject: ")
    
    db[roll_number] = {
        "name": name, age: age, "subject": subject, 
    }

    
    
def display_all_students(db):
    for roll_number, student in db.items():
        print(f"Roll number: {roll_number}")
        print(f"Name: {student['name']}")
        print(f"Age: {student['age']}")
        print(f"Subject: {student['subject']}")
        print()
    main()
        
def search_student(db):
    roll_number = input("Enter roll number: ")
    student = db.get(roll_number)
    if student:
        print(f"Roll number: {roll_number}")
        print(f"Name: {student['name']}")
        print(f"Age: {student['age']}")
        print(f"Subject: {student['subject']}")
    else:
        print("Student not found")
    main()
        
def delete_student(db):
    roll_number = input("Enter roll number: ")
    student = db.pop(roll_number, None)
    if student:
        print("Student deleted successfully")
    else:
        print("Student not found")
    main()
        
def update_student(db):
    roll_number = input("Enter roll number: ")
    student = db.get(roll_number)
    if student:
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        subject = input("Enter subject: ")
        student["name"] = name
        student["age"] = age
        student["subject"] = subject
        print("Student updated successfully")
    else:
        print("Student not found")
        
    main()
    
def add_new_student(db):
        num_students = int(input("Enter number of students: "))
        for i in range(num_students):
            new_student(db)
        print("Students added successfully")
        main()
    
    
def main():
    db = dict()
    print("1. Add new student")
    print("2. Display all students")
    print("3. Search student")
    print("4. Delete student")
    print("5. Update student")
    print("6. Exit")
    
    choice = int(input("Enter your choice: "))
    
    
    
    if choice == 1:
        add_new_student(db)
    elif choice == 2:
        display_all_students(db)
    elif choice == 3:
        search_student(db)
    elif choice == 4:
        delete_student(db)
    elif choice == 5:
        update_student(db)
    elif choice == 6:
        return
    else:
        print("Invalid choice")
    
    
    
main()