def is_highly_rated(movie):
    return movie["imdb"] > 5.5

print(is_highly_rated({"name": "Usual Suspects", "imdb": 7.0, "category": "Thriller"}))  
print(is_highly_rated({"name": "AlphaJet", "imdb": 3.2, "category": "War"})) 