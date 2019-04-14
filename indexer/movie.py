"""Represent the Movie class inherited from the media class."""

from . import Media


class Movie(Media):
    

    def to_dict(self):
        """Export the movie to a dict."""
        result = {
            'title': self.title,
            'keywords': self.keywords
        }
        return result