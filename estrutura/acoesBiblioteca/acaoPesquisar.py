from estrutura.tratamento import *
from os import system

class AcaoPesquisar(TratamentoErro):
    def __menuPesquisaLivro(self):
        print('''
======================================================
================ Menu Pesquisa: Livro ================
======================================================
1. Código   |    2. Nome      |    3. Autor
4. Editora  |    5. Gênero    |    6. Disponibilidade
0. Sair
              ''')
        try:
            escolhaOpcao = int(input('Digite a opção da ação desejada: '))
            
            if escolhaOpcao < 0 or escolhaOpcao > 6:
                raise ErroSoftware('Opção inválida!')
            
            return escolhaOpcao
        except Exception as erro:
            self.erro(erro)
    
    def pesquisarLivro(self, biblioteca: any):
        while True:
            system('clear')
            escolha = self.__menuPesquisaLivro()
            
            livrosBuscados = []
            try:
                match(escolha):
                    case 1:
                        codigoLivro = int(input('Qual o código do livro? '))
                        livrosBuscados = self.__pesquisarLivroPorInfo(codigoLivro, 'codigo', biblioteca)
                    case 2:
                        nomeLivro = self.inserirNome('Qual o nome do livro? ')
                        livrosBuscados = self.__pesquisarLivroPorInfo(nomeLivro, 'nome', biblioteca)
                    case 3:
                        autorLivro = self.inserirNome('Qual o nome do autor? ')
                        livrosBuscados = self.__pesquisarLivroPorInfo(autorLivro, 'autor', biblioteca)
                    case 4:
                        editoraLivro = self.inserirNome('Qual o nome da editora? ')
                        livrosBuscados = self.__pesquisarLivroPorInfo(editoraLivro, 'editora', biblioteca)
                    case 5:
                        generoLivro = self.inserirNome('Qual o gênero do livro? ')
                        livrosBuscados = self.__pesquisarLivroPorInfo(generoLivro, 'genero', biblioteca)
                    case 6:
                        disponibilidadeLivro = self.inserirNome('Qual a disponibilidade do livro? (Disponível | Indisponível): ')
                        
                        if disponibilidadeLivro == 'Disponível':
                            livrosBuscados = self.__pesquisarLivroPorInfo(True, 'disponibilidade', biblioteca)
                        elif disponibilidadeLivro == 'Indisponível':
                            livrosBuscados = self.__pesquisarLivroPorInfo(False, 'disponibilidade', biblioteca)
                        else:
                            raise ErroSoftware('Status incompatível.')
                    case 0:
                        break
            except Exception as erro:
                self.erro(erro)
                return
            
            if livrosBuscados != []:
                total = len(livrosBuscados)
                
                j = 0
                for i in range(total):
                    livrosBuscados[i].info()
                    j += 1
                    
                    if j == 5:
                        input(f"\nAperte 'Enter' para continuar. ({i+1}/{total})")
                        j = 0
            else:
                print('\nNão há livro com esta informação.')
                
            input("\nAperte 'Enter' para continuar.")
            
    def __pesquisarLivroPorInfo(self, infoBusca: any, tipoBusca: str, biblioteca: any):
        informacoes = []
        match(tipoBusca):
            case 'codigo':
                for livro in biblioteca:
                    if livro.getCodigo() == infoBusca:
                        informacoes.append(livro)
            case 'nome':
                for livro in biblioteca:
                    if livro.getNome() == infoBusca:
                        informacoes.append(livro)
            case 'autor':
                for livro in biblioteca:
                    if livro.getAutor() == infoBusca:
                        informacoes.append(livro)
            case 'editora':
                for livro in biblioteca:
                    if livro.getEditora() == infoBusca:
                        informacoes.append(livro)
            case 'genero':
                for livro in biblioteca:
                    if livro.getGenero() == infoBusca:
                        informacoes.append(livro)
            case 'disponibilidade':
                for livro in biblioteca:
                    if livro.getDisponivel() == infoBusca:
                        informacoes.append(livro)
        return informacoes
    
    def __menuPesquisaAluguel(self):
        print('''
======================================================
=============== Menu Pesquisa: Aluguel ===============
======================================================
1. Código do livro  |    2. Nome do livro
3. Nome da pessoa   |
4. Data de aluguel  |    5. Data de entrega
0. Sair
              ''')
        try:
            escolhaOpcao = int(input('Digite a opção da ação desejada: '))
            
            if escolhaOpcao < 0 or escolhaOpcao > 5:
                raise ErroSoftware('Opção inválida!')
            
            return escolhaOpcao
        except Exception as erro:
            self.erro(erro)
    
    def pesquisarAluguel(self, alugados: any):
        while True:
            system('clear')
            escolha = self.__menuPesquisaAluguel()
            
            try:
                alugueiBuscados = []
                match(escolha):
                    case 1:
                        codigoLivro = int(input('Qual o código do livro? '))
                        alugueiBuscados = self.__pesquisarAluguelPorInfo(codigoLivro, 'codigoLivro', alugados)
                    case 2:
                        nomeLivro = self.inserirNome('Qual o nome do livro? ')
                        alugueiBuscados = self.__pesquisarAluguelPorInfo(nomeLivro, 'nomeLivro', alugados)
                    case 3:
                        nomePessoa = self.inserirNome('Qual o nome da pessoa? ')
                        alugueiBuscados = self.__pesquisarAluguelPorInfo(nomePessoa, 'nomePessoa', alugados)
                    case 4:
                        dataAluguel = self.inserirNome('Qual a data do aluguel? ')
                        alugueiBuscados = self.__pesquisarAluguelPorInfo(dataAluguel, 'dataAluguel', alugados)
                    case 5:
                        dataEntega = self.inserirNome('Qual a data de devolução? ')
                        alugueiBuscados = self.__pesquisarAluguelPorInfo(dataEntega, 'dataEntega', alugados)
                    case 0:
                        break
            except Exception as erro:
                self.erro(erro)
                return
            
            if alugueiBuscados != []:
                total = len(alugueiBuscados)
                
                j = 0
                for i in range(total):
                    alugueiBuscados[i].info()
                    j += 1
                    
                    if j == 5:
                        input(f"\nAperte 'Enter' para continuar. ({i+1}/{total})")
                        j = 0
            else:
                print('\nNão há livro alugado com esta informação.')
                
            input("\nAperte 'Enter' para continuar.")
            
    def __pesquisarAluguelPorInfo(self, infoBusca, tipoBusca: str, alugados: any):
        informacoes = []
        match(tipoBusca):
            case 'codigoLivro':
                for aluguel in alugados:
                    if aluguel.getCodigo() == infoBusca:
                        informacoes.append(aluguel)
            case 'nomeLivro':
                for aluguel in alugados:
                    if aluguel.getNomeLivro() == infoBusca:
                        informacoes.append(aluguel)
            case 'nomePessoa':
                for aluguel in alugados:
                    if aluguel.getNomePessoa() == infoBusca:
                        informacoes.append(aluguel)
            case 'dataAluguel':
                for aluguel in alugados:
                    if aluguel.getDataAluguel() == infoBusca:
                        informacoes.append(aluguel)
            case 'dataEntega':
                for aluguel in alugados:
                    if aluguel.getDataEntega() == infoBusca:
                        informacoes.append(aluguel)
        return informacoes