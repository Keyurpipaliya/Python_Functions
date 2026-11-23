# function that student_info(sid, sname, /) and call it correctly using positional arguments.

def student_info(sid, sname, /):
    print(f"Student ID: {sid}")
    print(f"Student Name: {sname}")
    

student_info(1, "keyur")

print("Student Information:")