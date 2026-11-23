# function using *kwargs to accept employee information such as eid, ename, salary and city.

def employee_information(**info):
    return info

print("Employee information is:", employee_information(eid=101, ename="keyur", salary=50000, city="surat"))