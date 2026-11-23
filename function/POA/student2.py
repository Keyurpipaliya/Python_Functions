# function where name is positional and city and salary Try diferent valid functon only.

def student_info(name, /, city, salary):
    print(f"Student Name: {name}")
    print(f"City: {city}")
    print(f"Salary: {salary}")
    
student_info("keyur", city="surat", salary=50000)

