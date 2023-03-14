from database import Database
from helper.writeAJson import writeAJson

db = Database(database="pokedex", collection="pokemons")

class Pokedex:
    def __init__(self, db_name, collection_name):
        self.db = Database(db_name, collection_name)

    def acha_pokemon(name):
        pokemon1 = db.collection.find({"name": name})
        writeAJson(pokemon1,"pokemon_achado")
        
        
    def pokemon_com_3_fraquezas():
        pokemon2 = db.collection.find({"weaknesses": {"$size": 3}})
        writeAJson(pokemon2,"pokemons_3_fraquezas")
        

    def pokemon_fracos_agua_voador():
        pokemon3 = db.collection.find({"$or": [{"type":"Water"},{"weaknesses": "Flying"}]})
        writeAJson(pokemon3,"pokemons_fracos_agua_voador")
        

    def pokemon_com_evolucao():
        pokemon4 = db.collection.find({"next_evolution": {"$exists": True} })
        writeAJson(pokemon4,"pokemons_que_tem_evolucao")
        

    def pokemon_com_duas_evolucoes():
        pokemon5 = db.collection.find({"next_evolution": {"$size": 2}})
        writeAJson(pokemon5,"pokemons_que_tem_2_evolucoes")
        