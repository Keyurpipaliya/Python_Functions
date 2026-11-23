
def Employee_Details(name, age, department, salary):
    employee = {
        "name": name,
        "age": age,
        "department": department,
        "salary": salary
    }
    for key, value in employee.items():
        print(f"{key}: {value}")
        
    print("Employee Details:")
    