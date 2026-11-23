#function using *kwargs to accept product details.

def product_details(**details):
    return details

print("Product details are:", product_details(name="Laptop", brand="Dell", price=50000, color="Black"))