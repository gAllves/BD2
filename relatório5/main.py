from database import Database
from writeAJson import writeAJson
from livroModel import LivroModel
from cli import LivroCLI

db = Database(database="relatorio_05", collection="livros")
livroModel = LivroModel(database=db)

livroCLI = LivroCLI(livroModel)
livroCLI.run()