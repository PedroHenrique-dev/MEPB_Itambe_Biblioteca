class Validador:
    def __init__(self) -> None:
        self.__senha = 'm0kon9ji'
        
    def validarEntrada(self, senha: str):
        if self.__senha == senha:
            return True
        else:
            print('\nSenha errada.')
            return False
        