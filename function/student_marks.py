# student_marks() that students name and marks in three subjects and print the total marks and percentage.

def student_marks(name, marks):
    total_marks = sum(marks)
    percentage = (total_marks / (len(marks) * 100)) * 100 
    print(f"Student Name: {name}")
    print(f"Total Marks: {total_marks}")
    print(f"Percentage: {percentage:.2f}%")
    
         
    