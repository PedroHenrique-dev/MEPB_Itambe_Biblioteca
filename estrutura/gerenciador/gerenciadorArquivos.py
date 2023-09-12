import os
from estrutura.gerenciador.acoesArquivos import *

class GerenciadorArquivos(Escritor, Leitor):
    def __init__(self) -> None:
        self.diretorio = 'C:/arquivosBiblioteca/'
        self.arquivoBilioteca = self.diretorio + 'biblioteca.json'
        self.arquivoAlugados = self.diretorio + 'alugados.json'
        
        existenciaArquivo = os.path.exists(self.arquivoBilioteca)
        if existenciaArquivo == False:
            self.gerarArquivo([], self.arquivoBilioteca)
        
        existenciaArquivo = os.path.exists(self.arquivoAlugados)
        if existenciaArquivo == False:
            self.gerarArquivo([], self.arquivoAlugados) 
        
    def lerArquivoJSON(self, lerBiblioteca: bool):
        if lerBiblioteca:
            return self.lerJSON(self.arquivoBilioteca, lerBiblioteca)
        else:
            return self.lerJSON(self.arquivoAlugados, lerBiblioteca)
    
    def atualizarBiblioteca(self, livros):
        infoLivros = self.informacoesLivros(livros)
        self.gerarArquivo(infoLivros, self.arquivoBilioteca)
    
    def atualizarAlugados(self, alugados):
        infoAlugados = self.informacoesAlugados(alugados)
        self.gerarArquivo(infoAlugados, self.arquivoAlugados)