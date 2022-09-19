"""
    JSON manager
"""
from exceptionsAPI.exceptionsAPI import InvalidKey

def request_data(json_data, value):
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
    try:
        if json_data:
            if json_data[value]:
                return json_data[value]
            raise InvalidKey
        raise InvalidKey
    except InvalidKey as error:
        return error
