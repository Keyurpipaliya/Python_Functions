# function that accepts multiple numbers using *args and yields each number one by one.

def generate_numbers(*args):
    for num in args:
        yield num
        
num_gen = generate_numbers(1, 2, 3, 4, 5)
for num in num_gen:
    print(num)