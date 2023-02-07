from estrutura.gerenciador import GerenciadorArquivos
from estrutura.acoesBiblioteca import Cadastro

class Biblioteca(Cadastro):
    def __init__(self) -> None:
        self.__arquivos = GerenciadorArquivos()
        self.__biblioteca = self.__arquivos.lerArquivoJSON(True)
        self.__alugados = self.__arquivos.lerArquivoJSON(False)
        
    def cadastrarLivroBiblioteca(self):
        self.__arquivos, self.__alugados = self.cadastrarLivro(self.__arquivos, self.__alugados)
        
    def removerLivroBiblioteca(self):
        self.__arquivos, self.__alugados, self.__biblioteca = self.removerCadastro(self.__arquivos, self.__alugados, self.__biblioteca)