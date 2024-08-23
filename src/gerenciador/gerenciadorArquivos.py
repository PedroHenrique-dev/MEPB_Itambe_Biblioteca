import os
from src.gerenciador.acoesArquivos import *
from src.config import *


class GerenciadorArquivos(Escritor, Leitor):
    def __init__(self) -> None:
        configuracao = Configuracao()
        
        diretorio = configuracao.biblioteca
        self.arquivoBilioteca = diretorio + 'biblioteca.json'
        self.arquivoAlugados = diretorio + 'alugados.json'
        
        self.conexao = configuracao.conexao
        self.nome_banco = configuracao.nome_banco
        self.colecoes = configuracao.colecoes
        
        existenciaArquivo = os.path.exists(self.arquivoBilioteca)
        if not existenciaArquivo:
            self.gerarArquivo([], self.arquivoBilioteca)
        
        existenciaArquivo = os.path.exists(self.arquivoAlugados)
        if not existenciaArquivo:
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