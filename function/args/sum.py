# function using *args to accept calculate the sum of any number of values.

def sum_of_values(*values):
    return sum(values)

print("The sum of values 1, 2, 3, 4, 5 is:", sum_of_values(1, 2, 3, 4, 5))