class Pagamentos:
    def __init__(self,
                 id_pagamentos: int = None,
                 matricula: int = None,
                 id_contrato: int = None,
                 data_pagamento: str = None,
                 valor_pago: float = None,
                 metodo_pagamento: str = None,
                 tipo_transacao: str = None):
        self.set_id_pagamentos(id_pagamentos)
        self.set_matricula(matricula)
        self.set_id_contrato(id_contrato)
        self.set_data_pagamento(data_pagamento)
        self.set_valor_pago(valor_pago)
        self.set_metodo_pagamento(metodo_pagamento)
        self.set_tipo_transacao(tipo_transacao)

    # Setters
    def set_id_pagamentos(self, id_pagamentos: int):
        self.id_pagamentos = id_pagamentos

    def set_matricula(self, matricula: int):
        self.matricula = matricula

    def set_id_contrato(self, id_contrato: int):
        self.id_contrato = id_contrato

    def set_data_pagamento(self, data_pagamento: str):
        self.data_pagamento = data_pagamento

    def set_valor_pago(self, valor_pago: float):
        self.valor_pago = valor_pago

    def set_metodo_pagamento(self, metodo_pagamento: str):
        self.metodo_pagamento = metodo_pagamento

    def set_tipo_transacao(self, tipo_transacao: str):
        self.tipo_transacao = tipo_transacao

    # Getters
    def get_id_pagamentos(self) -> int:
        return self.id_pagamentos
    
    def get_matricula(self) -> int:
        return self.matricula

    def get_id_contrato(self) -> int:
        return self.id_contrato

    def get_data_pagamento(self) -> str:
        return self.data_pagamento

    def get_valor_pago(self) -> float:
        return self.valor_pago

    def get_metodo_pagamento(self) -> str:
        return self.metodo_pagamento

    def get_tipo_transacao(self) -> str:
        return self.tipo_transacao

    # Representação textual
    def to_string(self) -> str:
        return (f"ID Pagamento: {self.get_id_pagamentos()} | "
                f"Matrícula: {self.get_matricula()} | "
                f"ID Contrato: {self.get_id_contrato()} | "
                f"Data Pagamento: {self.get_data_pagamento()} | "
                f"Valor Pago: R$ {self.get_valor_pago():.2f} | "
                f"Método: {self.get_metodo_pagamento()} | "
                f"Tipo: {self.get_tipo_transacao()}")
