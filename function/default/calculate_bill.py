
def calculate_bill(price, quantity, discount=20):
    total = price * quantity
    discounted_total = total - (total * discount / 100)
    return discounted_total

for i in range(1, 4):
    price = float(input(f"Enter the price of item {i}: "))
    quantity = int(input(f"Enter the quantity of item {i}: "))
    bill_amount = calculate_bill(price, quantity)
    print(f"The total bill amount for item {i} is: {bill_amount}")
    
print("Bill calculation completed.")    