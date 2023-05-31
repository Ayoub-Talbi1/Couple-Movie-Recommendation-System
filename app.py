import streamlit as st
import pandas as pd
from recommandation_system import give_rec, find_common_recommendations, select_recommended_movie
from PIL import Image

# Load the movie dataset and other necessary data
movies_encoded = pd.read_csv('movies_encoded.csv')
placeholder_option = "Select a movie..."

# Set the logo image path
logo_image_path = 'imgs/logo.png'

# Load the logo image
logo_image = Image.open(logo_image_path)

# Create a container for the header
header_container = st.container()

# Add the logo to the header container
with header_container:
    # Set the layout for the header
    st.columns([1, 10])  # Adjust the column widths as needed
    logo_col, header_col = st.columns([1, 10])

    # Add the logo to the left column
    with logo_col:
        st.image(logo_image, use_column_width=True)

    # Add the header text to the right column
    with header_col:
        st.title('MOVIE DATE')

# Create two dropdowns to select movies for each person
movie_1 = st.selectbox('Select a movie for person 1', [placeholder_option] + movies_encoded['Title'].tolist())
movie_2 = st.selectbox('Select a movie for person 2', [placeholder_option] + movies_encoded['Title'].tolist())

# Button to compute the recommended movie
compute_button = st.button('Compute Recommended Movie')

# Check if the compute button is clicked and both movies are selected
if compute_button and movie_1 != placeholder_option and movie_2 != placeholder_option:
    # Call the give_rec() function to get recommended movies for each person
    recommendations_1 = give_rec(movie_1)
    recommendations_2 = give_rec(movie_2)

    # Find the intersection of recommended movies
    common_recommendations = find_common_recommendations(recommendations_1, recommendations_2)

    # Select a recommended movie
    recommended_movie = select_recommended_movie(common_recommendations, recommendations_1)

    # Display the recommended movie or a warning message
    st.success(f"Based on your selections, a movie that suits both of your preferences is: {recommended_movie}")
    movie_poster_url = movies_encoded.loc[movies_encoded['Title'] == recommended_movie, 'Poster_Url'].values[0]
    #st.image(movie_poster_url, width=200)
    st.markdown(
        f'<div style="display: flex; justify-content: center;"><img src="{movie_poster_url}" alt="Movie Poster" width="200"/></div>',
        unsafe_allow_html=True)