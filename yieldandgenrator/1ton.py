# function that accept a number n and yields numbers from 1 to n

def generate_numbers(n):
    for i in range(1, n + 1):
        yield i
        
num_gen = generate_numbers(10)
for num in num_gen:
    print(num)