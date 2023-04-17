from motorista import Motorista
from passageiro import Passageiro
from corrida import Corrida

class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

    def run(self):
        while True:
            command = input("Entre com um comando: ")
            if command == "quit":
                print("Obrigado!")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Comando inválido. Tente novamente!")


class MotoristaCLI(SimpleCLI):
    def __init__(self, motorista_model):
        super().__init__()
        self.motorista_model = motorista_model
        self.add_command("create", self.create_motorista)
        self.add_command("read", self.read_motorista)
        self.add_command("update", self.update_motorista)
        self.add_command("delete", self.delete_motorista)

    def create_motorista(self):
        corridas = []
        controle = 1
        while(controle == 1):
            nome = input("Entre com o nome do passageiro: ")
            documento = input("Entre com o documento do passageiro: ")
            passageiro = Passageiro(nome,documento)

            notaCorrida = int(input("Entre com a nota da corrida: "))
            distancia = float(input("Entre com a distãncia da corrida: "))
            valor = float(input("Entre com o valor da corrida: "))
            corrida = Corrida(notaCorrida,distancia,valor,passageiro)
            corridas.append(corrida)

            controle = int(input("Adicionar mais corridas?   1- Sim  0- Não   : "))
        
        notaMotorista = int(input("Entre com a nota do motorista: "))
        motorista = Motorista(notaMotorista,corridas)
        self.motorista_model.create_motorista(motorista)

    def read_motorista(self):
        id = input("Entre com o id: ")
        self.motorista_model.read_motorista_by_id(id)
        

    def update_motorista(self):
        id = input("Entre com o id: ")
        print(f"Se você quiser apenas alterar a nota do motorista, digite 0")
        print(f"Se você quiser atualizar as corridas do motorista, digite 1 (Isso apagará todas as corridas atuais)")
        atualiza = int(input("Opção: "))
        if(atualiza == 1):
            controle = 1
            corridas = []
        else:
            controle = 0
        
        while(controle == 1):
            nome = input("Entre com o nome do passageiro: ")
            documento = input("Entre com o documento do passageiro: ")
            passageiro = Passageiro(nome,documento)

            notaCorrida = int(input("Entre com a nota da corrida: "))
            distancia = float(input("Entre com a distãncia da corrida: "))
            valor = float(input("Entre com o valor da corrida: "))
            corrida = Corrida(notaCorrida,distancia,valor,passageiro)
            corridas.append(corrida)

            controle = int(input("Adicionar mais corridas?   1- Sim  0- Não   : "))
        
        notaMotorista = int(input("Entre com a nota do motorista: "))
        motorista = Motorista(notaMotorista,corridas)
        self.motorista_model.update_motorista(id, motorista)
        

    def delete_motorista(self):
        id = input("Entre com o id: ")
        self.motorista_model.delete_motorista(id)
        
    def run(self):
        print("Bem vindo ao CLI Motoristas!")
        print("Comandos disponíveis: create, read, update, delete, quit")
        super().run()
        