"""_
    Posts exceptions
"""

from exceptions.basic import APIexception


class BasePostError(APIexception):
    """Post Error
    """

class PostArgsError(BasePostError):
    """Request arguments error
    """
    message =  'Request arguments error'

