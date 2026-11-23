# function that accepts a students marks and returns 'pass' or 'fail'.

def student_marks(marks):
    if marks >= 40:
        return "Pass"
    else:
        return "Fail"

print("Student has:", student_marks(45))
