
class SqlFile :

    def __init__(self):
        self._f = open("update.sql", "a")

    def add_query(self,query):
        self._f.write(query)    
        self._f.write("\n")

    def close(self):
        self._f.close()