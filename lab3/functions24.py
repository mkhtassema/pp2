from movies_data import movies
def average_imdb(movies):
    if not movies:
        return 0  
    return sum(movie["imdb"] for movie in movies) / len(movies)

print(average_imdb(movies)) 