# recursive function to print numbers from 1 to 10.

def print_numbers(n):
    if n <= 10:
        print(n)
        print_numbers(n + 1)
        
print_numbers(1)
