import requests
import collections
import movie_svc
import requests.exceptions


URL = 'http://movie_service.talkpython.fm/api/search/'
MovieResult = collections.namedtuple(
    'MovieResult',
    'imdb_code, title, duration, director, year, rating, imdb_score, keywords, genres'
)

def print_header():
    print('--------------------------------------------------')
    print("                   MOVIE SEARCH APP")
    print('--------------------------------------------------')
    print()


def search_event_loop():
    search = 'ONCE_THROUGH_LOOP'

    while search != 'x':
        try:
            search = input('Movie search text (x to exit): ')
            if search != 'x':
                results = movie_svc.find_movies(search)
                print(f"Found {len(results)} results.")
                for r in results:
                    print(f'{r.year} -- {r.title}')
                print()
        except ValueError as ve:
            print(ve)
        except requests.exceptions.ConnectionError as ce:
            print('Error: your network is down.')
            break
        except Exception as x:
            print(f"Unexpected error. Details: {x}")
            break

    print('exiting...')


def main():
    print_header()
    search_event_loop()


if __name__ == '__main__':
    main()