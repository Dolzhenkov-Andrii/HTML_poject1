from cmath import nan
import pymysql
from pymysql.cursors import DictCursor
class ORM_my:
    def __init__(self, host, user, password, db):
        try:
            self.connection = pymysql.connect(
                host=host,
                user=user,
                password=password,
                db=db,
                charset='utf8mb4',
                cursorclass=DictCursor
                )
            print("Connect successful!!!... (^_^)")
        except:
            print("Erorr connecting... (X_X)")
        
    def select(self, sel_str):
        try :
            if 'select' or 'SELECT' in sel_str:
                with self.connection.cursor() as cursor:
                    cursor.execute(sel_str)
                    query = []
                    for row in cursor:
                        # print('#4___| row : ',row)
                        query.append(row)
                return query
            else:
                return None
        except:
            ...
                
        
        
    # def __del__(self):
    #     self.connection.close()
        
# myDB = ORM_my(host='',user='oscura',password='Ujhs!!Gj04Rjktyj!((#',db='my_blog')        
        
# user_post = myDB.select("select id, title, text from Post")
# for id in user_post:
#     print('ID: ', id)
#     id.update(myDB.select(f"SELECT photo FROM User_Photo INNER JOIN Photo_Post ON User_Photo.id=Photo_Post.photo_id WHERE photo_id={id['id']}")[0])
# for id in user_post:
#     print('-'*10)
#     print('ID: ', id['id'])
#     print('Photo: ', id['photo'])
#     print('Title: ', id['title'])
#     print('='*10)

# img_us = myDB.select("SELECT photo FROM User_Photo INNER JOIN Photo_Post ON User_Photo.id=Photo_Post.photo_id AND Photo_Post.photo_id={id}")  
