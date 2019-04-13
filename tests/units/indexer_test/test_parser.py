from indexer.parser import is_video

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
