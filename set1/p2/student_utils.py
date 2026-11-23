# Name: Diana C. Esguerra
# Section: IV - BSIT - B
# Activity: P2 - Custom Module
# Date: November 23, 2026

# Calculate the average grade
def calculate_average(grades):
    return sum(grades) / len(grades)


# Determine pass or fail
def determine_status(grades):
    if calculate_average(grades) >= 75:
        return "PASSED"
    else:
        return "FAILED"


# Get the highest grade
def get_highest_grade(grades):
    return max(grades)


# Get the lowest grade
def get_lowest_grade(grades):
    return min(grades)