from movies_data import movies
def get_highly_rated_movies(movies):
    return [movie for movie in movies if movie["imdb"] > 5.5]

filtered_movies = get_highly_rated_movies(movies)
print([movie["name"] for movie in filtered_movies])  