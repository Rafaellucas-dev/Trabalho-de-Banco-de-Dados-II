from model.Instrutores import Instrutor

class Aluno:
    def __init__(self,
                 matricula: int = None,
                 id_instrutores: int = None,
                 id_gerente: int = None,
                 nome: str = None,
                 email: str = None,
                 cpf: str = None,
                 telefone: str = None,
                 status: int = None):
        self.set_matricula(matricula)
        self.set_id_instrutores(id_instrutores)
        self.set_id_gerente(id_gerente)
        self.set_nome(nome)
        self.set_email(email)
        self.set_cpf(cpf)
        self.set_telefone(telefone)
        self.set_status(status)

    def set_matricula(self, matricula: int):
        self.matricula = matricula
    
    def set_id_instrutores(self, id_instrutores: int):
        self.id_instrutores = id_instrutores
    
    def set_id_gerente(self, id_gerente: int):
        self.id_gerente = id_gerente
    
    def set_nome(self, nome: str):
        self.nome = nome

    def set_email(self, email: str):
        self.email = email

    def set_cpf(self, cpf: str):
        self.cpf = cpf

    def set_telefone(self, telefone: str):
        self.telefone = telefone

    def set_status(self, status: int):
        self.status = status
    
    def get_matricula(self) -> int:
        return self.matricula
    
    def get_id_instrutores(self) -> int:
        return self.id_instrutores
    
    def get_id_gerente(self) -> int:
        return self.id_gerente
    
    def get_nome(self) -> str:
        return self.nome 

    def get_email(self) -> str:
        return self.email

    def get_cpf(self) -> str:
        return self.cpf 

    def get_telefone(self) -> str:
        return self.telefone

    def get_status(self) -> int:
        return self.status

    def to_string(self) -> str:
        return (f"Matrícula: {self.get_matricula()} | "
                f"ID Instrutor: {self.get_id_instrutores()} | "
                f"ID Gerente: {self.get_id_gerente()} | "
                f"Nome: {self.get_nome()} | "
                f"Email: {self.get_email()} | "
                f"CPF: {self.get_cpf()} | "
                f"Telefone: {self.get_telefone()} | "
                f"Status: {self.get_status()}")
