from app.database.models import UsuarioModel
from app.database.conection import criar_conexao

conexao = criar_conexao()
if conexao and conexao.is_connected():

    cursor = conexao.cursor(dictionary=True)
    user = UsuarioModel(conexao=conexao, cursor=cursor)

class Controller: 
    

    def FazerLogin(self, email_fornecido, senha_fornecida):
        
        dados_banco = user.consultar_usuario_por_email(email_fornecido)
        

        if dados_banco:
            if dados_banco.get('senha') == senha_fornecida:
                return dados_banco
            
            else:
                print("Login mal sucedido")
        else: 
            print("Você não tem cadastro")
            
        #aaaaaaaaaaaaaaaaaaaaaaaaaaaaa





