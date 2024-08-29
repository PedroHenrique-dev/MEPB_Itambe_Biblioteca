import json
from sys import platform


class Configuracao:
    def __init__(self) -> None:
        self.info = None
        self.imagens = None

        self.conexao = None
        self.nome_banco = None

        self.ler_config()
        
    def ler_config(self):
        nome_arquivo = './config.json'

        with open(nome_arquivo, encoding='utf-8') as f:
            json_arquivo = json.load(f)
            
        with open(nome_arquivo,'r', encoding='utf-8'):
            diretorios = json_arquivo['diretorios']
            diretorios_arquivos = diretorios['localArquivos_windows'] if platform == 'win32' else diretorios['localArquivos_linux']
            
            self.imagens = diretorios_arquivos + diretorios['imagens']
            self.info = diretorios_arquivos + diretorios['info']
            
            self.conexao = str(json_arquivo['banco_mongodb']['string_connection'])
            self.nome_banco = str(json_arquivo['banco_mongodb']['string_bank'])
