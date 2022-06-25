

class BaseModel:
    ### Использует databases.connection
    
    def __init__(self, connection):
        self.query = None
        self.connection = connection
        

    def _create():
        pass

    def _select(self,table_name, *columns ):
        columns_list = ','.join(columns)
        self.query = f"SELECT {columns_list} FROM {table_name}"
        return self

    def _update(self,tableName,which=None, *column_date,):
        column_list = ','.join(column_date)
        self.query = f'UPDATE {tableName} SET {column_list}'
        if which:
           self.query += f' WHERE {which}'  
        return self

    def _delete(self, tableName, *condition):
        condition_list = ','.join(condition)
        self.query = f'UPDATE {tableName} WHERE {condition_list}'
        return self

    def _join(self,typeJOIN, table_name, value1,value2):
        self.query += f" {typeJOIN} {table_name} ON {value1}={value2}"
        return self
    
    
    def _limit(self, limit):
        if limit != None:
            self.query += f" LIMIT {limit}"
        return self
    
    def _sort(self, table):
        self.query += f" ORDER BY {table}"
        return self
          
    def _get(self):
        with self.connection._connection.cursor() as cursor:
            cursor.execute(self.query)
            query = []
            for row in cursor:
                query.append(row)
        return query
