# rectangle area that accept length and width and returns area.

def rectangle_area(length, width):
    return length * width

rectangle_length = float(input("Enter the length of the rectangle: "))
rectangle_width = float(input("Enter the width of the rectangle: "))

area = rectangle_area(rectangle_length, rectangle_width)
print("The area of the rectangle is:", area)


