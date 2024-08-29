from .acoes import AcaoCadastro, AcaoAluguel, AcaoPesquisar
from .banco import Banco, TypeCollections
from .config import Configuracao


class Biblioteca(AcaoCadastro, AcaoAluguel, AcaoPesquisar):
    def __init__(self) -> None:
        configuracao = Configuracao()
        self._banco = Banco(string_connection=configuracao.conexao, string_bank=configuracao.nome_banco)

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

    def app_pesquisar_livro_biblioteca(self, pesquisa: str, tipo_pesquisa: str) -> str:
        return self.pesquisar_livro(banco=self._banco, pesquisa=pesquisa, tipo_pesquisa=tipo_pesquisa)

    def pesquisar_livro_biblioteca(self) -> None:
        self.terminal_pesquisar_livro(banco=self._banco)

    def app_pesquisar_aluguel_biblioteca(self, pesquisa: str, tipo_pesquisa: str) -> str:
        return self.pesquisar_aluguel(banco=self._banco, pesquisa=pesquisa, tipo_pesquisa=tipo_pesquisa)

    def pesquisar_aluguel_biblioteca(self) -> None:
        self.terminal_pesquisar_aluguel(banco=self._banco)

    def app_mostrar_livros_biblioteca(self) -> str:
        return self._pesquisar_livros(self._app_titulo_todos_livros())

    def mostrar_livros_biblioteca(self) -> None:
        print(self._pesquisar_livros(self._titulo_todos_livros()))

    def app_mostrar_alugados_biblioteca(self) -> str:
        return self._pesquisar_alugueis(self._app_titulo_todos_alugueis())

    def mostrar_alugados_biblioteca(self) -> None:
        print(self._pesquisar_alugueis(self._titulo_todos_alugueis()))

    def mostrar_quantidade_livros(self) -> None:
        existe_documento = self._banco.exists_document(type_collection=TypeCollections.ALUGUEIS, data_type={})
        if existe_documento:
            livros = self._banco.find_document(type_collection=TypeCollections.LIVROS, data_type={})
            print(f'Quantidade de livros cadastrados: {livros.__len__()}')
        else:
            print('Não há livro.')

    def app_gasto_total_livros(self) -> str:
        gasto = 0
        livros = self._banco.find_document(type_collection=TypeCollections.LIVROS, data_type={})
        for livro in livros:
            gasto += livro['preco']
        gasto_total = f'{gasto:5.2f}'
        return f'R$ {gasto_total.replace(".", ",")}'

    def terminal_gasto_total_livros(self) -> None:
        gasto = self.app_gasto_total_livros()
        print(f'Gasto total com livros: R$ {gasto}')

    def _pesquisar_livros(self, informacoes: str) -> str:
        existe_documento = self._banco.exists_document(type_collection=TypeCollections.ALUGUEIS, data_type={})
        if existe_documento:
            livros = self._banco.find_document(type_collection=TypeCollections.LIVROS, data_type={})
            for livro in livros:
                informacoes += self._mostrar_info_livro(livro=livro)
            return informacoes
        else:
            return 'Não há livro.'

    def _pesquisar_alugueis(self, informacoes: str) -> str:
        existe_documento = self._banco.exists_document(type_collection=TypeCollections.ALUGUEIS, data_type={})
        if existe_documento:
            alugueis = self._banco.find_document(type_collection=TypeCollections.ALUGUEIS, data_type={})
            for aluguel in alugueis:
                informacoes += self._mostrar_info_aluguel(aluguel=aluguel)
            return informacoes
        return 'Não há livro alugado.'

    @staticmethod
    def _mostrar_info_aluguel(aluguel: dict) -> str:
        return f'''_________________________________________________

    * Livro {aluguel['codigo']} *
Nome da pessoa: {aluguel['nome_pessoa']}
Codigo: {aluguel['codigo']}
Nome do livro: {aluguel['nome_livro']}
Data do aluguel: {aluguel['data_aluguel']}
Data da entrega: {aluguel['data_entrega']}
Multa: {aluguel['multa']}
'''

    @staticmethod
    def _mostrar_info_livro(livro: dict) -> str:
        disponibilidade = 'Disponível' if livro['disponibilidade'] else 'Indisponível'
        return f'''_________________________________________________

    * Livro {livro['codigo']} *
Nome: {livro['nome']}
Autor: {livro['autor']}
Editora: {livro['editora']}
Páginas: {livro['paginas']}
Gênero: {livro['genero']}
Disponibilidade para alugar: {disponibilidade}
Data de cadastro: {livro['data_cadastro']}
'''

    @staticmethod
    def _titulo_todos_livros() -> str:
        return ('''
======================================================
================== Todos os Livros ===================
======================================================
''')

    @staticmethod
    def _titulo_todos_alugueis() -> str:
        return ('''
======================================================
================= Todos os Alugueis ==================
======================================================
''')

    @staticmethod
    def _app_titulo_todos_livros() -> str:
        return '''
============================================
===============  Todos os Livros  ================
============================================
'''

    @staticmethod
    def _app_titulo_todos_alugueis() -> str:
        return '''
============================================
==============  Todos os Alugueis  ===============
============================================
'''
