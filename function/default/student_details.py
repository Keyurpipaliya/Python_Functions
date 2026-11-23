#student_details with city='pune' as default argument and print all details.

def student_details(rollno, name, age, city='pune'):
    details = {
        "Roll Number": rollno,
        "Name": name,
        "Age": age,
        "City": city,
    }
    for key, value in details.items():
        print(f"{key}: {value}")
    
print("Student Details:")
student_details(rollno=101, name="John Doe", age=16)
