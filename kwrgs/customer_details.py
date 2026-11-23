# function using *kwargs to accept bank customer details.

def customer_details(**details):
    return details

print("Customer details are:", customer_details(name="keyur", age=20, account_no=101, balance=50000, city="surat"))