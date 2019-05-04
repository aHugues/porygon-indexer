"""Test the parsing methods for the indexer."""

import os

from indexer.parser import is_video
from indexer.parser import separate_keywords
from indexer.parser import get_videos_in_directory
from indexer.parser import analyze_directory


def test_correct_video():
    """Test the detection of true video files."""
    assert is_video('true_video.mp4') is True
    assert is_video('true_video.mkv') is True
    assert is_video('true_video.avi') is True


def test_non_video():
    """Test the filtering of non-video files."""
    assert is_video('not_video.mp3') is False
    assert is_video('not_video.txt') is False


def test_weird_filenames():
    """Test the filtering of non-standard filenames."""
    assert is_video('true.video.with.dots.MKV') is True
    assert is_video('NoT.ViDEo.mkv.mp3') is False


def test_separate_keywords():
    """Test the separation of keywords."""
    _, list1 = separate_keywords('My Super Movie [2019] [FR].mkv')
    _, list2 = separate_keywords('the.movie.of.the.year.2018.hevc.aac.mp4')
    _, list3 = separate_keywords('Python the movie 2: Return \
        with a mega revenge (2019).mkv')
    _, list4 = separate_keywords("the.movie.of.the.year.2018.1080p.x265.hevc. \
        aac.mp4")

    assert list1 == ['super', 'movie', 'my']
    assert list2 == ['movie', 'year', '2018']
    assert list3 == ['revenge', 'python', 'return', 'movie', 'with', 'mega']
    assert list4 == ['movie', 'year', '2018']


def test_read_directory():
    """Test scanning a directory for videos."""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    scanned_dir = f"{current_dir}/example_directory/movies/"
    movies = get_videos_in_directory(scanned_dir)

    movie1 = "My Super Movie [2019] [FR].mkv"
    movie2 = "Python the movie 2: Return  with a mega revenge (2019).mkv"
    movie3 = "the.movie.of.the.year.2018.1080p.x265.hevc.aac.mp4"

    assert len(movies) == 3
    assert movie1 in movies
    assert movie2 in movies
    assert movie3 in movies


def test_analyze_directory():
    """Test scanning and parsing of directory for keywords."""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    scanned_dir = f"{current_dir}/example_directory/movies/"
    movies_keywords = analyze_directory(scanned_dir)

    keywords1 = ['super', 'movie', 'my']
    keywords2 = ['movie', 'year', '2018']
    keywords3 = ['revenge', 'python', 'return', 'movie', 'with', 'mega']

    assert len(movies_keywords) == 3
    assert keywords1 in movies_keywords
    assert keywords2 in movies_keywords
    assert keywords3 in movies_keywords
