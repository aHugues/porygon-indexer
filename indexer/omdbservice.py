"""Handle the querying to omdb."""

import requests
import configparser


def get_api_key(self):
    config = configparser.ConfigParser()
    config.read('config/config.ini')
    return config['OMDB']['api_key']


class QueryService():

    def __init__(self):
        self.api_key = get_api_key()

    def query_db(movie):
        keywords = movie.keywords
        payload = '+'.join(keywords)
        request_url = \
            f'http://www.omdbapi.com/?apikey={self.api_key}&s={payload}'
        r = requests.get(request_url)
        return r.json()
    

