from database.models import ModelSQL
from database.conection import criar_conexao

conexao = criar_conexao()
if conexao and conexao.is_connected():

    cursor = conexao.cursor(dictionary=True)
    # cursor = conexao.cursor()
    modelo = ModelSQL(conexao=conexao, cursor=cursor)
    
    # resultado = modelo.deletar_na_tabela_usuarios(3)
    # if resultado:
    #     print("usuário deletado com sucesso ")   
     
    # adicionar = modelo.inserir_na_tabela_usuarios('Igor', '55698569963', 21, 'igorteste12@gmail.com', 'senhateste1234', '11956897945')

    consultar = modelo.consultar_na_tabela_usuarios(2)
    # print(consultar)

    dados_originais = consultar

    dados_novos = {'nome': 'Igor Souza', 'email': 'igorsouzateste@gmail.com'}


    alteracoes = {}

    print(consultar)

    for chave, valor_novo in dados_novos.items():
        if valor_novo != dados_originais[chave]:
            alteracoes[chave] = valor_novo

    print(alteracoes)

    id = 5

    modelo.alterar_na_tabela_usuarios(id, alteracoes)



    # dados_editar = {'telefone': '11989665989'}
    # teste = dados_editar.get('telefone')


    # print(consultar)
    # if consultar:
    #     for chave, valor in consultar.items():
            
   
    # alterar = modelo.alterar_na_tabela_usuarios()



conexao.close()
cursor.close()
