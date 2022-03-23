from sqlobject import *
from utils.mysql import conn

class TributacaoEntity(SQLObject):
    _connection = conn
    id_prospect = IntCol();
    tipo_tributo = StringCol();

    class sqlmeta:
        table = "TRIBUTACAO"
        idName = 'id_prospect'
        # idType = 'int'