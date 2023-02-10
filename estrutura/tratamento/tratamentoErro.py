from estrutura.tratamento.erroSoftware import ErroSoftware

class TratamentoErro:
    def erro(self, erro):
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
        
    def inserirNome(self, pergunta: str):
        nome = str(input(pergunta))
        if len(nome) < 2:
            raise ErroSoftware('Nome inválido. Letras insuficientes!')
        return nome