"""Provide methods to parse filenames and extract keywords."""

import os
import re


def is_video(filename):
    """Check if the file has one of the authorized video extensions.

    # Arguments
    filename (str): Full filename to check.

    # Returns
    is_video (Boolean): True if the file has a correct video extension.
    """
    authorized_extensions = ['mkv', 'mp4', 'avi']
    extension = filename.split('.')[-1].lower()
    return extension in authorized_extensions


def separate_keywords(filename):
    """Separate the most pertinent keywords for a given filename.

    Remove useless information to only keep words relevant to the movie title
    and keep the 6 longest words to be used when querying an API.

    # Arguments
    filename (str): Filename to analyze.

    # Returns
    separated_words (List of str): List of 6 longest keywords from the file.
    """
    additionnal_info_re = r'([^\x00-\x7F])|(\([^\(]+\))|(\[[^\[]+\])| \
        (\w+\d+\w+)|(\d+\w+)|(\w+\d+)|(the)|(hevc)|(psa)|(bluray)|(aac)| \
        (chs)|(tigole)'
    separators_re = r"[\s\.-]"
    filtered_name = re.sub(additionnal_info_re, '', filename.lower())
    separated_words = [
        x for x in re.split(separators_re, filtered_name)[:-1] if x != '']
    separated_words.sort(key=len, reverse=True)
    return separated_words[:6]


def get_videos_in_directory(full_path):
    """Get the list of video files in a directory given the absolute path.

    # Arguments
    path (str): Absolute path of the directory to search.

    # Returns
    filenames (List of str): List of movies in the directory.
    """
    files = []
    for (_, _, filenames) in os.walk(full_path):
        files.extend(filenames)
    return [element for element in files if is_video(element)]


def analyze_directory(full_path):
    """Conduct a full analysis of a directory.

    # Arguments
    path (str): Absolute path of the directory to search.

    # Returns
    keywords (List of Lists of str): List of found keywords in the directory.
    """
    movies = get_videos_in_directory(full_path)
    return [separate_keywords(movie) for movie in movies]
