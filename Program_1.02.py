import math


def round_dec(n):
    if n - math.floor(n) < 0.5:
        return math.floor(n)
    return math.ceil(n)


def student_grade():
    student_int = float(input("Grade: "))
    grade = round_dec(student_int)
    if grade >= 97 and grade <= 100:
        print("Equivalent: 1.0 ")
        print("Description: Excellent")
    elif grade >= 94 and grade <= 96:
        print("Equivalent: 1.25")
        print("Description: Excellent")
    elif grade >= 91 and grade <= 93:
        print("Equivalent: 1.5")
        print("Description: Very Good")
    elif grade >= 88 and grade <= 90:
        print("Equivalent: 1.75")
        print("Description: Very Good")
    elif grade >= 85 and grade <= 87:
        print("Equivalent: 2.0")
        print("Description: Good")
    elif grade >= 82 and grade <= 84:
        print("Equivalent: 2.25")
        print("Description: Good")
    elif grade >= 79 and grade <= 81:
        print("Equivalent: 2.5")
        print("Description: Satisfactory")
    elif grade >= 76 and grade <= 78:
        print("Equivalent: 2.75")
        print("Description: Satisfactory")
    elif grade == 75:
        print("Equivalent: 3.0")
        print("Description: Passing")
    elif grade >= 65 and grade <= 74:
        print("Grade/Mark: 5.0")
        print("Description: Failure")
    else:
        print("Sorry, you've inputed a wrong data. Thank you ")
    return grade


def issues():
    print("-------------------------------------------------------------------")
    print("Do you have a remarks get of INC(Incomplete), W(Withdraw), or D(Dropout)?")
    answer = input("NO/YES: ").upper()
    if answer == "YES":
        print("-------------------------------------------------------------------")
        print(
            "Sorry to said that you are subjected to fail this semester. Consult your teachers if you could do something about it. "
        )
    else:
        print("-------------------------------------------------------------------")
        print(
            "Congratulation student, you've gained the fruits of your hardwork.You deserve a virtual applause. "
        )
    return answer


student_grade()
issues()
