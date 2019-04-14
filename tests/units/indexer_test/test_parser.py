import os

from indexer.parser import is_video
from indexer.parser import separate_keywords
from indexer.parser import get_videos_in_directory

def test_correct_video():
    """Test the detection of true video files."""
    assert is_video('true_video.mp4') == True
    assert is_video('true_video.mkv') == True
    assert is_video('true_video.avi') == True


def test_non_video():
    """Test the filtering of non-video files."""
    assert is_video('not_video.mp3') == False
    assert is_video('not_video.txt') == False


def test_weird_filenames():
    """Test the filtering of non-standard filenames."""
    assert is_video('true.video.with.dots.MKV') == True
    assert is_video('NoT.ViDEo.mkv.mp3') == False


def test_separate_keywords():
    """Test the separation of keywords."""
    list1 = separate_keywords('My Super Movie [2019] [FR].mkv')
    list2 = separate_keywords('the.movie.of.the.year.2018.hevc.aac.mp4')
    list3 = separate_keywords('Python the movie 2: Return \
        with a mega revenge (2019).mkv')

    assert list1 == ['super', 'movie', 'my']
    assert list2 == ['movie', 'year', 'of']
    assert list3 == ['revenge', 'python', 'return', 'movie', 'with', 'mega']


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
