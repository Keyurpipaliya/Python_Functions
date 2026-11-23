# function using *args to accept any number so integers and return them as tuple

def intergers(*integers):
    return tuple(integers)

print("Integers:", intergers(1, 2, 3, 4, 5))