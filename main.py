import json 
import datetime
from app.database.conection import criar_conexao as cn
from app.utils.Utilities import *
from app.utils.Controller import Controller 
from app.database.models.ContaModel import ContaModel 
# cria a conexão 

conexao = cn()

cursor = conexao.cursor(dictionary=True)
class Main:
   
    def main(self):
        self.usuario_logado_atualmente = None
        controller = Controller()
        conta = ContaModel(conexao=conexao, cursor=cursor)
        

        email = None
        senha = None


        resultado = controller.FazerLogin(email, senha)

        if resultado: 
            self.usuario_logado_atualmente = resultado.get('id')
            print(f"Usuário identificado com sucesso, ID: {self.usuario_logado_atualmente}")
            

            dados_contas = conta.consultar_contas_usuario(self.usuario_logado_atualmente)

            if dados_contas:
                print(dados_contas)

            else: 
                print("Você não tem uma conta, vamos cadastrar uma!")
                primeira_conta = input("Digite o nome da sua primeira conta: ")
                primeiro_saldo = input("Digite seu saldo atual para esta conta: ")
                self.usuario_logado_atualmente 

                conta.criar_conta(self.usuario_logado_atualmente, primeira_conta, primeiro_saldo)

            
        else:
            print('Usuário não logado')


objeto = Main()

objeto.main()