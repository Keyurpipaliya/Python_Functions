# function using *args to print all even numbers passed to the function.

def even_numbers(*numbers):
    even_nums = [num for num in numbers if num % 2 == 0]
    for num in even_nums:
        print(num)
    
    print("Total even numbers:", len(even_nums))
    