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