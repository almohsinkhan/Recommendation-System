import pandas as pd


data = {
    "movie": [
        "Inception",
        "Inception",
        "Inception",
        "Titanic",
        "Titanic",
        "Avatar",
        "Avatar",
    ],
    "rating": [
        5,
        4,
        5,
        2,
        5,
        4,
        5,
    ],
}

df = pd.DataFrame(data)

recommendations = (
    df.groupby("movie")["rating"]
      .mean()
      .sort_values(ascending=False)
)

print(recommendations)
