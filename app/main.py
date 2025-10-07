from database.models import ModelSQL
from database.conection import criar_conexao

conexao = criar_conexao()
if conexao and conexao.is_connected():

    
    cursor = conexao.cursor()
    modelo = ModelSQL(conexao=conexao, cursor=cursor)
    
    # resultado = modelo.deletar_na_tabela_usuarios(3)
    # if resultado:
    #     print("usuário deletado com sucesso ")    
    adicionar = modelo.inserir_na_tabela_usuarios('Igor', '55698569963', 21, 'igorteste12@gmail.com', 'senhateste1234', '11956897945')
conexao.close()
cursor.close()
