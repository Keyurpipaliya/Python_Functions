 
def bank_details(bank_name, account_number, ifsc_code, branch_name, city):
    details = {
        "bank_name": bank_name,
        "account_number": account_number,
        "ifsc_code": ifsc_code,
        "branch_name": branch_name,
        "city": city
    }
    for key, value in details.items():
        print(f"{key}: {value}")
        
    print("Bank Details:");
    