from database import Database
from teacher_crud import TeacherCRUD 
from teacherCLI import TeacherCLI
from query import Query

# cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
db = Database("bolt://18.215.189.151:7687", "neo4j", "cuffs-faults-waves")

query_database = Query(db)

#Questão 1
print(query_database.renzo())
print()
print(query_database.começa_com_M())
print()
print(query_database.cidades())
print()
print(query_database.escolas())
print()

#Questão 2
print(query_database.mais_jovem())
print()
print(query_database.populacao())
print()
print(query_database.cep())
print()
print(query_database.caractere())
print("Fim das questões 1 e 2")
print()


#Questão 3
#Cria um instância prof, do TeacherCRUD
prof = TeacherCRUD(db)

# Criando o professor
prof.create('Chris Lima', '1956', '189.052.396-66')

#Pesquisando o professor Chris
print(prof.read('Chris Lima'))

#Alterando o cpf do professor
prof.update('Chris Lima', '162.052.777-77')

# Cria uma instância cli, da classe CLI
cli = TeacherCLI(prof)

#Inicia o CLI
cli.run()

# Fecha conexão com o BD
db.close()


