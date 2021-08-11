import pandas as pd
import json
import glob
import shutil


#belongs_to_collection, genres, id, original_title, overview
def filter_data():
    raw_data = pd.read_csv("movies_metadata.csv")
    raw_data = raw_data[["imdb_id", "genres", "original_language", "release_date", "original_title",
                         "overview", "vote_average", "vote_count"]]
    #raw_data['year'].astype('date')
    # Check missing values
    print(raw_data.shape)
    raw_data = raw_data.dropna(subset=["imdb_id", "genres", "overview", "original_title"])
    raw_data['vote_count'] = raw_data['vote_count'].fillna(0)
    raw_data['vote_average'] = raw_data['vote_average'].fillna(0)
    raw_data['original_language'] = raw_data['original_language'].fillna('en')
    raw_data['overview'] = raw_data['overview'].fillna('na')
    raw_data['release_date'] = raw_data['release_date'].fillna('1970-1-1')
    raw_data = raw_data.drop_duplicates(subset='imdb_id', keep="last")
    print(raw_data.isna().sum())
    raw_data['release_date'] = pd.to_datetime(raw_data['release_date'], errors='coerce', format="%Y-%m-%d")
    raw_data['release_date'] = pd.DatetimeIndex(raw_data['release_date']).year
    raw_data['release_date'] = raw_data['release_date'].fillna(1970)
    raw_data['vote_count'] = raw_data['vote_count'].astype('int')
    raw_data['release_date'] = raw_data['release_date'].astype('int')
    raw_data = raw_data[raw_data['release_date'] > 1975]
    raw_data = raw_data[raw_data['vote_count'] > 5]
    print(raw_data.shape)

    raw_data.to_csv("movies.csv", index=False)


def convert_genres_column(genre_column):
    genre_column = genre_column.replace("\'", "\"")
    genre_column = genre_column.lower()
    genres = json.loads(genre_column)
    results = ""
    for genre in genres:
        results += genre["name"] + " "
    return results.strip()


def convert_title(title_column):
    return title_column.lower()


def convert_overview_column(overview_column):
    overview_column = overview_column.replace("\"", "")
    return overview_column


def process_genres():
    raw_data = pd.read_csv("movies.csv")
    raw_data['genres'] = raw_data['genres'].apply(convert_genres_column)
    raw_data['overview'] = raw_data['overview'].apply(convert_overview_column)
    raw_data.to_csv("movies.csv", index=False)


def jaccard_similarity(list1, list2):
    s1 = set(list1)
    s2 = set(list2)
    return float(len(s1.intersection(s2)) / len(s1.union(s2)))


def merge_poster():
    output = "movie_posters.csv"
    with open(output, 'wb') as outfile:
        for file_name in glob.glob("poster/movie_poster_*.csv"):
            if file_name == output:
                # don't want to copy the output into the output
                continue
            with open(file_name, 'rb') as readfile:
                shutil.copyfileobj(readfile, outfile)


def process_data():
    filter_data()
    process_genres()
    movie_df = pd.read_csv("movies.csv")
    poster_df = pd.read_csv("movie_posters.csv")
    movie_df = pd.merge(movie_df, poster_df, on=["imdb_id"])
    movie_df.to_csv("movies.csv", index=False)


# https://image.tmdb.org/t/p/original/
process_data()
