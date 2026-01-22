students = []

def calculate_grade(score):
    if score >= 70:
        return "A"
    elif score >= 60:
        return "B"
    elif score >= 50:
        return "C"
    elif score >= 45:
        return "D"
    else:
        return "F"

def add_student():
    name = input("Enter student name: ")
    score = int(input("Enter student score: "))
    grade = calculate_grade(score)
    students.append({"name": name, "score": score, "grade": grade})
    print("Student record added successfully.\n")

def view_students():
    if not students:
        print("No student records available.\n")
        return

    print("\nSTUDENT RESULT LIST")
    for student in students:
        print(f"Name: {student['name']}, Score: {student['score']}, Grade: {student['grade']}")
    print()

while True:
    print("STUDENT RESULT MANAGEMENT SYSTEM")
    print("1. Add Student")
    print("2. View Student Results")
    print("3. Exit")

    choice = input("Select an option: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        print("Exiting system...")
        break
    else:
        print("Invalid option. Try again.\n")
