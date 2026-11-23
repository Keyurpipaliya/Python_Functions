# program where local variable and global variable have same name. print their values inside the function.

def local_and_global():
    num = 10  # local variable
    print("Local variable num:", num)

num = 20  
local_and_global()
print("Global variable num:", num) 