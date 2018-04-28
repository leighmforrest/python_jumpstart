import requests
import collections


URL = 'http://movie_service.talkpython.fm/api/search/'
MovieResult = collections.namedtuple(
    'MovieResult',
    'imdb_code, title, duration, director, year, rating, imdb_score, keywords, genres'
)


def find_movies(search_text):
    if not search_text or not search_text.strip():
        raise ValueError("Search text is required")

    url = URL + search_text
    resp = requests.get(url)
    movie_data = resp.json()
    movies_list = movie_data.get('hits')

    movies = [
        MovieResult(**md)
        for md in movies_list
    ]
    
    # for md in movies_list:
    #     m = MovieResult(**md)
    #
    #     movies.append(m)

    movies.sort(key=lambda m: -m.year)

    return movies


if __name__ == '__main__':
    find_movies('hills')