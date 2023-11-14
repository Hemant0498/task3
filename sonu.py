class ContentBasedRecommendationSystem:
    def __init__(self):
        # Movie database with genres as features
        self.movies = {
            'Movie1': {'Action': 1, 'Comedy': 0, 'Drama': 1, 'Sci-Fi': 1},
            'Movie2': {'Action': 0, 'Comedy': 1, 'Drama': 1, 'Sci-Fi': 0},
            'Movie3': {'Action': 1, 'Comedy': 0, 'Drama': 0, 'Sci-Fi': 1},
            'Movie4': {'Action': 0, 'Comedy': 1, 'Drama': 0, 'Sci-Fi': 1},
            # Add more movies and genres as needed
        }

    def recommend_movies(self, user_preferences):
        # Calculate the similarity score between user preferences and each movie
        similarity_scores = {movie: self.calculate_similarity(user_preferences, features) for movie, features in self.movies.items()}

        # Sort movies by similarity score in descending order
        recommended_movies = sorted(similarity_scores, key=similarity_scores.get, reverse=True)

        return recommended_movies[:3]  # Recommend the top 3 movies

    def calculate_similarity(self, user_preferences, movie_features):
        # Simple cosine similarity calculation
        dot_product = sum(user_preferences[genre] * movie_features[genre] for genre in user_preferences)
        magnitude_user = sum(user_preferences[genre] ** 2 for genre in user_preferences) ** 0.5
        magnitude_movie = sum(movie_features[genre] ** 2 for genre in user_preferences) ** 0.5

        if magnitude_user == 0 or magnitude_movie == 0:
            return 0  # Avoid division by zero

        return dot_product / (magnitude_user * magnitude_movie)

# Example usage
recommendation_system = ContentBasedRecommendationSystem()

# User preferences for genres
user_preferences = {'Action': 1, 'Comedy': 0, 'Drama': 1, 'Sci-Fi': 1}

# Recommend movies based on user preferences
user_recommendations = recommendation_system.recommend_movies(user_preferences)
print("Recommendations for the user:", user_recommendations)
