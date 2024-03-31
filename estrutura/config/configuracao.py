import json
from sys import platform


class Configuracao():
    def __init__(self) -> None:
        self.biblioteca = str
        self.imagens = str
        self.info = str
        
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
            
            if platform == 'win32':
                self.biblioteca.replace('/', '\\')
                self.imagens.replace('/', '\\')
                self.info.replace('/', '\\')