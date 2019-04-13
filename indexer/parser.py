import os 

def is_video(filename):
    """Check if the file has one of the authorized video extensions."""
    authorized_extensions = ['mkv', 'mp4', 'avi']
    extension = filename.split('.')[-1].lower()
    return extension in authorized_extensions

def separate_keywords(filename):
    """Separate the most pertinent keywords from a given filename."""
    