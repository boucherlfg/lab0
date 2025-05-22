# pylint: skip-file

import pytest
from unittest.mock import patch
from src import app

@pytest.fixture
def mock_print():
    with patch('builtins.print') as mock:
        yield mock

def test_func(mock_print):
    class Test:
        check : str = ""
    def assign_check(value):
        Test.check = value
    mock_print.side_effect = assign_check
    app.func("hello")
    assert Test.check == "hello"

def test_func_not_toto(mock_print):
    class Test:
        check : str = ""
    def assign_check(value):
        Test.check = value
    mock_print.side_effect = assign_check
    app.func("hello")
    mock_print.assert_called()
