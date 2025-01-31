from movies_data import movies  

def get_movies_by_category(movies, category):
    return [movie for movie in movies if movie["category"] == category]

def average_imdb_by_category(movies, category):
    category_movies = get_movies_by_category(movies, category)
    if not category_movies:
        return 0  
    return sum(movie["imdb"] for movie in category_movies) / len(category_movies)

print(average_imdb_by_category(movies, "Romance"))