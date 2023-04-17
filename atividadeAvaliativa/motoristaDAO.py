from pymongo import MongoClient
from bson.objectid import ObjectId
from passageiro import Passageiro
from motorista import Motorista
from corrida import Corrida

class MotoristaDAO:
    def __init__(self, database):
        self.db = database

    def create_motorista(self, motorista):
        try:
            moto = {
                'Nota do motorista': motorista.notaMotorista, 
                'Corridas': [
                    {
                
                    'Nota da corrida':corrida.notaCorrida, 
                    'Distância':corrida.distancia, 
                    'Valor':corrida.valor, 
                    'Passageiro': {
                        'Nome':corrida.passageiro.nome, 
                        'Documento':corrida.passageiro.documento
                    }

                    } for corrida in motorista.corridas
                ]
            }

            res = self.db.collection.insert_one(moto)

            print(f"Motorista criado com o id: {res.inserted_id}")
            return res.inserted_id
        except Exception as e:
            print(f"An error occurred while creating motorista: {e}")
            return None

    def read_motorista_by_id(self, id: str):
        try:
            moto = self.db.collection.find_one({"_id": ObjectId(id)})
            nota = moto['Nota do motorista']
            corrida = moto['Corridas']
            print(f"Motorista found: {moto}")
            return Motorista(nota,corrida)
        except Exception as e:
            print(f"An error occurred while reading motorista: {e}")
            return None

    def update_motorista(self, id, motorista):
        try:
            moto = {
                'Nota do motorista': motorista.notaMotorista, 
                'Corridas': [{
                
                    'Nota da corrida':corrida.notaCorrida, 
                    'Distância':corrida.distancia, 
                    'Valor':corrida.valor, 
                    'Passageiro': {
                        'Nome':corrida.passageiro.nome, 
                        'Documento':corrida.passageiro.documento
                    }

                }for corrida in motorista.corridas
            ]
            }
            res = self.db.collection.update_one({"_id": ObjectId(id)}, {"$set": moto})
            print(f"Motorista atualizado: {res.modified_count} documento(s) modificado(s)")
            return res.modified_count
        except Exception as e:
            print(f"An error occurred while updating motorista: {e}")
            return None

    def delete_motorista(self, id: str):
        try:
            res = self.db.collection.delete_one({"_id": ObjectId(id)})
            print(f"Motorista deletado: {res.deleted_count} documentos(s) deletados")
            return res.deleted_count
        except Exception as e:
            print(f"An error occurred while deleting motorista: {e}")
            return None