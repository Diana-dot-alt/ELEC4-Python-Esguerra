# Name: Diana C. Esguerra
# Section: IV - BSIT - B
# Activity: P1 - Student Grade Calculator
# Date: November 23, 2026


# Function 1: Accept student's grades
def enter_grades():
    grades = []

    number_of_grades = int(input("How many grades do you want to enter? "))

    for i in range(number_of_grades):
        while True:
            try:
                grade = float(input(f"Enter grade {i + 1} (0-100): "))

                if 0 <= grade <= 100:
                    grades.append(grade)
                    break
                else:
                    print("Invalid grade! Enter a grade from 0 to 100.")

            except ValueError:
                print("Invalid input! Please enter a number.")

    return grades


# Function 2: Calculate average
def calculate_average(grades):
    return sum(grades) / len(grades)


# Function 3: Get highest grade
def get_highest_grade(grades):
    return max(grades)


# Function 4: Get lowest grade
def get_lowest_grade(grades):
    return min(grades)


# Function 5: Determine pass or fail
def determine_status(grades):
    average = calculate_average(grades)

    if average >= 75:
        return "PASSED"
    else:
        return "FAILED"


# Function 6: Display the menu
def show_menu():
    print("\n===== STUDENT GRADE CALCULATOR =====")
    print("[1] Enter Student Grades")
    print("[2] View Grade Results")
    print("[3] Exit")


# Main program
def main():
    grades = []

    while True:
        show_menu()

        choice = input("Enter your choice: ")

        if choice == "1":
            grades = enter_grades()
            print("\nGrades successfully entered!")

        elif choice == "2":
            if len(grades) == 0:
                print("\nPlease enter grades first.")
            else:
                print("\n===== STUDENT GRADE RESULTS =====")
                print(f"Average Grade: {calculate_average(grades):.2f}")
                print(f"Highest Grade: {get_highest_grade(grades)}")
                print(f"Lowest Grade: {get_lowest_grade(grades)}")
                print(f"Status: {determine_status(grades)}")

        elif choice == "3":
            print("\nThank you for using the Student Grade Calculator!")
            break

        else:
            print("\nInvalid choice! Please select 1, 2, or 3.")


# Run the program
if __name__ == "__main__":
    main()

# Local and Global Variables:
# Local variables are used only inside a function.
# Global variables can be used in different functions.
# In this program, grades is a local variable inside main().
# No global variables are used.