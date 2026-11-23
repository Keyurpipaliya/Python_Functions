# student info and call it using keyword arguments in diffrent order.

def student_info(name, age, grade):
    print(f"Student Name: {name}")
    print(f"Age: {age}")
    print(f"Grade: {grade}")
    

print("Student Information:")
student_info(grade="10th Grade", age=16, name="John Doe")