from sqlobject import *
from lib.mysql import conn

class TributacaoEntity(SQLObject):
    _connection = conn
    id_prospect = IntCol();
    tipo_tributo = StringCol();

    class sqlmeta:
        table = "TRIBUTACAO"
        idName = 'id_prospect'
        # idType = 'int'