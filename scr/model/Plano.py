class Plano:
    def __init__(self, 
                 id_plano: int = None, 
                 nome_plano: str = None, 
                 valor: float = None, 
                 tipo_plano: str = None):
        self.set_id_plano(id_plano)
        self.set_nome_plano(nome_plano)
        self.set_valor(valor)
        self.set_tipo_plano(tipo_plano)

    def set_id_plano(self, id_plano: int):
        self.id_plano = id_plano

    def set_nome_plano(self, nome_plano: str):
        self.nome_plano = nome_plano

    def set_valor(self, valor: float):
        self.valor = valor

    def set_tipo_plano(self, tipo_plano: str):
        self.tipo_plano = tipo_plano

    def get_id_plano(self) -> int:
        return self.id_plano

    def get_nome_plano(self) -> str:
        return self.nome_plano

    def get_valor(self) -> float:
        return self.valor

    def get_tipo_plano(self) -> str:
        return self.tipo_plano

    def to_string(self) -> str:
        return (f"ID Plano: {self.get_id_plano()} | "
                f"Nome Plano: {self.get_nome_plano()} | "
                f"Valor: R$ {self.get_valor():.2f} | "
                f"Tipo Plano: {self.get_tipo_plano()}")
