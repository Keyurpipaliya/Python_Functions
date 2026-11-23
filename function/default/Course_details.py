
def course_details(course_name, instructor, duration, level, price):
    course = {
        "course_name": course_name,
        "instructor": instructor,
        "duration": duration,
        "level": level,
        "price": price,
    }
    for key, value in course.items():
        print(f"{key}: {value}")
        
    print("Course Details:")