import json
from sys import platform


class Configuracao:
    def __init__(self) -> None:
        self.nome_banco = str
        self.conexao = str
        self.colecoes = str

        self.info = str
        self.imagens = str
        self.biblioteca = str

        self.ler_config()
        
    def ler_config(self):
        nome_arquivo = './config.json'
        
        with open(nome_arquivo) as f:
            json_arquivo = json.load(f)
            
        with open(nome_arquivo,'r'):
            diretorios = json_arquivo['diretorios']
            diretorios_arquivos = diretorios['localArquivos_windows'] if platform == 'win32' else diretorios['localArquivos_linux']
            
            self.biblioteca = diretorios_arquivos + diretorios['biblioteca']
            self.imagens = diretorios_arquivos + diretorios['imagens']
            self.info = diretorios_arquivos + diretorios['info']
            
            self.conexao = json_arquivo['banco_mongodb']['string_connection']
            self.nome_banco = json_arquivo['banco_mongodb']['string_bank']
            self.colecoes = {}
            for colecao in json_arquivo['banco_mongodb']['collections']:
                self.colecoes[colecao] = colecao
