# global variable and modify it inside the function using global keyword.

def modify_global_variable():
    global global_variable
    global_variable = 20
    print("Inside the function, global_variable is modified to:", global_variable)
    
global_variable = 10
print("Before calling the function, global_variable is:", global_variable)

modify_global_variable()
print("After calling the function, global_variable is:", global_variable)



