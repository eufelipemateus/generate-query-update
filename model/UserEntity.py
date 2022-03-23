from sqlobject import *
from utils.mysql import conn

class UserEntity(SQLObject):
    _connection = conn
    id_prospect = IntCol()
    cpf = StringCol()

    class sqlmeta:
        table = "PEDENCPP"
        idName = 'id_prospect'
        # idType = 'int'