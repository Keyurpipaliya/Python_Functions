# function that accepts employee details and returns a formatted string containing all employee information.

def employee_details(name, age, department, salary):
    return f"Employee Name: {name}, Age: {age}, Department: {department}, Salary: ${salary}"

print("Employee Details:", employee_details("John Doe", 30, "Engineering", 75000))
