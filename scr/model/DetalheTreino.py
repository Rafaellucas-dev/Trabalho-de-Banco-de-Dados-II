from model.Instrutores import Instrutor
from model.Treinos import Treino

class DetalheTreino:
    def __init__(self,
                 id_detalhe: int = None,
                 id_instrutores: int = None,
                 id_treino: int = None,
                 series: int = None,
                 repeticoes: int = None,
                 instrucoes: str = None):
        self.set_id_detalhe(id_detalhe)
        self.set_id_instrutores(id_instrutores)
        self.set_id_treino(id_treino)
        self.set_series(series)
        self.set_repeticoes(repeticoes)
        self.set_instrucoes(instrucoes)

    # Setters
    def set_id_detalhe(self, id_detalhe: int):
        self.id_detalhe = id_detalhe

    def set_id_instrutores(self, id_instrutores: int):
        self.id_instrutores = id_instrutores

    def set_id_treino(self, id_treino: int):
        self.id_treino = id_treino

    def set_series(self, series: int):
        self.series = series

    def set_repeticoes(self, repeticoes: int):
        self.repeticoes = repeticoes

    def set_instrucoes(self, instrucoes: str):
        self.instrucoes = instrucoes

    # Getters
    def get_id_detalhe(self) -> int:
        return self.id_detalhe

    def get_id_instrutores(self) -> int:
        return self.id_instrutores

    def get_id_treino(self) -> int:
        return self.id_treino

    def get_series(self) -> int:
        return self.series

    def get_repeticoes(self) -> int:
        return self.repeticoes

    def get_instrucoes(self) -> str:
        return self.instrucoes

    # Representação textual
    def to_string(self) -> str:
        return (f"ID Detalhe: {self.get_id_detalhe()} | "
                f"ID Instrutor: {self.get_id_instrutores()} | "
                f"ID Treino: {self.get_id_treino()} | "
                f"Séries: {self.get_series()} | "
                f"Repetições: {self.get_repeticoes()} | "
                f"Instruções: {self.get_instrucoes()}")
