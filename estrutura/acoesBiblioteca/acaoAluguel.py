from estrutura.classesArquivos import *
from estrutura.acoesBiblioteca.funcoesAuxiliares import FuncoesAuxiliares
from datetime import date

class AcaoAluguel(FuncoesAuxiliares):
    def alugar(self, arquivos: any, biblioteca: any, alugados: any):
        self.__tituloAlugar()
        codigoLivro = int(input('Qual o código do livro? '))
        indiceLivro, existeciaCodigo = self.verificaExistenciaLivro(codigoLivro, biblioteca)
        
        if existeciaCodigo:
            podeAlugar = biblioteca[indiceLivro].validarAluguel()
            
            if podeAlugar:
                nomePessoa = str(input('\nDigite o nome completo da pessoa que está alugando o livro: '))
                if len(nomePessoa) > 3:
                    codigo = biblioteca[indiceLivro].getCodigo()
                    nomeLivro = biblioteca[indiceLivro].getNome()
                    
                    dataAluguel = self.gerarDataAtual()
                    dataEntega = self.gerarDataProximoMes()
                    
                    novoAluguel = Aluguel(nomePessoa, codigo, nomeLivro, dataAluguel, dataEntega)
                    alugados.append(novoAluguel)
                    
                    arquivos.atualizarAlugados(alugados)
                    arquivos.atualizarBiblioteca(biblioteca)
                
                    print('\nLivro alugado com sucesso.')
                else:
                    print('\nNome inválido.')
            else:
                print('\nO livro já está alugado.')
        else:
            print('\nNão existe este livro nos cadastros.')
            
        return arquivos, biblioteca, alugados
                
    def devolucao(self, arquivos: any, biblioteca: any, alugados: any):
        self.__tituloDevolucao()
        codigoLivro = int(input('Qual o código do livro? '))
        indiceLivro, existeciaCodigo = self.__verificaExistenciaLivro(codigoLivro, biblioteca)
        
        if existeciaCodigo:
            podeDevolder = biblioteca[indiceLivro].validarDevolucao()
            
            if podeDevolder:
                codigoLivro = biblioteca[indiceLivro].getCodigo()
                devolverAlugado = self.__buscarAlugado(codigoLivro, alugados)
                
                if devolverAlugado != '':
                    alugados.remove(devolverAlugado)
                    arquivos.atualizarAlugados(alugados)
                    arquivos.atualizarBiblioteca(biblioteca)
                    
                    print('\nLivro devolvido com sucesso.')
                else:
                    print('\nO livro não foi alugado.')
            else:
                print('\nO livro não foi alugado.')
        else:
            print('\nNão existe este livro nos cadastros.')
            
        return arquivos, biblioteca, alugados
    
    def __tituloAlugar(self):
        print('''
======================================================
======================= Alugar =======================
======================================================
''')
    
    def __tituloDevolucao(self):
        print('''
======================================================
====================== Devolver ======================
======================================================
''')