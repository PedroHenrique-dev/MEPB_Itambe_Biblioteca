from ..classesArquivos import *
from src.acoesBiblioteca.funcoesAuxiliares import FuncoesAuxiliares
from ..banco import *
from src.tratamento import *
from typing import Type


class AcaoCadastro(FuncoesAuxiliares, TratamentoErro):
    @staticmethod
    def __novo_codigo(banco) -> int:
        codigo = 1001
        ultimo_documento = banco.get_last_document(TypeCollections.LIVROS)
        if ultimo_documento != None:
            codigo = ultimo_documento['codigo'] + 1
        return codigo
    
    def __criar_documento_livro(self, informacoes_livro:list, codigo:int) -> dict:
        nome, autor, editora, paginas, genero, preco = informacoes_livro
        
        if paginas < 6:
            raise ErroSoftware('Quantidade insuficiente!')

        for info in informacoes_livro:
            if type(info) == str:
                self.testeNomeValido(info)
        
        disponivel = True
        data_cadastro = self.gerarDataAtual()
        
        documento = {
            "codigo": codigo,
            "nome": nome,
            "autor": autor,
            "editora": editora,
            "paginas": paginas,
            "genero": genero,
            "preco": preco,
            "disponivel": disponivel,
            "data_cadastro": data_cadastro
        }
        
        return documento

    def app_cadastrar_livro(self, informacoes_livro:list, banco:Type[Banco]) -> None:
        codigo = self.__novo_codigo(banco=banco)
        documento = self.__criar_documento_livro(informacoes_livro=informacoes_livro, codigo=codigo)
        banco.add_document(type_collection=TypeCollections.LIVROS, document=documento)

    def cadastrar_livro(self, banco:Type[Banco]) -> None:
        self.__titulo_cadastrar()

        codigo = self.__novo_codigo(banco=banco)

        try:
            nome = self.inserirNome('Qual o nome do livro? ')
            autor = self.inserirNome('Qual o nome do autor? ')
            editora = self.inserirNome('Qual o nome da editora? ')
            paginas = int(input('Qual a quantidade de páginas? '))
            genero = self.inserirNome('Qual o gênero do livro? ')
            preco = float(input('Qual o preço do livro? '))
        except Exception as erro:
            self.erro(erro)

        informacoes_livro = nome, autor, editora, paginas, genero, preco
        documento = self.__criar_documento_livro(informacoes_livro=informacoes_livro, codigo=codigo)

        banco.add_document(type_collection=TypeCollections.LIVROS, document=documento)
        print('\nLivro cadastrado com sucesso.')

    def remover_livro(self, banco:Type[Banco], codigo_livro:int) -> None:
        existe_documento = banco.exists_document(
            type_collection=TypeCollections.LIVROS,
            data_type={"codigo": codigo_livro}
        )
        
        if existe_documento:
            banco.delete_document(
                type_collection=TypeCollections.LIVROS,
                codigo=codigo_livro
            )
        else:
            raise ErroSoftware('Livro inexistente!')

    def terminal_remover_livro(self, banco:Type[Banco]) -> None:
        self.__titulo_remover()

        try:
            codigo_livro = int(input('Qual o código do livro? '))
        except Exception as erro:
            self.erro(erro)

        self.remover_livro(banco=banco, codigo_livro=codigo_livro) 

    @staticmethod
    def __titulo_cadastrar():
        print('''
======================================================
===================== Cadastrar ======================
======================================================
''')

    @staticmethod
    def __titulo_remover():
        print('''
======================================================
================== Remover Cadastro ==================
======================================================
''')
