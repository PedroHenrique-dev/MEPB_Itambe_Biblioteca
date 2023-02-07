from estrutura.classesArquivos import *
from datetime import date

class Cadastro:
    def cadastrarLivro(self, arquivos: any, biblioteca: any) -> None:
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
        
        print('Livro cadastrado com sucesso.')
        return arquivos, biblioteca
        
    def removerCadastro(self, arquivos: any, biblioteca: any, alugados: any):
        codigoLivro = int(input('Qual o código do livro? '))
        indiceLivro, existeciaCodigo = self.__verificaExistenciaLivro(codigoLivro)
        
        if existeciaCodigo:
            removerAlugado = self.__buscarAlugado(biblioteca[indiceLivro].getCodigo())
            if removerAlugado != '':
                alugados.remove(removerAlugado)
                arquivos.atualizarAlugados(alugados)
            
            biblioteca.pop(indiceLivro)
            arquivos.atualizarBiblioteca(biblioteca)
                
            print('Livro removido com sucesso.')
        else:
            print('Não existe este livro nos cadastros.')
            
        return arquivos, biblioteca, alugados