"""Test methods for the Media class."""

from indexer import Media


def create_tested_media():
    """Create a movie object that will be used for later tests."""
    return Media("the.movie.of.the.year.2018.1080p.x265.hevc.aac.mp4")


def test_default_media_creation():
    """Test the correct generation of a media fields."""
    tested_media = create_tested_media()

    assert tested_media.title == 'the movie of the year 2018'
    assert tested_media.keywords == ['movie', 'year', '2018']