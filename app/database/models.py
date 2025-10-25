class UsuarioModel():
    def __init__(self, conexao, cursor):
        self.conexao = conexao 
        self.cursor = cursor 
    # Funções de consulta, inserção e remoção 
    def inserir_na_tabela_usuarios(self, nome, cpf, idade, email, senha, telefone):
        sql_insert = 'insert into usuarios (nome, cpf, idade, email, senha, telefone) values (%s, %s, %s, %s, %s, %s);'
        dados = (nome, cpf, idade, email, senha, telefone)
        self.cursor.execute(sql_insert, dados)
        self.conexao.commit()



    def alterar_na_tabela_usuarios(self, id, dados_para_alterar):
        partes_do_set = []
        if dados_para_alterar:
            for coluna in dados_para_alterar:
                partes_do_set.append(f'{coluna} = %s')
        else:
            print("não há nada para alterar")
            
        string_set = ', '.join(partes_do_set) #formata para sql
        print(f'dados para alterar: {dados_para_alterar}')
        valores = list(dados_para_alterar.values())
        valores.append(id)    
        print(valores)
        sql_update =  f"update usuarios set {string_set} where id=%s"
        self.cursor.execute(sql_update, valores)
        self.conexao.commit()


    def consultar_na_tabela_usuarios(self, id):
        sql_consuta = 'select * from usuarios where id=%s'
        dados  = (id,)
        self.cursor.execute(sql_consuta, dados)
        resultado = self.cursor.fetchone()
        # print(resultado)
        return resultado
    

    def deletar_na_tabela_usuarios(self, id):
        sql_delete = 'delete from usuarios where id=%s'
        dados = (id,)
        self.cursor.execute(sql_delete, dados)
        self.conexao.commit()



    def consultar_usuario_por_email(self, email):
        """Função auxiliar para verificar o usuário e um determinado email
            return: usuário, email e senha 
        """


        sql = "select id, nome, email, senha from usuarios where email=%s" 
        dados = (email, )
        self.cursor.execute(sql, dados)
        resultado = self.cursor.fetchone()
        
        return resultado

        




class ContaModel():
    def __init__(self, conexao, cursor):
        self.conexao = conexao
        self.cursor = cursor


    def criar_conta(self, usuario, nome, saldo):
        sql_insert = 'insert into contas(id_usuario, nome, saldo_atual) values (%s, %s, %s)'
        dados = (usuario, nome, saldo)
        self.cursor.execute(sql_insert, dados)
        self.conexao.commit()
    
    def consultar_contas_usuario(self, id_usuario):
        sql_consuta = 'select * from contas where id_usuario=%s'
        dados = (id_usuario, )  
        self.cursor.execute(sql_consuta, dados)
        resultado = self.cursor.fetchall()
        
        return resultado  


    def alterar_saldo_conta(self, valor_para_somar, conta_id):
        sql_alterar = 'update contas set saldo_atual = saldo_atual + %s where id_conta=%s' 
        dados = (valor_para_somar, conta_id)
        self.cursor.execute(sql_alterar, dados)
        self.conexao.commit()



                                                                          


class CategoriaModel():    

    def __init__(self, conexao, cursor):
        self.conexao = conexao
        self.cursor = cursor

    def criar_categoria(self, nome_categoria, tipo_categoria, id_usuario):
        sql_insert = 'insert into categorias(nome_categoria, tipo_categoria, id_usuario) values (%s, %s, %s)'
        dados = (nome_categoria, tipo_categoria, id_usuario)
        self.cursor.execute(sql_insert, dados)
        self.conexao.commit()
    
    def deletar_categoria(self, id):
        sql_delete = 'delete from categorias where id_categoria=%s'
        dados = (id,)
        self.cursor.execute(sql_delete, dados)
        self.conexao.commit()

    def listar_categoria_por_tipo(self, tipo_categoria, id_usuario):
        sql_list = 'select * from categorias where tipo_categoria=%s and id_usuario=%s'
        dados = (tipo_categoria, id_usuario)
        self.cursor.execute(sql_list, dados)
        resultado = self.cursor.fetchall()
        
        return resultado  

class TransacaoModel():
    def __init__(self, conexao, cursor):
        self.conexao = conexao 
        self.cursor = cursor 

    def inserir_transacao(self, descricao_transacao, tipo_transacao, valor_transacao, dta_transacao, id_usuario, id_conta, id_categoria):
        sql_insert = 'insert into transacoes(descricao_transacao, tipo_transacao, valor_transacao, dta_transacao, id_usuario, id_conta, id_categoria) values (%s, %s, %s,%s, %s, %s,%s)'
        dados = (descricao_transacao, tipo_transacao, valor_transacao, dta_transacao, id_usuario, id_conta, id_categoria)
        self.cursor.execute(sql_insert, dados)
        self.conexao.commit()

    def deletar_transacao(self, id):
        sql_delete = 'delete from transacoes where id_transacao=%s'
        dados = (id,)
        self.cursor.execute(sql_delete, dados)
        self.conexao.commit()

    def consultar_transacoes_por_usuario(self, id_usuario, ):
        sql_list = 'select * from transacoes where id_usuario=%s'
        dados = (id_usuario, )
        self.cursor.execute(sql_list, dados)
        resultado = self.cursor.fetchall()
        
        return resultado  

    def consultar_transacoes_por_periodo(self, primeira_data, segunda_data, id_usuario):
        sql_consult = 'select * from transacoes where dta_transacao between %s and %s and id_usuario=%s'
        dados = (primeira_data, segunda_data, id_usuario)
        self.cursor.execute(sql_consult, dados)
        resultado = self.cursor.fetchall()

        return resultado





    
    