# student details that accept rollno, name and age and print all details.

def student(rollno, name, age):
    details = {
        "Roll Number": rollno,
        "Name": name,
        "Age": age,
    }
    for key, value in details.items():
        print(f"{key}: {value}")