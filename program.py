from sqlobject import *
from lib.util import format_cpf
from model.TributacaoEntity import TributacaoEntity
from model.UserEntity import UserEntity
from lib.sql import SqlFile

Sql = SqlFile()
Query = UserEntity.select()

for Prospect in Query:
    try:
        Tax = TributacaoEntity.get(Prospect.id_prospect)

        TipoTributo =  'RE'  if Tax.tipo_tributo =='regressivo'  else 'NO'

        Cpf = format_cpf(Prospect.cpf)                
        SqlLine = (f"UPDSATE PESFISPP COD_OPCAO_TRIBUTO_CNTRADEP = '{TipoTributo}' WHERE NUM_CPF = '{Cpf}'.")

        Sql.add_query(SqlLine)        
        print(SqlLine)
    except SQLObjectNotFound:
        print(f'Tipo de Tributação de ID \'{Prospect.id_prospect}\' Não encontrado')
    
Sql.close()
