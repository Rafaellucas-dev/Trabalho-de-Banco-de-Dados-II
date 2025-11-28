class Instrutor:
    def __init__(self,
                 id_instrutores: int = None,
                 id_gerente: int = None,
                 nome: str = None,
                 cpf: str = None,
                 email: str = None,
                 telefone: str = None,
                 cref: str = None,
                 salario: float = None):
        self.set_id_instrutores(id_instrutores)
        self.set_id_gerente(id_gerente)
        self.set_nome(nome)
        self.set_cpf(cpf)
        self.set_email(email)
        self.set_telefone(telefone)
        self.set_cref(cref)
        self.set_salario(salario)

    # Setters
    def set_id_instrutores(self, id_instrutores: int):
        self.id_instrutores = id_instrutores

    def set_id_gerente(self, id_gerente: int):
        self.id_gerente = id_gerente

    def set_nome(self, nome: str):
        self.nome = nome

    def set_cpf(self, cpf: str):
        self.cpf = cpf

    def set_email(self, email: str):
        self.email = email

    def set_telefone(self, telefone: str):
        self.telefone = telefone

    def set_cref(self, cref: str):
        self.cref = cref

    def set_salario(self, salario: float):
        self.salario = salario

    # Getters
    def get_id_instrutores(self) -> int:
        return self.id_instrutores

    def get_id_gerente(self) -> int:
        return self.id_gerente

    def get_nome(self) -> str:
        return self.nome

    def get_cpf(self) -> str:
        return self.cpf

    def get_email(self) -> str:
        return self.email

    def get_telefone(self) -> str:
        return self.telefone

    def get_cref(self) -> str:
        return self.cref

    def get_salario(self) -> float:
        return self.salario

    # Representação textual
    def to_string(self) -> str:
        return (f"ID Instrutor: {self.get_id_instrutores()} | "
                f"ID Gerente: {self.get_id_gerente()} | "
                f"Nome: {self.get_nome()} | "
                f"CPF: {self.get_cpf()} | "
                f"Email: {self.get_email()} | "
                f"Telefone: {self.get_telefone()} | "
                f"CREF: {self.get_cref()} | "
                f"Salário: {self.get_salario()}")
