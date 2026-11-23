# recursive function to calculate the sum of the first n natural numbers

def sum_of_natural_numbers(n):
    if n <= 0:
        return 0
    else:
        return n + sum_of_natural_numbers(n - 1)
    
print("Enter a positive integer:")
print(sum_of_natural_numbers(int(input())))
