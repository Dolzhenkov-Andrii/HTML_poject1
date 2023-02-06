"""
    Validator strings
"""
import re
from exceptions.validate import (
    InvalidStringMinSize,
    InvalidStringMaxSize,
    InvalidCharactersInString,
    InvalidType,
    APIexception,
)


def valid_string_size(string, min_size, max_size):
    """
        Checks the maximum and minimum length of a string.
        Returns an error if it doesn't match.
        Returns a string if it matches.
    """
    if isinstance(string, str) is False:
        raise InvalidType
    if (isinstance(min_size, int) and isinstance(max_size, int)) is False:
        raise InvalidType

    if len(string) < min_size:
        raise InvalidStringMinSize
    if len(string) > max_size:
        raise InvalidStringMaxSize

    return string


def invalid_string_characters(string, characters):
    """
        Checks for invalid string characters.
        Returns an error if there are invalid characters.
        Returns a string if there are no such characters.
    """
    if (isinstance(string, str) and isinstance(characters, str)) is False:
        raise InvalidType

    pattern = re.compile(characters)

    if pattern.search(string) is not None:
        raise InvalidCharactersInString

    return string


def valid_string_characters(string, characters):
    """
        Checks for invalid string characters.
        Returns an error if there are invalid characters.
        Returns a string if there are no such characters.
    """
    if (isinstance(string, str) and isinstance(characters, str)) is False:
        raise InvalidType

    pattern = re.compile(characters)

    if pattern.search(string) is None:
        raise InvalidCharactersInString

    return string


def valid_string_size_and_characters(string, min_size, max_size, characters):
    """Checks a string for correct length and valid characters

    Args:
        string (str): String to check
        min (int): minimum length
        max (int): maximum length
        char (str): characters that are allowed in a string
    """

    try:
        valid_string_size(
            string=string,
            min_size=min_size,
            max_size=max_size,
        )
        valid_string_characters(
            string=string,
            characters=characters
        )
    except APIexception as error:
        raise error

    return string
