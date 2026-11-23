#function using *args to print all student names passed to function.

def student_names(*names):
    for name in names:
        print(name)
        
print("Student names are:")
student_names("keyur", "divy", "pratham", "naval")
