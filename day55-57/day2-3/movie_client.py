import uplink
from uplink_helpers import raise_for_status
import requests

@raise_for_status
class MovieSearchClient(uplink.Consumer):

    def __init__(self):
        super().__init__(base_url='http://movie_service.talkpython.fm/')

    @uplink.get('api/search/{keyword}')
    def search_movies(self, keyword) -> requests.models.Response:
        '''Get's all movie entries'''

    @uplink.get('api/director/{director_name}')
    def search_directors(self, director_name) -> requests.models.Response:
        '''Get's all movie entries by director'''

    @uplink.get('api/movie/{imdb_number}')
    def movie_by_imdb(self, imdb_number) -> requests.models.Response:
        '''Gets'all movie entries by imdb_number'''



