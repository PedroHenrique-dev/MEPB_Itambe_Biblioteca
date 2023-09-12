class Aluguel:
    def __init__(self, nomePessoa: str, codigo: int, nomeLivro: str, dataAluguel: str, dataEntega: str) -> None:
        self.__nomePessoa = nomePessoa
        self.__codigo = codigo
        self.__nomeLivro = nomeLivro
        self.__dataAluguel = dataAluguel
        self.__dataEntega = dataEntega

    def info(self) -> None:
        print(
f'''______________________________________________________
    * Livro {self.__codigo} *
Nome da pessoa: {self.__nomePessoa}
Codigo: {self.__codigo}
Nome do livro: {self.__nomeLivro}
Data do aluguel: {self.__dataAluguel}
Data da entega: {self.__dataEntega}
______________________________________________________''')

    def getNomePessoa(self):
        return self.__nomePessoa 
    
    def getCodigo(self):
        return self.__codigo
    
    def getNomeLivro(self):
        return self.__nomeLivro
    
    def getDataAluguel(self):
        return self.__dataAluguel
    
    def getDataEntega(self):
        return self.__dataEntega
    
    def getInfo(self):
        informacoes = f'''_________________________________________________

    * Livro {self.__codigo} *
Nome da pessoa: {self.__nomePessoa}
Codigo: {self.__codigo}
Nome do livro: {self.__nomeLivro}
Data do aluguel: {self.__dataAluguel}
Data da entega: {self.__dataEntega}
'''
        return informacoes