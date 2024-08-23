import json
from sys import platform


class Configuracao():
    def __init__(self) -> None:        
        self.ler_config()
        
    def ler_config(self):
        nomeArquivo = './config.json'
        
        with open(nomeArquivo) as f:
            jsonArquivo = json.load(f)
            
        with open(nomeArquivo,'r') as arquivo:
            diretorios = jsonArquivo['diretorios']
            diretorios_arquivos = diretorios['localArquivos_windows'] if platform == 'win32' else diretorios['localArquivos_linux']
            
            self.biblioteca = diretorios_arquivos + diretorios['bibioteca']
            self.imagens = diretorios_arquivos + diretorios['imagens']
            self.info = diretorios_arquivos + diretorios['info']
            
            self.conexao = jsonArquivo['banco_mongodb']['string_connection']
            self.nome_banco = jsonArquivo['banco_mongodb']['string_bank']
            self.colecoes = {}
            for colacao in jsonArquivo['banco_mongodb']['collections']:
                self.colecoes[colacao] = colacao
