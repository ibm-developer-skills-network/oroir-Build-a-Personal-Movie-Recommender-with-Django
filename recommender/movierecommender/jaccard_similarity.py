
class Movie():
    def __init__(self):
        self.genres = ""


def jaccard_similarity(list1: list, list2: list) -> float:
    s1 = set(list1)
    s2 = set(list2)
    return float(len(s1.intersection(s2)) / len(s1.union(s2)))


def check_valid_genres(genres: str):
    if bool(genres and not genres.isspace()) and genres != 'na':
        return True
    else:
        return False


def similarity_between_movies(movie1: Movie, movie2: Movie) -> float:
    if check_valid_genres(movie1.genres) and check_valid_genres(movie2.genres):
        m1_generes = movie1.genres.split()
        m2_generes = movie2.genres.split()
        return jaccard_similarity(m1_generes, m2_generes)
    else:
        return 0


movie1 = Movie()
movie1.genres = "animation comedy family "
movie2 = Movie()
movie2.genres = "animation comedy family"
print(similarity_between_movies(movie1, movie2))

movie1 = Movie()
movie1.genres = "animation comedy family"
movie2 = Movie()
movie2.genres = "animation comedy"
print(similarity_between_movies(movie1, movie2))

movie1 = Movie()
movie1.genres = " "
movie2 = Movie()
movie2.genres = "animation comedy"
print(similarity_between_movies(movie1, movie2))

movie1 = Movie()
movie1.genres = " "
movie2 = Movie()
movie2.genres = " "
print(similarity_between_movies(movie1, movie2))


movie1 = Movie()
movie1.genres = "animation"
movie2 = Movie()
movie2.genres = "na"
print(similarity_between_movies(movie1, movie2))


movie1 = Movie()
movie1.genres = "animation"
movie2 = Movie()
movie2.genres = "animation"
print(similarity_between_movies(movie1, movie2))