from estrutura.tratamento import ErroSoftware

class Validador:        
    def validarEntrada(self, senha: str):
        if senha == 'm0kon9ji':
            return True
        else:
            print('\nSenha errada.')
            return False
    
    def appValidarEntrada(self, senha: str):
        if senha == 'm0kon9ji':
            return True
        else:
            raise ErroSoftware('Senha inválida!')
        