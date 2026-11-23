# function that yields numbers from 1 to 10

def generate_numbers():
    for i in range(1, 11):
        yield i
        
num_gen = generate_numbers()
for num in num_gen:
    print(num)