# function that prints "Task Started" returns the kwargs ditionary, and observe whether the code after return execute.

def task_started(**kwargs):
    print("Task Started")
    return kwargs
    print("This code will not execute after return statement.")
    
print("Task started with details:", task_started(task_id=101, task_name="Data Processing", priority="High"))