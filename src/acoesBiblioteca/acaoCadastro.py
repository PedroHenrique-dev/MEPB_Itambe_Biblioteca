from src.classesArquivos import *
from src.acoesBiblioteca.funcoesAuxiliares import FuncoesAuxiliares

from src.tratamento import *


class AcaoCadastro(FuncoesAuxiliares, TratamentoErro):
    @staticmethod
    def __novoCodigo(banco, nome_colecao):
        codigo = 1001
        ultimo_documento = banco.get_last_document(nome_colecao)
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

    def app_cadastrar_livro(self, informacoes_livro, nome_colecao:str, banco) -> None:
        codigo = self.__novoCodigo(banco=banco, nome_colecao=nome_colecao)
        documento = self.__criar_documento_livro(informacoes_livro=informacoes_livro, codigo=codigo)
        banco.add_document(string_collection=nome_colecao, document=documento)

    def cadastrar_livro(self, nome_colecao:str, banco) -> None:
        self.__tituloCadastrar()

        codigo = self.__novoCodigo(banco=banco, nome_colecao=nome_colecao)

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

        banco.add_document(string_collection=nome_colecao, document=documento)
        print('\nLivro cadastrado com sucesso.')

    def appRemoverCadastro(self, codigoLivro, arquivos: any, biblioteca: any, alugados: any):
        indiceLivro, existeciaCodigo = self.verificaExistenciaLivro(codigoLivro, biblioteca)

        if existeciaCodigo:
            removerAlugado = self.buscarAlugado(biblioteca[indiceLivro].getCodigo(), alugados)
            if removerAlugado != '':
                alugados.remove(removerAlugado)
                arquivos.atualizarAlugados(alugados)
            biblioteca.pop(indiceLivro)
            arquivos.atualizarBiblioteca(biblioteca)
        else:
            raise ErroSoftware('Livro inexistente!')

        return arquivos, biblioteca, alugados

    def removerCadastro(self, arquivos: any, biblioteca: any, alugados: any):
        self.__tituloRemover()

        try:
            codigoLivro = int(input('Qual o código do livro? '))
        except Exception as erro:
            self.erro(erro)
            return arquivos, biblioteca, alugados

        indiceLivro, existeciaCodigo = self.verificaExistenciaLivro(codigoLivro, biblioteca)

        if existeciaCodigo:
            removerAlugado = self.buscarAlugado(biblioteca[indiceLivro].getCodigo(), alugados)
            if removerAlugado != '':
                alugados.remove(removerAlugado)
                arquivos.atualizarAlugados(alugados)
            biblioteca.pop(indiceLivro)
            arquivos.atualizarBiblioteca(biblioteca)

            print('\nLivro removido com sucesso.')
        else:
            print('\nNão existe este livro nos cadastros.')

        return arquivos, biblioteca, alugados

    @staticmethod
    def __tituloCadastrar():
        print('''
======================================================
===================== Cadastrar ======================
======================================================
''')

    @staticmethod
    def __tituloRemover():
        print('''
======================================================
================== Remover Cadastro ==================
======================================================
''')
