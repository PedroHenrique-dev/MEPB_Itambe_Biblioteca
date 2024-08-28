from datetime import date

from src.banco import Banco, TypeCollections
from src.tratamento import TratamentoErro, ErroSoftware


class AcaoCadastro(TratamentoErro):
    data_atual = date.today().strftime('%d/%m/%Y')

    @staticmethod
    def __novo_codigo(banco) -> int:
        codigo = 1001
        ultimo_documento = banco.get_last_document(TypeCollections.LIVROS)
        if ultimo_documento != {}:
            codigo = ultimo_documento['codigo'] + 1
        return codigo

    def __criar_documento_livro(self, informacoes_livro: list, codigo: int) -> dict:
        nome, autor, editora, paginas, genero, preco = informacoes_livro

        if paginas < 6:
            raise ErroSoftware('Quantidade insuficiente!')

        for info in informacoes_livro:
            if type(info) == str:
                self.teste_nome_valido(info)

        documento = {
            "codigo": codigo,
            "nome": nome,
            "autor": autor,
            "editora": editora,
            "paginas": paginas,
            "genero": genero,
            "preco": preco,
            "disponibilidade": True,
            "data_cadastro": AcaoCadastro.data_atual
        }

        return documento

    def app_cadastrar_livro(self, banco: Banco, informacoes_livro: list) -> None:
        codigo = self.__novo_codigo(banco=banco)
        livro = self.__criar_documento_livro(informacoes_livro=informacoes_livro, codigo=codigo)
        banco.add_document(type_collection=TypeCollections.LIVROS, document=livro)

    def cadastrar_livro(self, banco: Banco) -> None:
        self.__titulo_cadastrar()

        codigo = self.__novo_codigo(banco=banco)

        try:
            nome = self.inserir_nome('Qual o nome do livro? ')
            autor = self.inserir_nome('Qual o nome do autor? ')
            editora = self.inserir_nome('Qual o nome da editora? ')
            paginas = int(input('Qual a quantidade de páginas? '))
            genero = self.inserir_nome('Qual o gênero do livro? ')
            preco = float(input('Qual o preço do livro? '))

            informacoes_livro = [nome, autor, editora, paginas, genero, preco]
            documento = self.__criar_documento_livro(informacoes_livro=informacoes_livro, codigo=codigo)

            banco.add_document(type_collection=TypeCollections.LIVROS, document=documento)
            print('\nLivro cadastrado com sucesso.')
        except Exception as erro:
            self.erro(erro)

    @staticmethod
    def remover_livro(banco: Banco, codigo_livro: int) -> None:
        existe_documento = banco.exists_document(
            type_collection=TypeCollections.LIVROS,
            data_type={"codigo": codigo_livro}
        )

        if existe_documento:
            banco.delete_document(
                type_collection=TypeCollections.LIVROS,
                code_document_delete=codigo_livro
            )
        else:
            raise ErroSoftware('Livro inexistente!')

    def terminal_remover_livro(self, banco: Banco) -> None:
        self.__titulo_remover()

        codigo = int
        try:
            codigo = int(input('Qual o código do livro? '))
        except Exception as erro:
            self.erro(erro)

        self.remover_livro(banco=banco, codigo_livro=codigo)

    @staticmethod
    def __titulo_cadastrar() -> None:
        print('''
======================================================
===================== Cadastrar ======================
======================================================
''')

    @staticmethod
    def __titulo_remover() -> None:
        print('''
======================================================
================== Remover Cadastro ==================
======================================================
''')
