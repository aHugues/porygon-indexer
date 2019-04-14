"""Represent the media class."""

from .parser import separate_keywords


class Media:

    def __init__(self, filename):
        title, keywords = separate_keywords(filename)
        print(title)
        self.title = title
        self.keywords = keywords