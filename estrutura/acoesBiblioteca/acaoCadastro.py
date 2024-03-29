from estrutura.classesArquivos import *
from estrutura.acoesBiblioteca.funcoesAuxiliares import FuncoesAuxiliares

from estrutura.tratamento import *


class AcaoCadastro(FuncoesAuxiliares, TratamentoErro):
    @staticmethod
    def __novoCodigo(biblioteca):
        codigo = 0
        if not biblioteca:
            codigo = 1001
        else:
            indice = biblioteca.__len__() - 1
            codigo += biblioteca[indice].getCodigo() + 1
        return codigo

    def appCadastrarLivro(self, informacoesLivro, arquivos: any, biblioteca: any):
        nome, autor, editora, paginas, genero, preco = informacoesLivro

        if paginas < 6:
            raise ErroSoftware('Quantidade insuficiente!')

        for info in informacoesLivro:
            if type(info) == str:
                self.testeNomeValido(info)

        codigo = self.__novoCodigo(biblioteca)

        disponivel = True
        dataCadastro = self.gerarDataAtual()

        biblioteca.append(Livro(codigo, nome, autor, editora, paginas, genero, preco, disponivel, dataCadastro))
        arquivos.atualizarBiblioteca(biblioteca)

        return arquivos, biblioteca

    def cadastrarLivro(self, arquivos: any, biblioteca: any) -> None:
        self.__tituloCadastrar()

        codigo = self.__novoCodigo(biblioteca)

        try:
            nome = self.inserirNome('Qual o nome do livro? ')
            autor = self.inserirNome('Qual o nome do autor? ')
            editora = self.inserirNome('Qual o nome da editora? ')
            paginas = int(input('Qual a quantidade de páginas? '))
            genero = self.inserirNome('Qual o gênero do livro? ')
            preco = float(input('Qual o preço do livro? '))
        except Exception as erro:
            self.erro(erro)
            return arquivos, biblioteca

        disponivel = True
        dataCadastro = self.gerarDataAtual()

        biblioteca.append(Livro(codigo, nome, autor, editora, paginas, genero, preco, disponivel, dataCadastro))
        arquivos.atualizarBiblioteca(biblioteca)

        print('\nLivro cadastrado com sucesso.')
        return arquivos, biblioteca

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
