
def movie(name, type, ticket_price, theatre, city, pincode):
    movie = {
        "name": name,
        "type": type,
        "ticket_price": ticket_price,
        "city": city,
        "theatre": theatre,
        "pincode": pincode,
    }
    for key, value in movie.items():
        print(f"{key}: {value}")
        
    print("Movie Details:")