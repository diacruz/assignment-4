# test_barky.py

import pytest
import barky
from unittest.mock import patch, MagicMock

def test_option_choose():
    mock_command = MagicMock()
    mock_prep_call = MagicMock(return_value="prep_data")
    option = barky.Option("Option", mock_command, prep_call=mock_prep_call)

    option.choose()

    mock_prep_call.assert_called_once()
    mock_command.execute.assert_called_once_with("prep_data")

def test_clear_screen():
  
    with patch("barky.os") as mock_os:
        barky.clear_screen()
        mock_os.system.assert_called_once()

def test_get_user_input(monkeypatch):

    monkeypatch.setattr('builtins.input', lambda _: 'test_input')
    user_input = barky.get_user_input("Test Label")
    assert user_input == "test_input"

def test_get_option_choice(monkeypatch):

    options = {"A": barky.Option("Option A", MagicMock())}
    monkeypatch.setattr('builtins.input', lambda _: 'A')
    chosen_option = barky.get_option_choice(options)
    assert chosen_option == options["A"]

def test_option_choice_is_valid():
    
    options = {"A": barky.Option("Option A", MagicMock())}
    assert barky.option_choice_is_valid("A", options)
    assert barky.option_choice_is_valid("a", options)
    assert not barky.option_choice_is_valid("B", options)

def test_get_new_bookmark_data(monkeypatch):
   
    monkeypatch.setattr('builtins.input', lambda _: 'Test Title')
    assert barky.get_new_bookmark_data()["title"] == "Test Title"



def test_loop(monkeypatch):
    mock_clear_screen = MagicMock()
    mock_option_choose = MagicMock()

    with patch("barky.clear_screen", mock_clear_screen), \
         patch("barky.get_option_choice", mock_option_choose):
        
        monkeypatch.setattr('builtins.input', lambda _: 'Q')
        barky.loop()

    
    mock_clear_screen.assert_called()
  
    mock_option_choose.assert_called()


if __name__ == "__main__":
    pytest.main()
