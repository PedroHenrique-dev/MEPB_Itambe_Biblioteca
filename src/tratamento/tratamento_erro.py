from src.tratamento.erro_software import ErroSoftware


class TratamentoErro:
    @staticmethod
    def erro(erro: any):
        if isinstance(erro, ErroSoftware):
            print(f'\nErro: {erro}')

        if isinstance(erro, ValueError):
            print('\nVocê inseriu tipo de dado incompatível.')

        if isinstance(erro, TypeError):
            print('\nVocê inseriu tipo de dado incompatível.')

        if isinstance(erro, Exception):
            print(type(erro))

    @staticmethod
    def teste_nome_valido(nome: str):
        if isinstance(type(nome), str) and len(nome) < 2:
            raise ErroSoftware('Nome inválido. Letras insuficientes!')
