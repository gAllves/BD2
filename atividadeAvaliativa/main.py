from database import Database
from cli import MotoristaCLI
from motoristaDAO import MotoristaDAO

db = Database(database="ExAvaliativo", collection="Motoristas")
motoristaDAO = MotoristaDAO(database=db)

motoristaCLI = MotoristaCLI(motoristaDAO)
motoristaCLI.run()

