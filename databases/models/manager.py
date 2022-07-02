

from basecomand import BaseMetodSQL



class Manager(BaseMetodSQL):
    
    def __init__(self, model_class):
        self.model_class = model_class
        self._model_fields = model_class._original_fields.keys()
        self.query = ''
    
    def __get_date(self,conector):
      self.connection = conector
      with self.connection._connection.cursor() as cursor:
          cursor.execute(self.query)
          query = []
          for row in cursor:
              query.append(row)
      return query    
       
    def fetch(self,conector):
        query = str(self.query)
        db_results = self.__get_date(conector)
        results = []
        for row in db_results:
          model = self.model_class()
          for field, val in zip(self._model_fields, row):
            setattr(model, field, val)
          results.append(model)
        return results
  
  
  
