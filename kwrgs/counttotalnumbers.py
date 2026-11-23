# function using *kwargs and count the total number of key-value pairs recieved.

def count_total_numbers(**kwargs):
    return len(kwargs)

print("Total number of key-value pairs received:", count_total_numbers(name="keyur", age=20, account_no=101, balance=50000, city="surat"))