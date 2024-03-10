from estrutura.tratamento import ErroSoftware


class Validador:        
    @staticmethod
    def validarEntrada(senha: str):
        if senha == 'm0kon9ji':
            return True
        else:
            print('\nSenha errada.')
            return False
    
    @staticmethod
    def appValidarEntrada(senha: str):
        if senha == 'm0kon9ji':
            return True
        else:
            raise ErroSoftware('Senha inválida!')
        