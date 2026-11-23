# employee_details that accept empid, name and salary and print all details.

def employee(empid, name, salary):
    details = {
        "Employee ID": empid,
        "Name": name,
        "Salary": salary,
    }
    for key, value in details.items():
        print(f"{key}: {value}")
        