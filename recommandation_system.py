import pandas as pd
import random
from sklearn.metrics.pairwise import cosine_similarity

movies_encoded = pd.read_csv('movies_encoded.csv')
similarity = cosine_similarity(movies_encoded.drop(columns=['Release_Date', 'Title', 'Overview', 'Poster_Url']))
indices = pd.Series(movies_encoded.index, index=movies_encoded['Title']).drop_duplicates()


def give_rec(title, sim=similarity):
    # Get the index corresponding to original_title
    idx = indices[title]

    # Get the pairwise similarity scores
    sim_scores = list(enumerate(sim[idx]))

    # Sort the movies
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Scores of the 20 most similar movies
    sim_scores = sim_scores[1:21]

    # Movie indices
    movie_indices = [i[0] for i in sim_scores]

    # Top 10 most similar movies
    return list(movies_encoded['Title'].iloc[movie_indices])


def find_common_recommendations(recommendations_1, recommendations_2):
    common_recommendations = set(recommendations_1).intersection(recommendations_2)
    return common_recommendations


def select_recommended_movie(common_recommendations, recommendations_1):
    if common_recommendations:
        if len(common_recommendations) == 1:
            recommended_movie = common_recommendations.pop()
        else:
            recommended_movie = random.choice(list(common_recommendations))
        return recommended_movie
    else:
        return random.choice(recommendations_1)
