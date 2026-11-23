# function using *args that counts how many values are passed the function.

def count_values(*values):
    return len(values)

print("The number of values passed to the function is:", count_values(1, 2, 3, 4, 5))

