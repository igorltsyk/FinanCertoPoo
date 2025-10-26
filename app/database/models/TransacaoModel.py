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
    