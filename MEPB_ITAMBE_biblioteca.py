from estrutura import Biblioteca

mepb = Biblioteca()

def menu():
    print('''
******************************************************
************  Biblioteca M.E.P.B. Itambé  ************
******************************************************
1. Cadastrar            |       2. Alugar
3. Remover              |       4. Devolver
5. Pesquisar livro      |       6. Pesquisar aluguel
0. Sair
          ''')
    return int(input('Digite a opção da ação desejada: '))

while True:
    escolha = menu()
    
    match(escolha):
        case 1:
            mepb.cadastrarLivroBiblioteca()
        case 2:
            mepb.alugarLivroBiblioteca()
        case 3:
            mepb.removerLivroBiblioteca()
        case 4:
            mepb.devolucaoLivroBiblioteca()
        case 5:
            mepb.pesquisarLivro()
        case 6:
            mepb.pesquisarAluguel()
        case 123:
            mepb.mostrarLivros()
        case 321:
            mepb.mostrarAlugados()
        case 0:
            break
            
    input("\nAperte 'Enter' para continuar.")

print('******************************************************')