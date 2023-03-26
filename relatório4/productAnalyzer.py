from database import Database
from writeAJson import writeAJson


class ProductAnalyzer:
    def __init__(self, database, collection):
        self.db = Database(database, collection)
    
    #Vendas por dia
    def vendasdia(self):
        result = self.db.collection.aggregate([
        {"$unwind":"$produtos"},
        {"$group": {"_id": "$data_compra", "total":{"$sum": "$produtos.quantidade"}}},
        {"$sort": {"total": -1}}

    ])
        writeAJson(result, "Vendas por dia")


    #Produto mais vendido
    def produtomaisvendido(self):
        result2 = self.db.collection.aggregate([
        {"$unwind": "$produtos"},
        {"$group": {"_id": "$produtos.descricao", "total": {"$sum": "$produtos.quantidade"}}},
        {"$sort": {"total": -1}},
        {"$limit": 1}
    ])
        writeAJson(result2, "Produto mais vendido")

    #Cliente que mais gastou em uma única compra
    def clientemais(self):
        result3 = self.db.collection.aggregate([
        {"$unwind":"$produtos"},
        {"$group":{"_id":"$cliente_id","total":{"$sum":{"$multiply":["$produtos.quantidade","$produtos.preco"]}}}},
        {"$sort":{"total": -1}},
        {"$limit": 1}
    ])
        writeAJson(result3, "Cliente que mais gastou em uma única compra")

    #Produtos que tiveram mais de uma unidade vendida
    def produtos1(self):
        result4 = self.db.collection.aggregate([
        {"$unwind":"$produtos"},
        {"$match":{"produtos.quantidade": {"$gt":1}}},
        {"$group":{"_id":"$produtos.descricao"}},
    ])
        writeAJson(result4, "Produtos que tiveram mais de uma unidade vendida")


