from database.models import ModelSQL
from database.conection import criar_conexao

conexao = criar_conexao()
if conexao and conexao.is_connected():

    
    cursor = conexao.cursor(dictionary=True)
    modelo = ModelSQL(conexao=conexao, cursor=cursor)

    reusltado = modelo.consultar_na_tabela_usuarios(3)
    

conexao.close()
cursor.close()
