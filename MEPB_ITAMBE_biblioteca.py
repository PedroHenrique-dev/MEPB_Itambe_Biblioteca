from os import system
from sys import platform
from estrutura import Biblioteca
from estrutura.tratamento import *
from estrutura.gerenciador import *

class MEPBbiblioteca(TratamentoErro, Validador):
    def __init__(self) -> None:
        self.__nomeIgreja = 'M.E.P.B. Itambé'
        self.__mepb = Biblioteca()

    def __menu(self):
        print(f'''
    **********************************************************
    **************  Biblioteca {self.__nomeIgreja}  **************
    **********************************************************
    1. Cadastrar            |       2. Alugar
    3. Remover              |       4. Devolver
    5. Pesquisar livro      |       6. Pesquisar aluguel
    7. Todos os livros      |       8. Todos os alugueis
    9. Gasto total          |       10. Quantidade de livros
    0. Sair
            ''')
        try:
            escolhaOpcao = int(input('Digite a opção da ação desejada: '))
            
            if escolhaOpcao < 0 or escolhaOpcao > 10:
                raise ErroSoftware('Opção inválida!')
            
            return escolhaOpcao
        except Exception as erro:
            self.erro(erro)
    
    def iniciar(self):
        separador = '======================================================'
        permissao = False
        
        while True:
            limpar()
            escolha = self.__menu()            
            if permissao == False and (escolha == 1 or escolha == 3 or escolha == 4 or escolha == 6 or escolha == 7 or escolha == 8):
                permissao = self.validarEntrada(str(input('Digite a senha: ')))
                if permissao == False:
                    continue
            
            limpar()
            match(escolha):
                case 1:
                    self.__mepb.cadastrarLivroBiblioteca()
                case 2:
                    self.__mepb.alugarLivroBiblioteca()
                case 3:
                    self.__mepb.removerLivroBiblioteca()
                case 4:
                    self.__mepb.devolucaoLivroBiblioteca()
                case 5:
                    self.__mepb.pesquisarLivroBiblioteca()
                case 6:
                    self.__mepb.pesquisarAluguelBiblioteca()
                case 7:
                    self.__mepb.mostrarLivrosBiblioteca()
                case 8:
                    self.__mepb.mostrarAlugadosBiblioteca()
                case 9:
                    self.__mepb.gastoTotalLivros()
                case 10:
                    self.__mepb.mostrarQuantidadeLivros()
                case 0:
                    break
                case None:
                    input("\nAperte 'Enter' para continuar.")
                    continue
            
            print(separador)
            input("\nAperte 'Enter' para continuar.")
        limpar()

def limpar():
    if platform == 'win32':
        system('cls')
    else:
        system('clear')

itambe = MEPBbiblioteca()
itambe.iniciar()
