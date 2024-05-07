# Define a list of movies with their genres
movies = {
    "The Shawshank Redemption": "Drama",
    "The Godfather": "Crime",
    "The Dark Knight": "Action",
    "Pulp Fiction": "Crime",
    "Forrest Gump": "Drama",
    "Schindler's List": "Drama",
    "The Lord of the Rings: The Return of the King": "Fantasy",
    "Fight Club": "Drama",
    "Inception": "Action",
    "The Matrix": "Action",
    "The Silence of the Lambs": "Thriller",
    "Goodfellas": "Crime",
    "The Godfather: Part II": "Crime",
    "The Lord of the Rings: The Fellowship of the Ring": "Fantasy",
    "The Lord of the Rings: The Two Towers": "Fantasy",
}

# Function to recommend movies based on genre
def recommend_movie(genre):
    recommended_movies = []
    for movie, movie_genre in movies.items():
        if movie_genre == genre:
            recommended_movies.append(movie)
    return recommended_movies

# Main loop of the chatbot
print("Welcome to the Movie Recommendation Chatbot!")
while True:
    print("What genre are you interested in? (Type 'quit' to exit)")
    user_input = input("> ").capitalize()
    if user_input == "Quit":
        print("Thank you for using the Movie Recommendation Chatbot. Goodbye!")
        break
    elif user_input in movies.values():
        recommended_movies = recommend_movie(user_input)
        if recommended_movies:
            print("Here are some recommendations for you:")
            for movie in recommended_movies:
                print("-", movie)
        else:
            print("Sorry, we don't have any recommendations for that genre.")
    else:
        print("Invalid genre. Please try again or type 'quit' to exit.")
