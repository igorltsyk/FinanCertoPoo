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
