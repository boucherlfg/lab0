# pylint: skip-file

import pytest
from src import app
from unittest.mock import patch

@pytest.fixture
def mock_print():
    with patch("builtins.print") as mock:
        yield mock

def test_func(mock_print):
    app.func("hello")
    mock_print.assert_called_with("hello")

def test_func_error():
    with pytest.raises(Exception):
        app.func("test" + 1)