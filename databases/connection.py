import pymysql
from pymysql.cursors import DictCursor


class Connection:
    
    def __init__(self, db_host, db_user, db_password, db_name):
        self._connection = pymysql.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            db=db_name,
            charset='utf8mb4',
            cursorclass=DictCursor
        )
        print(f"Connected to {db_name}({db_host})")
      
        
    # def select(self, sel_str):
    #     try :
    #         if 'select' or 'SELECT' in sel_str:
    #             with self.connection.cursor() as cursor:
    #                 cursor.execute(sel_str)
    #                 query = []
    #                 for row in cursor:
    #                     # print('#4___| row : ',row)
    #                     query.append(row)
    #             return query
    #         else:
    #             return None
    #     except:
    #         ...
                
        
        
    # def __del__(self):
    #     self.connection.close()
        

