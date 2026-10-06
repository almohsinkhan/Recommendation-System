import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


movies = pd.read_csv("../data/movies.csv")

print(movies)

vectorizer =CountVectorizer(
	tokenizer=lambda x:x.split("|")
)

genre_matrix = vectorizer.fit_transform(movies["genres"])

print(genre_matrix.toarray())

similarity = cosine_similarity(genre_matrix)

print(similarity)

def recommend(movie_title, n=3):

    movie_index = movies[
        movies["title"] == movie_title
    ].index[0]

    scores = list(
        enumerate(similarity[movie_index])
    )

    scores = sorted(
        scores,
        key=lambda x: x[1],
        reverse=True
    )

    recommendations = []

    for index, score in scores[1:n+1]:
        recommendations.append(
            (movies.iloc[index]["title"], score)
        )

    return recommendations

print(recommend("Inception"))
