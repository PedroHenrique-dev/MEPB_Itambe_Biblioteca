from estrutura.gerenciador import *
from estrutura.acoesBiblioteca import *

class Biblioteca(AcaoCadastro, AcaoAluguel, AcaoPesquisar):
    def __init__(self) -> None:
        super().__init__()
        self.__arquivos = GerenciadorArquivos()
        self.__biblioteca = self.__arquivos.lerArquivoJSON(True)
        self.__alugados = self.__arquivos.lerArquivoJSON(False)
        
    def cadastrarLivroBiblioteca(self):
        self.__arquivos, self.__biblioteca = self.cadastrarLivro(self.__arquivos, self.__biblioteca)
        
    def removerLivroBiblioteca(self):
        self.__arquivos, self.__biblioteca, self.__alugados = self.removerCadastro(self.__arquivos, self.__biblioteca, self.__alugados)
        
    def alugarLivroBiblioteca(self):
        self.__arquivos, self.__biblioteca, self.__alugados = self.alugar(self.__arquivos, self.__biblioteca, self.__alugados)
    
    def devolucaoLivroBiblioteca(self):
        self.__arquivos, self.__biblioteca, self.__alugados = self.devolucao(self.__arquivos, self.__biblioteca, self.__alugados)
    
    def pesquisarLivroBiblioteca(self):
        self.pesquisarLivro(self.__biblioteca)
    
    def pesquisarAluguelBiblioteca(self):
        self.pesquisarAluguel(self.__alugados)
    
    def mostrarLivrosBiblioteca(self):
        self.__tituloTodosLivros()
        if self.__biblioteca != []:
            for livro in self.__biblioteca:
                livro.info()
        else:
            print('Não há livro cadastrado.')
    
    def mostrarAlugadosBiblioteca(self):
        self.__tituloTodosAlugueis()
        if self.__alugados != []:
            for alugado in self.__alugados:
                alugado.info()
        else:
            print('Não há livro alugado.')
                
    def __tituloTodosLivros(self):
        print('''
=====================================================
================== Todos os Livros ==================
=====================================================
''')
    
    def __tituloTodosAlugueis(self):
        print('''
=====================================================
================= Todos os Alugueis =================
=====================================================
''')