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
        nome_arquivo = './config/config.json'

        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            json_arquivo = json.load(arquivo)

            diretorios = json_arquivo['diretorios_windows'] if platform == 'win32' else json_arquivo['diretorios_linux']
            diretorios_arquivos = diretorios['local_arquivos']

            self.imagens = diretorios_arquivos + diretorios['imagens']
            self.info = diretorios_arquivos + diretorios['info']

            self.conexao = str(json_arquivo['banco_mongodb']['string_connection'])
            self.nome_banco = str(json_arquivo['banco_mongodb']['string_bank'])
