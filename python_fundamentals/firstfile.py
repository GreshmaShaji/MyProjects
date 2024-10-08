movie_database = {
    "Interstellar": ["Adventure", "Drama", "Sci-Fi"],
    "Ant-Man 2015": ["Superhero","Heist"],
    "Kantara": ["Action","Adventure", "Drama"],
    "Inception": ["Action", "Adventure", "Sci-Fi"],
    "Kaithi": ["Action","Adventure", "Crime"],
    "Guardians of the Galaxy": ["Action","Adventure", "Comedy"],
    "The Matrix": ["Action", "Sci-Fi"],
    "The Shawshank Redemption": ["Drama"],
    "Forrest Gump": ["Drama", "Romance"],
    "The Godfather": ["Crime", "Drama"],
    "Spider-Man: Into the Spider-Verse": ["Animation", "Action", "Adventure"],
    "Avengers: Endgame": ["Action", "Adventure", "Sci-Fi"],
    "The Lion King": ["Animation", "Adventure", "Drama"],
    "Pulp Fiction": ["Crime", "Drama"],
    "Parasite": ["Drama", "Thriller"],
    "Guardians of the Galaxy": ["Action", "Adventure", "Sci-Fi"],
    "Jurassic Park": ["Adventure", "Sci-Fi", "Thriller"]

}

user_genre = input("Enter your preference: ").split(',')

recommended_movie = []

for movie , genres in movie_database.items():
    for genre in genres:
        if genre in user_genre:
            recommended_movie.append(movie)
            break
        

if recommended_movie:
    print("Recommended movies based on your preferences: ",','.join(recommended_movie))
else:
    print("Sorry, no movies found")