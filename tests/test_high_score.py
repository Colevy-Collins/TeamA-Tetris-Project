import pytest
from src.HighScoreHandler import HighScoreHandler


@pytest.fixture
def high_score_handler(tmp_path):
    test_directory = tmp_path / "some_directory"
    test_directory.mkdir()
    test_filename = "high_score.txt"
    handler = HighScoreHandler(str(test_directory), test_filename)
    return handler

def test_read_high_score_no_file(high_score_handler):
    assert high_score_handler.read_data() == 0

def test_write_high_score_updates_value(high_score_handler):
    test_score = 100
    high_score_handler.write_data(test_score)
    assert high_score_handler.read_data() == test_score

def test_read_non_numeric_high_score_returns_zero(high_score_handler):
    test_directory, test_filename = high_score_handler.directory, high_score_handler.filename
    with open(f"{test_directory}/{test_filename}", "w") as f:
        f.write("not_a_number")
    assert high_score_handler.read_data() == 0