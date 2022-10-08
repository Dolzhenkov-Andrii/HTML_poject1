"""
    JSON manager
"""
from exceptions.validate import InvalidKey

def valid_key(json_data, value):
    """Key verification

    Args:
        json_data (JSON): request data in json format
        value (str): requested key

    Raises:
        InvalidKey: Error getting by key
        InvalidKey: Error getting by key

    Returns:
        str: dictionary data by key
    """
    if json_data:
        if json_data[value]:
            return json_data[value]
        return False
    raise InvalidKey
