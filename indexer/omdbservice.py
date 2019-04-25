"""Handle the querying to omdb."""

import requests
import configparser


def get_api_key():
    config = configparser.ConfigParser()
    config.read('config/config.ini')
    return config['OMDB']['api_key']


def query_db(keywords):
    api_key = get_api_key()
    keywords_request = '+'.join(keywords)
    request_url = \
        f'http://www.omdbapi.com/?apikey={api_key}&s={keywords_request}'
    r = requests.get(request_url)
    return r.json()
    

