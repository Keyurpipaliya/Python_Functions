# generator function using accept student details **kwargs and yields the dictionary.

def student_details():
    while True:
        name = input("Enter student name :");
        age = input("Enter student age :");
        grade = input("Enter student grade :");
        yield {"name": name, "age": age, "grade": grade}
    