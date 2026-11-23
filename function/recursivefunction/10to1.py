#recursive function to print numbers from 10 to 1

def print_numbers(n):
    if n > 0:
        print(n)
        print_numbers(n - 1)
    
print_numbers(10)