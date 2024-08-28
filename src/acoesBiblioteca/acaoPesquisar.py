from os import system

from src.tratamento import *
from ..banco import *


class AcaoPesquisar(TratamentoErro):
    def __menu_pesquisa_livro(self) -> int:
        print('''
======================================================
================ Menu Pesquisa: Livro ================
======================================================
1. Código   |    2. Nome      |    3. Autor
4. Editora  |    5. Gênero    |    6. Disponibilidade
0. Sair
              ''')
        try:
            escolha_opcao = int(input('Digite a opção da ação desejada: '))

            if escolha_opcao < 0 or escolha_opcao > 6:
                raise ErroSoftware('Opção inválida!')

            return escolha_opcao
        except Exception as erro:
            self.erro(erro)

    def pesquisar_livro(self, banco: Banco, pesquisa: str, tipo_pesquisa: str) -> str:
        if pesquisa == 'Disponível':
            pesquisa = True
        elif pesquisa == 'Indisponível':
            pesquisa = False

        if type(pesquisa) == str and tipo_pesquisa == 'codigo':
            pesquisa = int(pesquisa)

        filtro_documento = {tipo_pesquisa: pesquisa}

        existe_documento = banco.exists_document(
            type_collection=TypeCollections.LIVROS,
            data_type=filtro_documento
        )

        informacoes = '    *** Livros ***\n'

        if existe_documento:
            documentos = banco.find_document(type_collection=TypeCollections.LIVROS, data_type=filtro_documento)
            for documento in documentos:
                informacoes += self._exibir_info_livro(documento=documento)
        return informacoes

    def terminal_pesquisar_livro(self, banco: Banco):
        while True:
            system('clear')
            escolha = self.__menu_pesquisa_livro()

            pesquisa = str
            tipo_pesquisa = str
            try:
                match escolha:
                    case 1:
                        pesquisa = int(input('Qual o código do livro? '))
                        tipo_pesquisa = 'codigo'
                    case 2:
                        pesquisa = self.inserirNome('Qual o nome do livro? ')
                        tipo_pesquisa = 'nome'
                    case 3:
                        pesquisa = self.inserirNome('Qual o nome do autor? ')
                        tipo_pesquisa = 'autor'
                    case 4:
                        pesquisa = self.inserirNome('Qual o nome da editora? ')
                        tipo_pesquisa = 'editora'
                    case 5:
                        pesquisa = self.inserirNome('Qual o gênero do livro? ')
                        tipo_pesquisa = 'genero'
                    case 6:
                        pesquisa = self.inserirNome('Qual a disponibilidade do livro? (Disponível | Indisponível): ')
                        tipo_pesquisa = 'disponibilidade'
                    case 0:
                        break
                print(self.pesquisar_livro(banco=banco, pesquisa=pesquisa, tipo_pesquisa=tipo_pesquisa))
            except Exception as erro:
                self.erro(erro)
            input("\nAperte 'Enter' para continuar.")

    def __menu_pesquisa_aluguel(self):
        print('''
======================================================
=============== Menu Pesquisa: Aluguel ===============
======================================================
1. Código do livro  |    2. Nome do livro
3. Data de aluguel  |    4. Data de entrega
5. Nome da pessoa   |    0. Sair
              ''')
        try:
            escolha_opcao = int(input('Digite a opção da ação desejada: '))

            if escolha_opcao < 0 or escolha_opcao > 5:
                raise ErroSoftware('Opção inválida!')

            return escolha_opcao
        except Exception as erro:
            self.erro(erro)

    def pesquisar_aluguel(self, banco: Banco, pesquisa: str, tipo_pesquisa: str) -> str:
        if tipo_pesquisa == 'codigo':
            pesquisa = int(pesquisa)

        filtro_documento = {tipo_pesquisa: pesquisa}

        existe_documento = banco.exists_document(
            type_collection=TypeCollections.ALUGUEIS,
            data_type=filtro_documento
        )

        informacoes = '    *** Alugueis ***\n'

        if existe_documento:
            documentos = banco.find_document(type_collection=TypeCollections.ALUGUEIS, data_type=filtro_documento)
            for documento in documentos:
                informacoes += self._exibir_info_aluguel(documento=documento)
        return informacoes

    def terminal_pesquisar_aluguel(self, banco: Banco):
        while True:
            system('clear')
            escolha = self.__menu_pesquisa_aluguel()

            pesquisa = str
            tipo_pesquisa = str
            try:
                match escolha:
                    case 1:
                        pesquisa = int(input('Qual o código do livro? '))
                        tipo_pesquisa = 'codigo'
                    case 2:
                        pesquisa = self.inserirNome('Qual o nome do livro? ')
                        tipo_pesquisa = 'nome_livro'
                    case 3:
                        pesquisa = self.inserirNome('Qual a data do aluguel? ')
                        tipo_pesquisa = 'data_aluguel'
                    case 4:
                        pesquisa = self.inserirNome('Qual a data de devolução? ')
                        tipo_pesquisa = 'data_entrega'
                    case 5:
                        pesquisa = self.inserirNome('Qual o nome da pessoa? ')
                        tipo_pesquisa = 'nome_pessoa'
                    case 0:
                        break
                print(self.pesquisar_aluguel(banco=banco, pesquisa=pesquisa, tipo_pesquisa=tipo_pesquisa))
            except Exception as erro:
                self.erro(erro)
            input("\nAperte 'Enter' para continuar.")

    @staticmethod
    def _exibir_info_livro(documento: dict) -> str:
        disponibilidade = 'Disponível' if documento['disponibilidade'] else 'Indisponível'
        return f'''__________________________________________________
    * Livro {documento['codigo']} *
Nome: {documento['nome']}
Autor: {documento['autor']}
Editora: {documento['editora']}
Páginas: {documento['paginas']}
Gênero: {documento['genero']}
Disponibilidade para alugar: {disponibilidade}
Data de cadastro: {documento['data_cadastro']}
__________________________________________________ '''

    @staticmethod
    def _exibir_info_aluguel(documento: dict) -> str:
        return f'''__________________________________________________
    * Livro {documento['codigo']} *
Nome da pessoa: {documento['nome_pessoa']}
Codigo: {documento['codigo']}
Nome do livro: {documento['nome_livro']}
Data do aluguel: {documento['data_aluguel']}
Data da entrega: {documento['data_entrega']}
Multa: {documento['multa']}
__________________________________________________'''
