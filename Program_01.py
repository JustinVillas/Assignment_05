# Create a program that will ask for grade percentage.
# Display the equivalent Grade/Mark and Description
# Example:
# Input grade: 87.6
# Equivalent Grade/Mark: 1.75
# Description: Very Good
import math

# Steps
# 1. Ask student their grade percentage.
grade_int = float(input("Grade: "))
student_grade = math.ceil(grade_int)
if student_grade >= 97 and student_grade <= 100:
    print("Equivalent: 1.0 ")
    print("Description: Excellent")
elif student_grade >= 94 and student_grade <= 96:
    print("Equivalent: 1.25")
    print("Description: Excellent")
elif student_grade >= 91 and student_grade <= 93:
    print("Equivalent: 1.5")
    print("Description: Very Good")
elif student_grade >= 88 and student_grade <= 90:
    print("Equivalent: 1.75")
    print("Description: Very Good")
elif student_grade >= 85 and student_grade <= 87:
    print("Equivalent: 2.0")
    print("Description: Good")
elif student_grade >= 82 and student_grade <= 84:
    print("Equivalent: 2.25")
    print("Description: Good")
elif student_grade >= 79 and student_grade <= 81:
    print("Equivalent: 2.5")
    print("Description: Satisfactory")
elif student_grade >= 76 and student_grade <= 78:
    print("Equivalent: 2.75")
    print("Description: Satisfactory")
elif student_grade == 75:
    print("Equivalent: 3.0")
    print("Description: Passing")
elif student_grade > 65 and student_grade <= 74:
    print("Grade/Mark: 5.0")
    print("Description: Failure")
else:
    print("Sorry, you've inputed a wrong data. Thank you ")
