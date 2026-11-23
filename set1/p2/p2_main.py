# Name: Diana C. Esguerra
# Section: IV - BSIT - B
# Activity: P2 - Custom Module
# Date: November 23, 2026

import student_utils
from datetime import datetime

# Enter student grades
grades = []

number = int(input("How many grades do you want to enter? "))

for i in range(number):
    grade = float(input(f"Enter grade {i + 1} (0-100): "))
    grades.append(grade)

# Display grade report
print("\n===== STUDENT GRADE REPORT =====")
print("Date:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
print("Average:", student_utils.calculate_average(grades))
print("Highest:", student_utils.get_highest_grade(grades))
print("Lowest:", student_utils.get_lowest_grade(grades))
print("Status:", student_utils.determine_status(grades))