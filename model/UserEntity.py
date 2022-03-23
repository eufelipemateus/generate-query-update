from sqlobject import *
from lib.mysql import conn

class UserEntity(SQLObject):
    _connection = conn
    id_prospect = IntCol()
    cpf = StringCol()

    class sqlmeta:
        table = "PEDENCPP"
        idName = 'id_prospect'
        # idType = 'int'