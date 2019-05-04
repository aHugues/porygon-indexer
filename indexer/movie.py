"""Represent the Movie class inherited from the media class."""

from . import Media
from indexer.parser import separate_keywords

class Movie(Media):


    def __init__(self, filename):
        """Create a movie object from its raw filename."""
        self.filename = filename
        self.keywords = separate_keywords(filename)    

    def to_dict(self):
        """Export the movie to a dict."""
        result = {
            'title': self.title,
            'keywords': self.keywords
        }
        return result
