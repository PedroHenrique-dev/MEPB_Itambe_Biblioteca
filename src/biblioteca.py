from src.acoesBiblioteca import *
from src.gerenciador import *
from .banco import Banco


class Biblioteca(AcaoCadastro, AcaoAluguel, AcaoPesquisar):
    def __init__(self) -> None:
        self.__arquivos = GerenciadorArquivos()

        self._banco = Banco(string_connection=self.__arquivos.conexao, string_bank=self.__arquivos.nome_banco)

        self.__biblioteca = self.__arquivos.lerArquivoJSON(True)
        self.__alugados = self.__arquivos.lerArquivoJSON(False)

    def app_cadastrar_livro_biblioteca(self, informacoes_livro: list) -> None:
        self.app_cadastrar_livro(banco=self._banco, informacoes_livro=informacoes_livro)

    def cadastrar_livro_biblioteca(self) -> None:
        self.cadastrar_livro(banco=self._banco)

    def app_remover_livro_biblioteca(self, codigo_livro: int) -> None:
        self.remover_livro(banco=self._banco, codigo_livro=codigo_livro)

    def remover_livro_biblioteca(self) -> None:
        self.terminal_remover_livro(self._banco)

    def app_alugar_livro_biblioteca(self, informacoes_aluguel: list) -> None:
        self.alugar(banco=self._banco, informacoes_aluguel=informacoes_aluguel)

    def alugar_livro_biblioteca(self) -> None:
        self.terminal_alugar(banco=self._banco)

    def app_devolucao_livro_biblioteca(self, codigo_livro: int) -> None:
        self.app_devolucao(banco=self._banco, codigo_livro=codigo_livro)

    def devolucao_livro_biblioteca(self) -> None:
        self.devolucao(banco=self._banco)

    def app_pesquisar_livro_biblioteca(self, pesquisa: str, tipo_pesquisa: str):
        return self.pesquisar_livro(banco=self._banco, pesquisa=pesquisa, tipo_pesquisa=tipo_pesquisa)

    def pesquisar_livro_biblioteca(self):
        self.terminal_pesquisar_livro(banco=self._banco)

    def appPesquisarAluguelBiblioteca(self, pesquisa, tipoPesquisa):
        return self.pesquisar_aluguel(banco=self._banco, pesquisa=pesquisa, tipo_pesquisa=tipoPesquisa)

    def pesquisarAluguelBiblioteca(self):
        self.terminal_pesquisar_aluguel(self.__alugados)

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
