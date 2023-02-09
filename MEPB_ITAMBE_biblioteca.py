from estrutura import Biblioteca

class MEPBbiblioteca():
    def __init__(self) -> None:
        self.__nomeIgreja = 'M.E.P.B. Itambé'
        self.__mepb = Biblioteca()

    def __menu(self):
        print(f'''
    ******************************************************
    ************  Biblioteca {self.__nomeIgreja}  ************
    ******************************************************
    1. Cadastrar            |       2. Alugar
    3. Remover              |       4. Devolver
    5. Pesquisar livro      |       6. Pesquisar aluguel
    7. Todos os livros      |       8. Todos os alugueis
    0. Sair
            ''')
        return int(input('Digite a opção da ação desejada: '))
    
    def iniciar(self):
        separador = '______________________________________________________'
        
        while True:
            escolha = self.__menu()
            
            print(separador)
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
                case 0:
                    break
            
            print(separador)
            input("\nAperte 'Enter' para continuar.")
        print('******************************************************')
        
itambe = MEPBbiblioteca()
itambe.iniciar()