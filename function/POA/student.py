# function with roll number, name, age as positional only arguments.

def student_info(roll_number, name, age, /):
    print(f"Roll Number: {roll_number}")
    print(f"Name: {name}")
    print(f"Age: {age}")
    
student_info(101, "keyur", 22)