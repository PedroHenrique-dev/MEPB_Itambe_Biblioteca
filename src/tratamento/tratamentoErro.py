from src.tratamento.erroSoftware import ErroSoftware


class TratamentoErro:
    @staticmethod
    def erro(erro):
        if isinstance(erro, ErroSoftware):
            print(f'\nErro: {erro}')
            return

        if isinstance(erro, ValueError):
            print('\nVocê inseriu tipo de dado incompatível.')
            return

        if isinstance(erro, TypeError):
            print('\nVocê inseriu tipo de dado incompatível.')
            return

        if isinstance(erro, Exception):
            print(type(erro))
            return

    @staticmethod
    def inserirNome(pergunta: str):
        nome = str(input(pergunta))
        if len(nome) < 2:
            raise ErroSoftware('Nome inválido. Letras insuficientes!')
        return nome

    @staticmethod
    def testeNomeValido(nome):
        if len(nome) < 2:
            raise ErroSoftware('Nome inválido. Letras insuficientes!')
