import requests
from collections import namedtuple


MovieResult = namedtuple(
    'MovieResult',
    'imdb_code, title, duration, director, year, rating, imdb_score, keywords,'
    'genres'
)


def find_movies(search):
    if not search or not search.strip():
        raise ValueError('Search text is required.')
    url = "http://movie_service.talkpython.fm/api/search/{}".format(search)
    r = requests.get(url)
    r.raise_for_status()

    movie_data = r.json()
    movies_list = movie_data.get('hits')

    movies = [MovieResult(**movie) for movie in movies_list]
    movies = sorted(movies, key=lambda x: x.year)
    return movies