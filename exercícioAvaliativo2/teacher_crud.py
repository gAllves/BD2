class TeacherCRUD():
    def __init__(self, database):
        self.database = database

    def create(self, name, ano_nasc, cpf): # cria um novo Teacher
        query = f"CREATE (t:Teacher {{name: '{name}', ano_nasc: '{ano_nasc}', cpf: '{cpf}'}})"
        self.database.execute_query(query)
        print("Professor criado com sucesso")

    def read(self, name):
        query = f"MATCH (t:Teacher {{name: '{name}'}}) RETURN t.name AS name, t.ano_nasc AS ano_nasc, t.cpf AS cpf"
        results = self.database.execute_query(query)
        return [(result["name"], result["ano_nasc"], result["cpf"]) for result in results]

    def delete(self, name): # deleta Teacher com base no name
        query = f"MATCH (t:Teacher {{name: '{name}'}}) DETACH DELETE t"
        self.database.execute_query(query)

    def update(self, name, newCpf): # atualiza cpf com base no name
        query = f"MATCH (t:Teacher {{name: '{name}'}}) SET t.cpf = '{newCpf}'"
        self.database.execute_query(query)