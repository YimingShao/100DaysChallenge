from movie_client import MovieSearchClient
import sys
def main():
    menu()



def menu():
    val = True
    while val:
        print("WHat would you like to do next?")
        val = input('Search movie by [K]eyword?\n'
                    'Search movie by [D]irector?\n'
                    'Search movie by [I]mdb?\n'
                    'Or [E]xit\n')

        if val  in ['k', 'K']:
            search_by_keyword()
        elif val in ['d', 'D']:
            search_by_director()
        elif val in ['i', 'I']:
            search_by_imdb()
        elif val in ['e', 'E']:
            sys.exit()
        print()

def movie_details(json_file):
    print()
    print('---------------------------------------')
    print(f"Movie name: {json_file.get('title')}")
    print(f"Director: {json_file.get('director')}")
    print(f"Imdb code: {json_file.get('imdb_code')}")
    print(f"Genres: {json_file.get('genres')}")
    print(f"Duration: {json_file.get('duration')} minutes")
    print(f"Rating: {json_file.get('rating')}")
    print(f"Year: {json_file.get('year')}")
    print(f"Imdb score: {json_file.get('imdb_score')}")
    print('---------------------------------------')
    print()

def search_by_keyword():
    svc = MovieSearchClient()
    key = input('Input a keyword of movies?\t')
    response = svc.search_movies(keyword=key)
    post = response.json()
    posts = post.get('hits')
    for i, movie in enumerate(posts, 1):
        print(f"{i}. {movie.get('title')}")
    if len(posts) is not 0:
        key = int(input('Which movie you want to view?\t'))
        selected_movie = posts[key-1]
        movie_details(selected_movie)

def search_by_director():
    svc = MovieSearchClient()
    key = input('Input a director name to search movies?\t')
    response = svc.search_directors(director_name=key)
    post = response.json()
    posts = post.get('hits')
    for i, movie in enumerate(posts, 1):
        print(f"{i}. {movie.get('title')}")
    if len(posts) is not 0:
        key = int(input('Which movie you want to view?\t'))

        selected_movie = posts[key-1]
        movie_details(selected_movie)

def search_by_imdb():
    svc = MovieSearchClient()
    key = input('Input a imdb code to search a movie?\t')
    response = svc.movie_by_imdb(imdb_number=key)
    post = response.json()
    if post is not None:
        print('---------------------------------------')
        print(f"Movie name: {post['title']}")
        print(f"Director: {post['director']}")
        print(f"Imdb code: {post['imdb_code']}")
        print(f"Genres: {post['genres']}")
        print(f"Duration: {post['duration']} minutes")
        print(f"Rating: {post['rating']}")
        print(f"Year: {post['year']}")
        print(f"Imdb score: {post['imdb_score']}")
        print('---------------------------------------')

if __name__ == '__main__':
    main()