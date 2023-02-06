'''
    Connection
'''
import pymysql

from pymysql.cursors import DictCursor


class Connection: # pylint: disable=too-few-public-methods
    '''
        DB Connection class
    '''
    def __init__(self, db_host, db_user, db_password, db_name):
        self._connection = pymysql.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            db=db_name,
            charset='utf8mb4',
            cursorclass=DictCursor,
            autocommit=True
        )
