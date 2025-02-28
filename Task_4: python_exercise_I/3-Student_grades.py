"""
This program identifies students with grades above 90 from a list of student names and grades.
The user enters the number of students, followed by each student's name and grade. The program
then counts and displays the number of students with grades above 90, along with their details.
"""

def count_top_students(grades):
    """
    Identifies students with grades above 90.

    Args:
        grades (dict): A dictionary where keys are student names (str) and values are grades (int).

    Returns:
        tuple: A tuple containing:
            - The count of students with grades above 90 (int).
            - A dictionary of students with grades above 90 (dict).
    """
    toppers = {}
    for name, grade in grades.items():
        if grade > 90:
            toppers[name] = grade
    return len(toppers), toppers


# Instructions for the user
print("1. You will first enter the total number of students.")
print("2. For each student, you will enter their name (as text) and their grade (as a number).")
# Input validation for the number of students
while True:
    try:
        num_students = int(input("Enter the number of students: "))
        if num_students > 0:
            break
        else:
            print("Please enter a positive integer for the number of students.")
    except ValueError:
        print("Invalid input. Please enter a valid integer for the number of students.")

# Allow user to input student data dynamically
student_grades = {}
for i in range(num_students):
    print(f"\nEnter details for student {i + 1}:")
    name = input("   Enter the name of the student: ").strip()  # Remove extra spaces

    # Input validation for the grade
    while True:
        try:
            grade = int(input("   Enter the grade of the student (as a number): "))
            if 0 <= grade <= 100:  # Ensure grade is between 0 and 100
                break
            else:
                print("Grade must be between 0 and 100. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid integer for the grade.")

    student_grades[name] = grade

# Count top students and get their details
count, toppers = count_top_students(student_grades)

print(f"\nNumber of students with grades above 90: {count}")
print("Students with grades above 90:", toppers)
