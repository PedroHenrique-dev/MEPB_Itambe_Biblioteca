from estrutura.classesArquivos import *
from estrutura.acoesBiblioteca.funcoesAuxiliares import FuncoesAuxiliares

from estrutura.tratamento import *

class AcaoCadastro(FuncoesAuxiliares, TratamentoErro):
    def cadastrarLivro(self, arquivos: any, biblioteca: any) -> None:
        
        self.__tituloCadastrar()
        codigo = 1001
        if biblioteca != []:
            codigo += biblioteca.__len__()
            
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
            
        biblioteca.insert(0, Livro(codigo, nome, autor, editora, paginas, genero, preco, disponivel, dataCadastro))
        arquivos.atualizarBiblioteca(biblioteca)
        
        print('\nLivro cadastrado com sucesso.')
        return arquivos, biblioteca
        
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
    
    def __tituloCadastrar(self):
        print('''
=====================================================
===================== Cadastrar =====================
=====================================================
''')
        
    def __tituloRemover(self):
        print('''
======================================================
================== Remover Cadastro ==================
======================================================
''')
