import os
import re


def is_video(filename):
    """Check if the file has one of the authorized video extensions."""
    authorized_extensions = ['mkv', 'mp4', 'avi']
    extension = filename.split('.')[-1].lower()
    return extension in authorized_extensions


def separate_keywords(filename):
    """Separate the most pertinent keywords from a given filename."""
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
    """Get the list of video files in a directory given the absolute path."""
    files = []
    for (_, _, filenames) in os.walk(full_path):
        files.extend(filenames)
    return [element for element in files if is_video(element)]


def analyze_directory(full_path):
    """Conduct a full analysis of a directory."""
    movies = get_videos_in_directory(full_path)
    return [separate_keywords(movie) for movie in movies]