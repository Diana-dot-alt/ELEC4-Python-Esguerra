# Name: Diana C. Esguerra
# Section: IV - BSIT - B
# Activity: P3 - Student Record Manager
# Date: November 23, 2026

# Store student names
students = []

# Add a student
def add_student():
    name = input("Enter student name: ").strip()

    if name.lower() in [student.lower() for student in students]:
        print("Student already exists!")
    else:
        students.append(name)
        print("Student added successfully!")
        
# Remove a student
def remove_student():
    name = input("Enter student name to remove: ").strip()

    for student in students:
        if student.lower() == name.lower():
            students.remove(student)
            print("Student removed successfully!")
            return

    print("Student not found!")

# Search for a student
def search_student():
    name = input("Enter student name to search: ").strip().lower()

    found = [student for student in students if name in student.lower()]

    if found:
        print("\nSearch Results:")
        for student in found:
            print(student)
    else:
        print("Student not found!")

# Display all students
def display_students():
    if not students:
        print("No student records found.")
    else:
        print("\n===== STUDENT RECORDS =====")

        for number, student in enumerate(sorted(students, key=str.lower), start=1):
            print(f"{number}. {student}")

        print(f"Total Students: {len(students)}")

# Display the menu
def show_menu():
    print("\n===== STUDENT RECORD MANAGER =====")
    print("[1] Add Student")
    print("[2] Remove Student")
    print("[3] Search Student")
    print("[4] Display Students")
    print("[5] Exit")

# Main program
def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            remove_student()
        elif choice == "3":
            search_student()
        elif choice == "4":
            display_students()
        elif choice == "5":
            print("Thank you!")
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()


# Lists and Sets:
# A list stores student names and allows changes.
# A set stores unique values and prevents duplicates.
# This program uses a list to manage student records.
# Duplicate names are checked before adding a student.