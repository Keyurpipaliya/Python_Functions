# function that accepts number and returns its square and cube.

def square_and_cube(num):
    square = num ** 2
    cube = num ** 3
    return (square, cube)

print("The square and cube of 3 are:", square_and_cube(3))