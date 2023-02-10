class Validador:        
    def validarEntrada(self, senha: str):
        if senha == 'm0kon9ji':
            return True
        else:
            print('\nSenha errada.')
            return False
        