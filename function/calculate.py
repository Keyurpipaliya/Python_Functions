#calculate that accept three numbers and returns their sum, average, maximum and minimum.

def calculate(num1, num2, num3):
    total_sum = num1 + num2 + num3
    average = total_sum / 3
    maximum = max(num1, num2, num3)
    minimum = min(num1, num2, num3)
    return total_sum, average, maximum, minimum

print("Enter three numbers:")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

sum, avg, max_val, min_val = calculate(num1, num2, num3)
print(f"Sum: {sum}, Average: {avg}, Maximum: {max_val}, Minimum: {min_val}")
