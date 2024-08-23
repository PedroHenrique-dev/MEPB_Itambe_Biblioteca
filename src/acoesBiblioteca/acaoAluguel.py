from src.classesArquivos import *
from src.acoesBiblioteca.funcoesAuxiliares import FuncoesAuxiliares

from src.tratamento import *


class AcaoAluguel(FuncoesAuxiliares, TratamentoErro):
    def appAlugar(self, informacoesAluguel, arquivos: any, biblioteca: any, alugados: any):
        codigoLivro, nomePessoa = informacoesAluguel

        indiceLivro, existeciaCodigo = self.verificaExistenciaLivro(codigoLivro, biblioteca)

        if existeciaCodigo:
            podeAlugar = biblioteca[indiceLivro].validarAluguel()
            
            if podeAlugar:
                if len(nomePessoa) > 3:
                    codigo = biblioteca[indiceLivro].getCodigo()
                    nomeLivro = biblioteca[indiceLivro].getNome()
                    
                    dataAluguel = self.gerarDataAtual()
                    dataEntega = self.gerarDataProximoMes()
                    
                    novoAluguel = Aluguel(nomePessoa, codigo, nomeLivro, dataAluguel, dataEntega)
                    alugados.append(novoAluguel)
                    
                    arquivos.atualizarAlugados(alugados)
                    arquivos.atualizarBiblioteca(biblioteca)
                else:
                    raise ErroSoftware('Nome inválido!')
            else:
                raise ErroSoftware('Livro indiponível!')
        else:
            raise ErroSoftware('Livro inexistente!')

        return arquivos, biblioteca, alugados

    def alugar(self, arquivos: any, biblioteca: any, alugados: any):
        self.__tituloAlugar()
        
        try:
            codigoLivro = int(input('Qual o código do livro? '))
        except Exception as erro:
            self.erro(erro)
            return arquivos, biblioteca, alugados
        
        indiceLivro, existeciaCodigo = self.verificaExistenciaLivro(codigoLivro, biblioteca)
        
        if existeciaCodigo:
            podeAlugar = biblioteca[indiceLivro].validarAluguel()
            
            if podeAlugar:
                try:
                    nomePessoa = self.inserirNome('\nDigite o nome completo da pessoa que está alugando o livro: ')
                except Exception as erro:
                    self.erro(erro)
                    return arquivos, biblioteca, alugados 
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
    
    def appDevolucao(self, codigoLivro, arquivos: any, biblioteca: any, alugados: any):
        indiceLivro, existeciaCodigo = self.verificaExistenciaLivro(codigoLivro, biblioteca)

        if existeciaCodigo:
            podeDevolder = biblioteca[indiceLivro].validarDevolucao()
            
            if podeDevolder:
                codigoLivro = biblioteca[indiceLivro].getCodigo()
                devolverAlugado = self.buscarAlugado(codigoLivro, alugados)
                
                if devolverAlugado != '':
                    alugados.remove(devolverAlugado)
                    arquivos.atualizarAlugados(alugados)
                    arquivos.atualizarBiblioteca(biblioteca)
        else:
            raise ErroSoftware('Livro inexistente!')
        
        return arquivos, biblioteca, alugados
                
    def devolucao(self, arquivos: any, biblioteca: any, alugados: any):
        self.__tituloDevolucao()
        
        try:
            codigoLivro = int(input('Qual o código do livro? '))
        except Exception as erro:
            self.erro(erro)
            return arquivos, biblioteca, alugados
        
        indiceLivro, existeciaCodigo = self.verificaExistenciaLivro(codigoLivro, biblioteca)
        
        if existeciaCodigo:
            podeDevolder = biblioteca[indiceLivro].validarDevolucao()
            
            if podeDevolder:
                codigoLivro = biblioteca[indiceLivro].getCodigo()
                devolverAlugado = self.buscarAlugado(codigoLivro, alugados)
                
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
    
    @staticmethod
    def __tituloAlugar():
        print('''
======================================================
======================= Alugar =======================
======================================================
''')
    
    @staticmethod
    def __tituloDevolucao():
        print('''
======================================================
====================== Devolver ======================
======================================================
''')