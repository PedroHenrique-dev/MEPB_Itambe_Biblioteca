from src.tratamento import ErroSoftware


class Validador:
    @staticmethod
    def app_validar_entrada(senha: str):
        if senha == 'm0kon9ji':
            return True
        else:
            raise ErroSoftware('Senha inválida!')
