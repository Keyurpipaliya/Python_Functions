# student details with and call it once without passing the city and once by passing the city as an diffrent city.

def student_details2(rollno, name, age, city='pune'):
    details = {
        "Roll Number": rollno,
        "Name": name,
        "Age": age,
        "City": city,
    }
    for key, value in details.items():
        print(f"{key}: {value}")
        
student_details2(rollno=1, name="keyur", age=20)
student_details2(rollno=2, name="smit", age=22, city="Mumbai")

print("Student details printed successfully.")