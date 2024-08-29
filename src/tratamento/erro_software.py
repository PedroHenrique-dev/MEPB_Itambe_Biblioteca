class ErroSoftware(Exception):
    def __init__(self, mensagem) -> None:
        super().__init__(mensagem)
        self.mensagem = mensagem
