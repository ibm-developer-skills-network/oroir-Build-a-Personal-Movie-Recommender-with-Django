import requests
import json
import pandas as pd
import time


def get_request(url, **kwargs):
    # print(kwargs)
    # If argument contain API KEY
    #print("GET from {} ".format(url))
    try:
        params = dict()
        params["api_key"] = kwargs["api_key"]
        params["external_source"] = "imdb_id"
        response = requests.get(url, params=params, headers={'Content-Type': 'application/json'})
    except Exception as e:
        # If any error occurs
        print(e)
        return None
    status_code = response.status_code
    #print("With status {} ".format(status_code))
    json_data = json.loads(response.text)
    return json_data


def get_movie_by_imdbid(imdb_id):
    base_url = "https://api.themoviedb.org/3/find/" + imdb_id
    api_key = "8f235d3515774a8d17e2bab6bc6ba9d2"
    json_result = get_request(base_url, api_key=api_key)
    if json_result is not None:
        movies = json_result["movie_results"]
        if len(movies) == 1:
            movie_doc = movies[0]
            #print(imdb_id)
            #print(movie_doc["title"])
            #print(movie_doc["poster_path"])
            if movie_doc["poster_path"] is not None:
                return movie_doc["poster_path"]
            else:
                return "na"
    else:
        return "na"


def get_movie_posters():
    movie_df = pd.read_csv("ormtemplate/movies.csv")
    rows_list = []
    for index, row in movie_df.iterrows():
        dict = {}
        imdb_id = row['imdb_id']
        dict["imdb_id"] = imdb_id
        dict["poster_path"] = get_movie_by_imdbid(imdb_id)
        rows_list.append(dict)
        time.sleep(0.05)

        if index != 0 and index % 1001 == 0:
            # Reach every 1000 posters, save to csv
            print(f"{index} out of 40000 movies queried")
            new_movie_df = pd.DataFrame(rows_list)
            new_movie_df.to_csv(f"poster/movie_poster_{index}.csv", index=False)
            # Clear up the list
            rows_list.clear()

    if len(rows_list) > 0:
        new_movie_df = pd.DataFrame(rows_list)
        new_movie_df.to_csv("poster/movie_poster_final.csv", index=False)

#get_movie_by_imdbid("tt0114709")
get_movie_posters()
