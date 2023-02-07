import json
from estrutura.classesArquivos import *

class Leitor:
    def lerJSON(self, nomeArquivo: str, lerbiblioteca: bool):
        with open(nomeArquivo) as f:
            jsonArquivo = json.load(f)
            
        with open(nomeArquivo,'r') as arquivo:
            return self.__leitorJson(jsonArquivo, lerbiblioteca)
    
    def __leitorJson(self, jsonArquivo, lerbiblioteca: bool):
        informacoes = []
        if lerbiblioteca:
            for info in jsonArquivo['livros']:
                informacoes.append(self.__lerJsonInfoLivro(info))
        else:
            for info in jsonArquivo['alugados']:
                informacoes.append(self.__lerJsonInfoAluguel(info))
        return informacoes
    
    def __lerJsonInfoAluguel(self, dados):
        nomePessoa = str(dados['nomePessoa'])
        codigo = int(dados['codigo'])
        nomeLivro = str(dados['nomeLivro'])
        dataAluguel = str(dados['dataAluguel'])
        dataEntega = str(dados['dataEntega'])
        
        return Aluguel(nomePessoa, codigo, nomeLivro, dataAluguel, dataEntega)
                
    def __lerJsonInfoLivro(self, dados):
        codigo = int(dados['codigo'])
        nome = str(dados['nome'])
        autor = str(dados['autor'])
        editora = str(dados['editora'])
        paginas = int(dados['paginas'])
        genero = str(dados['genero'])
        preco = float(dados['preco'])
        disponivel = bool(dados['disponivel'])
        dataCadastro = str(dados['dataCadastro'])
        
        return Livro(codigo, nome, autor, editora, paginas, genero, preco, disponivel, dataCadastro)

    def __informacaoLivro(self, livro):
        infoLivro = {
            "codigo": livro.getCodigo(),
            "nome": livro.getNome(),
            "autor": livro.getAutor(),
            "editora": livro.getEditora(),
            "paginas": livro.getPaginas(),
            "genero": livro.getGenero(),
            "preco": livro.getPreco(),
            "disponivel": livro.getDisponivel(),
            "dataCadastro": livro.getDataCadastro()
        }
        return infoLivro
    
    def __informacaoAluguel(self, aluguel):
        infoAluguel = {
            "nomePessoa": aluguel.getNomePessoa(),
            "codigo": aluguel.getCodigo(),
            "nomeLivro": aluguel.getNomeLivro(),
            "dataAluguel": aluguel.getDataAluguel(),
            "dataEntega": aluguel.getDataEntega()
        }
        return infoAluguel
    
    def informacoesLivros(self, livros):
        infoLivros = []
        for livro in livros:
            infoLivros.append(self.__informacaoLivro(livro))
        return infoLivros
    
    def informacoesAlugados(self, alugados):
        infoAlugados = []
        for aluguel in alugados:
            infoAlugados.append(self.__informacaoAluguel(aluguel))
        return infoAlugados