import json


class Escritor:    
    def gerarArquivo(self, informacoesBiblioteca, nomeArquivo: str):
        nome = nomeArquivo[-15:-5]
        if nome == 'biblioteca':
            nome = "livros"
        else:
            nome = "alugados"
            
        informacoesArquivo = {
            "igreja": "Missao Evangelica Pentecostal do Brasil - Itambe",
            nome: informacoesBiblioteca
        }
        
        self.__json_nLinhas(informacoesArquivo, nomeArquivo)
            
    @staticmethod
    def __json_nLinhas(texto, nomeArquivo: str):
        with open(nomeArquivo, 'w') as arquivo: 
            arquivo.write(json.dumps(texto, indent = 4))
    
    @staticmethod
    def __json_1Linha(texto, nomeArquivo: str):
        with open(nomeArquivo, 'w') as arquivo: 
            json.dump(texto, arquivo)
