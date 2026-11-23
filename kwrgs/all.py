#function using *kwargs to print all key value pairs.

def print_key_value_pairs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
        
print("Key value pairs are:")