# function using *args to calculate the average of all numbers.

def average_of_all_numbers(*numbers):
    return sum(numbers) / len(numbers)

print("The average of all numbers 10, 20, 30, 40, 50 is:", average_of_all_numbers(10,20,30,40,50));
