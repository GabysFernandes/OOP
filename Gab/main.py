from student import Student
from student_repository import load_student, find_students_by_id, save_student

while True:
    print("\n Student Registry")
    print("1. Add Student")
    print("2. Show all students")
    print("3. Search Students by ID")
    print("4. Exit")

    choice = input("Choose an option: ").strip()

    match choice:
        case "1":
            student_id = input("Student ID: ").strip()
            name = input("Student Name: ").strip()
            course = input("Course: ").strip()

            if not student_id or not name or not course:
                print("A Student with that ID already exist.")
                continue


            student = Student(student_id, name, course)
            save_student(student)
            print("Student Saved!")

        case "2":
            students = load_student()

            if not students:
                print("There are no students saved yet.")
            else:
                print("\n Save Students")
                for student in students:
                    print(student)

        case "3":
            student_id = input("Enter Student ID to search: ").strip()

            student = find_students_by_id(student_id)

            print(student)

        case "4":
            print("Goodbye.")
            break

        case _:
            print("Invalid option, please choose 1, 2, 3 or 4")