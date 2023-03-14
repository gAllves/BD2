from pokedex import Pokedex
from database import Database
from helper.writeAJson import writeAJson

db = Database(database="pokedex", collection="pokemons")
db.resetDatabase()


Pokedex.acha_pokemon("Venonat")

Pokedex.pokemon_com_3_fraquezas()

Pokedex.pokemon_fracos_agua_voador()

Pokedex.pokemon_com_evolucao()

Pokedex.pokemon_com_duas_evolucoes()

