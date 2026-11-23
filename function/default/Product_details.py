
def product_details(product_id, product_name, price):
    details = {
        "Product ID": product_id,
        "Product Name": product_name,
        "Price": price,
    }
    for key, value in details.items():
        print(f"{key}: {value}")
        
product_details(product_id=101, product_name="Laptop", price=1200.00)
print("Product details displayed.")