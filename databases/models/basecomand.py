


AND = 'AND '
OR = 'OR '

#======================================================== +
class BaseExp:
    
    name = None
    
    def add(self, *args, **kwargs):
        raise NotImplementedError()
    
    def definition(self):
        return self.name + self.line() + ' '
    
    def line(self):
        raise NotImplementedError()
    
    def __bool__(self):
        raise NotImplementedError()

#======================================================== +
class OrAnd:
    def __init__(self, exp_type=AND, **kwargs):
        self.separator = exp_type
        self._params = kwargs

    def __str__(self):
        kv_paris = [f'{k} = {v}' for k,v in self._params.items()]
        return f' {self.separator}'.join(kv_paris) + ' '
    
    def __bool__(self):
        return bool(self._params)


#======================================================== +
class Select(BaseExp):
    
    name = "SELECT "
    
    def __init__(self,*args, **kwargs):
        self._params = []
        self.add(*args, **kwargs)
        self.query = self.definition()
        
    def add(self, *args, **kwargs):
        self._params.extend(args)
        return self

    def line(self):
        return ','.join([str(key) for key in self._params])

    def __bool__(self):
        return bool(self._params)
    
#======================================================== +
class Limit(Select):
    name = "LIMIT "  
#======================================================== +
class From(Select):
    name = "FROM "
    
#======================================================== + 
class Where(BaseExp):
    
    name = "WHERE "
    
    def __init__(self, exp_type=AND, **kwargs):
        self.add(exp_type, **kwargs)
        self.query = self.definition()
        
    def add(self, exp_type=AND, **kwargs):
        self._orAnd = OrAnd(exp_type, **kwargs)
        return self._orAnd

    def line(self):
        return str(self._orAnd)

    def __bool__(self):
        return bool(self._orAnd)
#========================================================
class Join(BaseExp):

    name = "JOIN "
    
    def __init__(self,table_name, exp_type=AND, **kwargs):
        self.name += f'{table_name} ON {table_name}.'
        self.add(exp_type, **kwargs)
        self.query = self.definition()
        
    def add(self, str_type=AND, **kwargs):
        self._orAnd = OrAnd(str_type, **kwargs)
        return self._orAnd

    def line(self):
        return  str(self._orAnd)

    def __bool__(self):
        return bool(self._orAnd)
#======================================================== + 


class BaseMetodSQL:
    ### Использует databases.connection
    query = ''
    
    def select(self, *columns):
        self.query += Select(*columns).query
        return self
    
    def FROM(self, *table):
        self.query += From(*table).query
        #==========================================
        return self

    
    def WHERE(self, exp_type=AND, **kwargs):
        self.query += Where(exp_type=AND, **kwargs).query
        #==========================================
        return self


    def JOIN(self,table_name, exp_type=AND, **kwargs):
        self.query += Join(table_name, exp_type=AND, **kwargs).query
        #==========================================
        return self
        
    def LIMIT(self, *args):
        self.query += Limit(*args).query
        #==========================================
        return self

        
        
    # def _update(self,tableName,which=None, *column_date,):  
    #     column_list = ','.join(column_date)
    #     self.query = f'UPDATE {tableName} SET {column_list}'
    #     if which:
    #        self.query += f' WHERE {which}'  
    #     return self

    # def _delete(self, tableName, *condition):
    #     condition_list = ','.join(condition)
    #     self.query = f'UPDATE {tableName} WHERE {condition_list}'
    #     return self
    
    # def len(self,table_name):
    #     return len(self._select(table_name,'id')._get())

    
    # def _sort(self, table):
    #     self.query += f" ORDER BY {table}"
    #     return self
          
    # 
    
    
    
#=================================================================================

# # colum = ['Post.id', 'Post.title','Post.text', 'User_Photo.photo']
# myModel = ModelComandsSQL()
# myModel.select('Post.id', 'Post.title','Post.text', 'User_Photo.photo')
# myModel.FROM('Photo_Post')
# myModel.JOIN('Post',id='Photo_Post.post_id')
# myModel.JOIN('User_Photo',id='Photo_Post.photo_id')
# print(myModel.query)

