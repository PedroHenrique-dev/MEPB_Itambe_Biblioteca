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
    
    def appPesquisarLivro(self, pesquisa, tipoPesquisa, biblioteca: any):
        if tipoPesquisa == 'codigo':
            pesquisa = int(pesquisa)
        
        if pesquisa == 'Disponível':
            pesquisa = True
        elif pesquisa == 'Indisponível':
            pesquisa = False

        livrosBuscados = self.__pesquisarLivroPorInfo(pesquisa, tipoPesquisa, biblioteca)

        informacoes = '    *** Livros ***\n'

        if livrosBuscados:
            for livro in livrosBuscados:
                informacoes += livro.getInfo()
        return informacoes
    
    def pesquisarLivro(self, biblioteca: any):
        while True:
            system('clear')
            escolha = self.__menuPesquisaLivro()
            
            livrosBuscados = []
            try:
                match escolha:
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
            
            print('======================================================')
            if livrosBuscados:
                print('\n    *** Livros ***')
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
            
    @staticmethod
    def __pesquisarLivroPorInfo(infoBusca: any, tipoBusca: str, biblioteca: any):
        informacoes = []
        match tipoBusca:
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
3. Data de aluguel  |    4. Data de entrega
5. Nome da pessoa   |    0. Sair
              ''')
        try:
            escolhaOpcao = int(input('Digite a opção da ação desejada: '))
            
            if escolhaOpcao < 0 or escolhaOpcao > 5:
                raise ErroSoftware('Opção inválida!')
            
            return escolhaOpcao
        except Exception as erro:
            self.erro(erro)
    
    def appPesquisarAluguel(self, pesquisa, tipoPesquisa, alugados: any):
        if tipoPesquisa == 'codigoLivro':
            pesquisa = int(pesquisa)

        alugueisBuscados = self.__pesquisarAluguelPorInfo(pesquisa, tipoPesquisa, alugados)

        informacoes = '    *** Alugueis ***\n'

        if alugueisBuscados:
            for aluguel in alugueisBuscados:
                informacoes += aluguel.getInfo()
        return informacoes
    
    def pesquisarAluguel(self, alugados: any):
        while True:
            system('clear')
            escolha = self.__menuPesquisaAluguel()
            
            try:
                alugueisBuscados = []
                match escolha:
                    case 1:
                        codigoLivro = int(input('Qual o código do livro? '))
                        alugueisBuscados = self.__pesquisarAluguelPorInfo(codigoLivro, 'codigoLivro', alugados)
                    case 2:
                        nomeLivro = self.inserirNome('Qual o nome do livro? ')
                        alugueisBuscados = self.__pesquisarAluguelPorInfo(nomeLivro, 'nomeLivro', alugados)
                    case 3:
                        dataAluguel = self.inserirNome('Qual a data do aluguel? ')
                        alugueisBuscados = self.__pesquisarAluguelPorInfo(dataAluguel, 'dataAluguel', alugados)
                    case 4:
                        dataEntega = self.inserirNome('Qual a data de devolução? ')
                        alugueisBuscados = self.__pesquisarAluguelPorInfo(dataEntega, 'dataEntega', alugados)
                    case 5:
                        nomePessoa = self.inserirNome('Qual o nome da pessoa? ')
                        alugueisBuscados = self.__pesquisarAluguelPorInfo(nomePessoa, 'nomePessoa', alugados)
                    case 0:
                        break
            except Exception as erro:
                self.erro(erro)
                return
            
            print('======================================================')
            if alugueisBuscados:
                print('\n    *** Alugueis ***')
                total = len(alugueisBuscados)
                
                j = 0
                for i in range(total):
                    alugueisBuscados[i].info()
                    j += 1
                    
                    if j == 5:
                        input(f"\nAperte 'Enter' para continuar. ({i+1}/{total})")
                        j = 0
            else:
                print('\nNão há livro alugado com esta informação.')
                
            input("\nAperte 'Enter' para continuar.")
            
    @staticmethod
    def __pesquisarAluguelPorInfo(infoBusca, tipoBusca: str, alugados: any):
        informacoes = []
        match tipoBusca:
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
            case 'dataEntrega':
                for aluguel in alugados:
                    if aluguel.getDataEntega() == infoBusca:
                        informacoes.append(aluguel)
        return informacoes