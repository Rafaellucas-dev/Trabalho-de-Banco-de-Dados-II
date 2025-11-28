class ContratoPlano:
    def __init__(self,
                 id_contrato: int = None,
                 matricula: int = None,
                 id_plano: int = None,
                 data_inicio: str = None,
                 data_fim: str = None,
                 status: int = None):
        self.set_id_contrato(id_contrato)
        self.set_matricula(matricula)
        self.set_id_plano(id_plano)
        self.set_data_inicio(data_inicio)
        self.set_data_fim(data_fim)
        self.set_status(status)

    # Setters
    def set_id_contrato(self, id_contrato: int):
        self.id_contrato = id_contrato

    def set_matricula(self, matricula: int):
        self.matricula = matricula

    def set_id_plano(self, id_plano: int):
        self.id_plano = id_plano

    def set_data_inicio(self, data_inicio: str):
        self.data_inicio = data_inicio

    def set_data_fim(self, data_fim: str):
        self.data_fim = data_fim

    def set_status(self, status: int):
        self.status = status

    # Getters
    def get_id_contrato(self) -> int:
        return self.id_contrato

    def get_matricula(self) -> int:
        return self.matricula

    def get_id_plano(self) -> int:
        return self.id_plano

    def get_data_inicio(self) -> str:
        return self.data_inicio

    def get_data_fim(self) -> str:
        return self.data_fim

    def get_status(self) -> int:
        return self.status

    # Representação do objeto
    def to_string(self) -> str:
        return (f"ID Contrato: {self.get_id_contrato()} | "
                f"Matrícula: {self.get_matricula()} | "
                f"ID Plano: {self.get_id_plano()} | "
                f"Data Início: {self.get_data_inicio()} | "
                f"Data Fim: {self.get_data_fim()} | "
                f"Status: {self.get_status()}")
