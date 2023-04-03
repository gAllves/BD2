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


class LivroCLI(SimpleCLI):
    def __init__(self, livro_model):
        super().__init__()
        self.livro_model = livro_model
        self.add_command("create", self.create_livro)
        self.add_command("read", self.read_livro)
        self.add_command("update", self.update_livro)
        self.add_command("delete", self.delete_livro)

    def create_livro(self):
        id = int(input("Entre com o id: "))
        titulo = input("Entre com o titulo: ")
        autor = input("Entre com o nome autor: ")
        ano = int(input("Entre com o ano de lançamento: "))
        preco = float(input("Entre com o preço do livro: "))
        self.livro_model.create_livro(id,titulo,autor,ano,preco)

    def read_livro(self):
        id = int(input("Entre com o id: "))
        livro = self.livro_model.read_livro_by_id(id)
        if livro:
            print(f"Titulo: {livro['titulo']}")
            print(f"Autor: {livro['autor']}")
            print(f"Ano: {livro['ano']}")
            print(f"Preco: {livro['preco']}")

    def update_livro(self):
        id = int(input("Enter the id: "))
        titulo = input("Entre com o novo título: ")
        autor = input("Entre com o novo autor: ")
        ano = int(input("Entre com o novo ano: "))
        preco = float(input("Entre com o novo preço: "))
        self.livro_model.update_livro(id, titulo, autor, ano, preco)

    def delete_livro(self):
        id = int(input("Entre com o id: "))
        self.livro_model.delete_person(id)
        
    def run(self):
        print("Bem vindo ao CLI livros!")
        print("Comandos disponíveis: create, read, update, delete, quit")
        super().run()
        