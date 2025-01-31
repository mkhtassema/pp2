from movies_data import movies
def get_movies_by_category(movies, category):
    return [movie for movie in movies if movie["category"] == category]

romance_movies = get_movies_by_category(movies, "Romance")
print([movie["name"] for movie in romance_movies]) 