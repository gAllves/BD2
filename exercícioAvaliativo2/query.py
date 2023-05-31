class Query:
    def __init__ (self,db):
        self.db = db

    #1-a)
    def renzo(self):
        print("1-a)")
        query = "MATCH (t:Teacher) WHERE t.name = 'Renzo' RETURN t.ano_nasc AS ano_nasc, t.cpf AS cpf"
        results = self.db.execute_query(query)
        return [(result["ano_nasc"], result["cpf"]) for result in results]
    
    #1-b)
    def começa_com_M(self):
        print("1-b)")
        query = "MATCH (t:Teacher) WHERE t.name STARTS WITH 'M' RETURN t.name AS name, t.cpf AS cpf"
        results = self.db.execute_query(query)
        return [(result["name"],result["cpf"]) for result in results]
    
    #1-c)
    def cidades(self):
        print("1-c)")
        query = "MATCH (c:City) RETURN c.name as name"
        results = self.db.execute_query(query)
        return [result["name"] for result in results]
    
    #1-d)
    def escolas(self):
        print("1-d)")
        query = "MATCH (s:School) WHERE s.number >= 150 AND s.number <= 550 RETURN s.name AS name, s.adress AS endereco, s.number AS numero"
        results = self.db.execute_query(query)
        return [(result["name"], result["endereco"], result["numero"]) for result in results]
            
    #2-a)
    def mais_jovem(self):
        print("2-a)")
        query = "MATCH (t:Teacher) RETURN MAX(t.ano_nasc) AS mais_jovem, MIN(t.ano_nasc) AS mais_velho"
        results = self.db.execute_query(query)
        return [(result["mais_jovem"], result["mais_velho"]) for result in results]
    
    #2-b)
    def populacao(self):
        print("2-b)")
        query = "MATCH (c:City) RETURN AVG(c.population) AS media"
        results = self.db.execute_query(query)
        return [result["media"] for result in results]
    
    #2-c)
    def cep(self):
        print("2-c)")
        query = "MATCH (c:City) WHERE c.cep = '37540-000' RETURN REPLACE(c.name, 'a', 'A') AS cidade"
        results = self.db.execute_query(query)
        return [result["cidade"] for result in results]
    
    #2-d)
    def caractere(self):
        print("2-d)")
        query = "MATCH (t:Teacher) RETURN SUBSTRING (t.name, 2, 1) AS professor"
        results = self.db.execute_query(query)
        return [result["professor"] for result in results]
    
