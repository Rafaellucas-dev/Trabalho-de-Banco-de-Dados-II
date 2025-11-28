class Gerente:
    def __init__(self,
                 id_gerente: int = None,
                 nome: str = None,
                 telefone: str = None,
                 email: str = None,
                 senha: str = None,
                 salario: float = None):
        self.set_id_gerente(id_gerente)
        self.set_nome(nome)
        self.set_telefone(telefone)
        self.set_email(email)
        self.set_senha(senha)
        self.set_salario(salario)

    # Setters
    def set_id_gerente(self, id_gerente: int):
        self.id_gerente = id_gerente

    def set_nome(self, nome: str):
        self.nome = nome

    def set_telefone(self, telefone: str):
        self.telefone = telefone

    def set_email(self, email: str):
        self.email = email

    def set_senha(self, senha: str):
        self.senha = senha

    def set_salario(self, salario: float):
        self.salario = salario

    # Getters
    def get_id_gerente(self) -> int:
        return self.id_gerente

    def get_nome(self) -> str:
        return self.nome

    def get_telefone(self) -> str:
        return self.telefone

    def get_email(self) -> str:
        return self.email

    def get_senha(self) -> str:
        return self.senha

    def get_salario(self) -> float:
        return self.salario

    # Representação textual
    def to_string(self) -> str:
        return (f"ID Gerente: {self.get_id_gerente()} | "
                f"Nome: {self.get_nome()} | "
                f"Telefone: {self.get_telefone()} | "
                f"Email: {self.get_email()} | "
                f"Senha: {self.get_senha()} | "
                f"Salário: {self.get_salario()}")
