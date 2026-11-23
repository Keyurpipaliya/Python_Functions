# product details that accept pid, pname and price and print all details.

def product(pid, pname, price):
    details = {
        "Product ID": pid,
        "Product Name": pname,
        "Price": price,
    }
    for key, value in details.items():
        print(f"{key}: {value}")
        
    print("Total Price with Tax:", price + (price * 0.18))  