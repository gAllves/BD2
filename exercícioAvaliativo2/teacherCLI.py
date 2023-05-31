class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

    def run(self):
        while True:
            command = input("Entre com o comando: ")
            if command == "quit":
                print("Adeus!")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Comando inválido. Por favor entre novamente!")


class TeacherCLI(SimpleCLI):
    def __init__(self, teacher_model):
        super().__init__()
        self.teacher_model = teacher_model
        self.add_command("create", self.create_teacher)
        self.add_command("read", self.read_teacher)
        self.add_command("update", self.update_teacher)
        self.add_command("delete", self.delete_teacher)

    def create_teacher(self):
        name = input("Entre com o nome: ")
        ano_nasc = int(input("Entre com o ano do nascimento: "))
        cpf = input("Entre com o CPF: ")
        self.teacher_model.create(name, ano_nasc, cpf)
        print("Professor criado com sucesso")

    def read_teacher(self):
        name = input("Entre com o nome: ")
        teacher = self.teacher_model.read(name)
        if teacher:
            _properties = teacher[0]._properties
            ano_nasc = _properties.get('ano_nasc')
            cpf = _properties.get('cpf')
            name = _properties.get('name')
            if ano_nasc:
                print(f"Ano de Nascimento: {ano_nasc}")
            if cpf:
                print(f"CPF: {cpf}")
            if name:
                print(f"Nome: {name}")

    def update_teacher(self):
        name = input("Entre com o nome: ")
        new_cpf = input("Entre com o novo cpf: ")
        self.teacher_model.update(name, new_cpf)

    def delete_teacher(self):
        name = input("Entre com o nome: ")
        self.teacher_model.delete(name)
        
    def run(self):
        print("Bem vindo ao Professor CLI!")
        print("Available commands: create, read, update, delete, quit")
        super().run()
        