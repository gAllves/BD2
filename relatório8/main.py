from database import Database
from jogo_database import JogoDatabase

# cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
db = Database("bolt://34.201.4.253:7687", "neo4j", "skies-flanges-splices")
db.drop_all()

jogo_db = JogoDatabase(db)

# Criando alguns jogadores
jogo_db.create_player("Paula")
jogo_db.create_player("Arthur")
jogo_db.create_player("Gabriel")

# Criando algumas partidas e vinculando os jogadores
jogo_db.create_match("Paula, Neymar", "Paula")
jogo_db.create_match("Paula, Gabriel", "Gabriel")
jogo_db.create_match("Gabriel, Neymar", "Gabriel")

# Atualizando o nome de um jogador
jogo_db.update_player("Arthur", "Neymar")

jogo_db.insert_player_match("Paula", "Paula, Neymar")
jogo_db.insert_player_match("Paula", "Paula, Gabriel")
jogo_db.insert_player_match("Gabriel", "Gabriel, Neymar")
jogo_db.insert_player_match("Gabriel", "Paula, Gabriel")
jogo_db.insert_player_match("Neymar", "Paula, Neymar")
jogo_db.insert_player_match("Neymar", "Gabriel, Neymar")

# Deletando
#jogo_db.delete_player("Gabriel")
#jogo_db.delete_match("Gabriel", "Gabriel, Neymar")

# Imprimindo todas as informações do banco de dados
print("Nome dos jogadores:")
print(jogo_db.get_players())
print("Matches:")
print(jogo_db.get_matches())

# Fechando a conexão com o banco de dados
db.close()