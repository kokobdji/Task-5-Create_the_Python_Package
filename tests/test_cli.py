import argparse
from unittest.mock import mock_open, patch

import pytest
from unique_characters_kokobdji.cli import (NotFound, UnknownFunc, main,
                                            opening_file, parse)


@patch('argparse.ArgumentParser.parse_args',
       return_value=argparse.Namespace(string=None, file=None))
def test_args_check_raise_error(mock_parse_args):
    with pytest.raises(UnknownFunc) as ExceptionInfo:
        parse()
        assert 'Must be a file or a string' == str(ExceptionInfo.value)
        mock_parse_args.assert_called_once()


@patch('argparse.ArgumentParser.parse_args',
       return_value=argparse.Namespace(string='1', file=None))
def test_parse_string(mock_parse_args):
    assert parse() == argparse.Namespace(string='1', file=None)
    mock_parse_args.assert_called_once()


@patch('os.path.isfile', return_value=False)
def test_isfile(mock_isfile):
    with pytest.raises(NotFound) as ExceptionInfo:
        opening_file(mock_isfile)
        assert 'File is not exist in directory' == str(ExceptionInfo.value)
        mock_isfile.assert_called_once()


@patch('builtins.open', new_callable=mock_open, read_data='data')
@patch('os.path.isfile', return_value=True)
def test_file_reading(mock_isfile, mock_file):
    assert opening_file("path/to/open") == ["data"]
    mock_file.assert_called_once()
    mock_isfile.assert_called_once()


@patch('unique_characters_kokobdji.cli.opening_file')
@patch('unique_characters_kokobdji.cli.list_input')
def test_args_file(mock_file, mock_open_file):
    assert main(argparse.Namespace(file='path/to/open', string=None))
    mock_file.assert_called_once()
    mock_open_file.assert_called_once()


@patch('unique_characters_kokobdji.cli.counter_unique_characters')
def test_args_string(mock_counter_func):
    assert main(argparse.Namespace(file=None, string='unique_characters_kokobdji'))
    mock_counter_func.assert_called_once()
