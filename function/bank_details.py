# bank details that accept account number, customer name, and balance. call the function using both positional and keyword arguments seperatly.

def bank_details(account_number, customer_name, balance):
    details = {
        "Account Number": account_number,
        "Customer Name": customer_name,
        "Balance": balance,
    }
    for key, value in details.items():
        print(f"{key}: {value}")
        
print("Bank Details using Positional Arguments:")
bank_details("1234567890", "Alice Smith", 5000.75)

print("\nBank Details using Keyword Arguments:")
bank_details(balance=5000.75, customer_name="Alice Smith", account_number="1234567890")

