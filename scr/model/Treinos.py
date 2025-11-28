class Treino:
    def __init__(self,
                 id_treino: int = None,
                 matricula: int = None,
                 nome_treino: str = None,
                 musculo_alvo: str = None,
                 objetivo: str = None,
                 duracao: int = None):
        self.set_id_treino(id_treino)
        self.set_matricula(matricula)
        self.set_nome_treino(nome_treino)
        self.set_musculo_alvo(musculo_alvo)
        self.set_objetivo(objetivo)
        self.set_duracao(duracao)

    # Setters
    def set_id_treino(self, id_treino: int):
        self.id_treino = id_treino

    def set_matricula(self, matricula: int):
        self.matricula = matricula

    def set_nome_treino(self, nome_treino: str):
        self.nome_treino = nome_treino

    def set_musculo_alvo(self, musculo_alvo: str):
        self.musculo_alvo = musculo_alvo

    def set_objetivo(self, objetivo: str):
        self.objetivo = objetivo

    def set_duracao(self, duracao: int):
        self.duracao = duracao

    # Getters
    def get_id_treino(self) -> int:
        return self.id_treino

    def get_matricula(self) -> int:
        return self.matricula

    def get_nome_treino(self) -> str:
        return self.nome_treino

    def get_musculo_alvo(self) -> str:
        return self.musculo_alvo

    def get_objetivo(self) -> str:
        return self.objetivo

    def get_duracao(self) -> int:
        return self.duracao

    # Representação textual
    def to_string(self) -> str:
        return (f"ID Treino: {self.get_id_treino()} | "
                f"Matrícula: {self.get_matricula()} | "
                f"Nome: {self.get_nome_treino()} | "
                f"Músculo Alvo: {self.get_musculo_alvo()} | "
                f"Objetivo: {self.get_objetivo()} | "
                f"Duração: {self.get_duracao()} min")
