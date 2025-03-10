import streamlit as st
import pickle
import pandas as pd

# Load the similarity matrix and movies list
similarity = pickle.load(open("similarity.pkl", "rb"))
movies_list = pickle.load(open("movies.pkl", 'rb'))

# Extract movie titles into a list
movies = movies_list['title'].values

# Function to recommend movies based on the selected movie
def recommend(movie):
    # Find the index of the selected movie
    movie_index = list(movies).index(movie)
    
    # Get the similarity scores for the selected movie
    distances = similarity[movie_index]
    
    # Sort the movies based on similarity scores and get the top 5
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    
    recommended_movies = []
    for i in movies_list:
        movie_id = i[0]
        
        recommended_movies.append(movies[i[0]])  # i[0] is the index of the movie
    
    return recommended_movies

# Streamlit UI
st.title('Flix Mate  - A Movie Recommendation System')

# Movie selection dropdown
selected_movie_name = st.selectbox(
    'Select your Favorite Movie: ',
    movies
)

# Recommend movies when button is pressed
if st.button("Recommend"):
    recommendation = recommend(selected_movie_name)
    
    # Display the recommended movies
    for movie in recommendation:
        st.write(movie)
