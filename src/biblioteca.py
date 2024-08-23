from src.gerenciador import *
from src.acoesBiblioteca import *
from .banco import Banco


class Biblioteca(AcaoCadastro, AcaoAluguel, AcaoPesquisar):
    def __init__(self) -> None:
        self.__arquivos = GerenciadorArquivos()
        
        self._banco = Banco(string_connection=self.__arquivos.conexao, string_bank=self.__arquivos.nome_banco)
        
        self.__biblioteca = self.__arquivos.lerArquivoJSON(True)
        self.__alugados = self.__arquivos.lerArquivoJSON(False)

    def app_cadastrar_livro_biblioteca(self, informacoes_livro):
        self.app_cadastrar_livro(
            informacoes_livro=informacoes_livro,
            nome_colecao=self.__arquivos.colecoes['livros'],
            banco=self._banco
        )

    def cadastrar_livro_biblioteca(self):
        self.cadastrar_livro(
            nome_colecao=self.__arquivos.colecoes['livros'],
            banco=self._banco
        )

    def appRemoverLivroBiblioteca(self, codigoLivro):
        self.__arquivos, self.__biblioteca, self.__alugados = self.appRemoverCadastro(codigoLivro, self.__arquivos, self.__biblioteca, self.__alugados)

    def removerLivroBiblioteca(self):
        self.__arquivos, self.__biblioteca, self.__alugados = self.removerCadastro(self.__arquivos, self.__biblioteca, self.__alugados)

    def appAlugarLivroBiblioteca(self, informacoesAluguel):
        self.__arquivos, self.__biblioteca, self.__alugados = self.appAlugar(informacoesAluguel, self.__arquivos, self.__biblioteca, self.__alugados)

    def alugarLivroBiblioteca(self):
        self.__arquivos, self.__biblioteca, self.__alugados = self.alugar(self.__arquivos, self.__biblioteca, self.__alugados)

    def appDevolucaoLivroBiblioteca(self, codigoLivro):
        self.__arquivos, self.__biblioteca, self.__alugados = self.appDevolucao(codigoLivro, self.__arquivos, self.__biblioteca, self.__alugados)

    def devolucaoLivroBiblioteca(self):
        self.__arquivos, self.__biblioteca, self.__alugados = self.devolucao(self.__arquivos, self.__biblioteca, self.__alugados)

    def appPesquisarLivroBiblioteca(self, pesquisa, tipoPesquisa):
        return self.appPesquisarLivro(pesquisa, tipoPesquisa, self.__biblioteca)

    def pesquisarLivroBiblioteca(self):
        self.pesquisarLivro(self.__biblioteca)

    def appPesquisarAluguelBiblioteca(self, pesquisa, tipoPesquisa):
        return self.appPesquisarAluguel(pesquisa, tipoPesquisa, self.__alugados)

    def pesquisarAluguelBiblioteca(self):
        self.pesquisarAluguel(self.__alugados)

    def appMostrarLivrosBiblioteca(self):
        informacoes = self.__appTituloTodosLivros()
        if self.__biblioteca:
            for livro in self.__biblioteca:
                informacoes += livro.getInfo()
        return informacoes

    def mostrarLivrosBiblioteca(self):
        self.__tituloTodosLivros()
        if self.__biblioteca:
            for livro in self.__biblioteca:
                livro.info()
        else:
            print('Não há livro cadastrado.')

    def mostrarQuantidadeLivros(self):
        print(f'Quantidade de livros cadastrados: {len(self.__biblioteca)}')

    def appMostrarAlugadosBiblioteca(self):
        informacoes = self.__appTituloTodosAlugueis()
        if self.__alugados:
            for alugado in self.__alugados:
                informacoes += alugado.getInfo()
        return informacoes

    def mostrarAlugadosBiblioteca(self):
        self.__tituloTodosAlugueis()
        if self.__alugados:
            for alugado in self.__alugados:
                alugado.info()
        else:
            print('Não há livro alugado.')

    def appGastoTotalLivros(self):
        gasto = 0
        for livro in self.__biblioteca:
            gasto += livro.getPreco()

        gastoTotal = f'{gasto:5.2f}'
        return f'R$ {gastoTotal.replace(".", ",")}'

    def gastoTotalLivros(self):
        gasto = 0
        for livro in self.__biblioteca:
            gasto += livro.getPreco()

        gastoTotal = f'{gasto:5.2f}'
        print(f'Gasto total com livros: R$ {gastoTotal.replace(".", ",")}')

    @staticmethod
    def __tituloTodosLivros():
        print('''
======================================================
================== Todos os Livros ===================
======================================================
''')

    @staticmethod
    def __tituloTodosAlugueis():
        print('''
======================================================
================= Todos os Alugueis ==================
======================================================
''')

    @staticmethod
    def __appTituloTodosLivros():
        return '''
============================================
===============  Todos os Livros  ================
============================================
'''

    @staticmethod
    def __appTituloTodosAlugueis():
        return '''
============================================
==============  Todos os Alugueis  ===============
============================================
'''
