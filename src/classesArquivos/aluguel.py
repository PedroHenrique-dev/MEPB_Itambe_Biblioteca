class Aluguel:
    def __init__(self, nomePessoa: str, codigo: int, nomeLivro: str, dataAluguel: str, dataEntrega: str) -> None:
        self.__nomePessoa = nomePessoa
        self.__codigo = codigo
        self.__nomeLivro = nomeLivro
        self.__dataAluguel = dataAluguel
        self.__dataEntrega = dataEntrega

    def info(self) -> None:
        print(f'''______________________________________________________
    * Livro {self.__codigo} *
Nome da pessoa: {self.__nomePessoa}
Codigo: {self.__codigo}
Nome do livro: {self.__nomeLivro}
Data do aluguel: {self.__dataAluguel}
Data da entrega: {self.__dataEntrega}
______________________________________________________''')

    def getNomePessoa(self):
        return self.__nomePessoa 
    
    def getCodigo(self):
        return self.__codigo
    
    def getNomeLivro(self):
        return self.__nomeLivro
    
    def getDataAluguel(self):
        return self.__dataAluguel
    
    def getDataEntrega(self):
        return self.__dataEntrega
    
    def getInfo(self):
        informacoes = f'''_________________________________________________

    * Livro {self.__codigo} *
Nome da pessoa: {self.__nomePessoa}
Codigo: {self.__codigo}
Nome do livro: {self.__nomeLivro}
Data do aluguel: {self.__dataAluguel}
Data da entrega: {self.__dataEntrega}
'''
        return informacoes