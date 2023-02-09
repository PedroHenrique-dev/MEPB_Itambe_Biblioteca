from estrutura.classesArquivos import *
from estrutura.acoesBiblioteca.funcoesAuxiliares import FuncoesAuxiliares
from datetime import date

class AcaoCadastro(FuncoesAuxiliares):
    def cadastrarLivro(self, arquivos: any, biblioteca: any) -> None:
        self.__tituloCadastrar()
        codigo = 1001
        if biblioteca != []:
            codigo += biblioteca.__len__()
        nome = str(input('Qual o nome do livro? '))
        autor = str(input('Qual o nome do autor? '))
        editora = str(input('Qual o nome da editora? '))
        paginas = int(input('Qual a quantidade de páginas? '))
        genero = str(input('Qual o gênero do livro? '))
        preco = float(input('Qual o preço do livro? '))
        disponivel = True
        dataCadastro = date.today().strftime('%d/%m/%Y')
        
        biblioteca.insert(0, Livro(codigo, nome, autor, editora, paginas, genero, preco, disponivel, dataCadastro))
        arquivos.atualizarBiblioteca(biblioteca)
        
        print('\nLivro cadastrado com sucesso.')
        return arquivos, biblioteca
        
    def removerCadastro(self, arquivos: any, biblioteca: any, alugados: any):
        self.__tituloRemover()
        codigoLivro = int(input('Qual o código do livro? '))
        indiceLivro, existeciaCodigo = self.verificaExistenciaLivro(codigoLivro, biblioteca)
        
        if existeciaCodigo:
            removerAlugado = self.__buscarAlugado(biblioteca[indiceLivro].getCodigo(), alugados)
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