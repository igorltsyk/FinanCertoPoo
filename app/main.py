from database.models import ModelSQL
from database.conection import criar_conexao

conexao = criar_conexao()
if conexao and conexao.is_connected():

    
    cursor = conexao.cursor(dictionary=True)
    modelo = ModelSQL(conexao=conexao, cursor=cursor)

    resultado = modelo.consultar_na_tabela_usuarios(3)
    for chave, valor in resultado.items():
        campo = chave
        valor = valor 
        print (f"{campo}: {valor}")
   

conexao.close()
cursor.close()
