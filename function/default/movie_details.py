
def Movie(movie_name, movie_type, theatre, Area, City):
    Movie = {
        "name": movie_name,
        "type": movie_type,
        "theatre": theatre,
        "area": Area,
        "city": City
    }
    return Movie

print("Movie Details:")
movie1 = Movie(movie_name="Inception", movie_type="Sci-Fi", theatre="C")

            
