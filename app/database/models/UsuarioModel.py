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

 