class AcaoPesquisar:   
    def __menuPesquisaLivro(self):
        print('''
======================================================
================ Menu Pesquisa: Livro ================
======================================================
1. Código   |    2. Nome      |    3. Autor
4. Editora  |    5. Gênero    |    6. Disponibilidade
0. Sair
              ''')
        return int(input('Digite a opção da ação desejada: '))
    
    def pesquisarLivro(self, biblioteca: any):
        while True:
            escolha = self.__menuPesquisaLivro()
            
            livrosBuscados = []
            match(escolha):
                case 1:
                    codigoLivro = int(input('Qual o código do livro? '))
                    livrosBuscados = self.__pesquisarLivroPorInfo(codigoLivro, 'codigo', biblioteca)
                case 2:
                    nomeLivro = str(input('Qual o nome do livro? '))
                    livrosBuscados = self.__pesquisarLivroPorInfo(nomeLivro, 'nome', biblioteca)
                case 3:
                    autorLivro = str(input('Qual o nome do autor? '))
                    livrosBuscados = self.__pesquisarLivroPorInfo(autorLivro, 'autor', biblioteca)
                case 4:
                    editoraLivro = str(input('Qual o nome da editora? '))
                    livrosBuscados = self.__pesquisarLivroPorInfo(editoraLivro, 'editora', biblioteca)
                case 5:
                    generoLivro = str(input('Qual o gênero do livro? '))
                    livrosBuscados = self.__pesquisarLivroPorInfo(generoLivro, 'genero', biblioteca)
                case 6:
                    disponibilidadeLivro = str(input('Qual a disponibilidade do livro? (Disponível | Indisponível): '))
                    if disponibilidadeLivro == 'Disponível':
                        livrosBuscados = self.__pesquisarLivroPorInfo(True, 'disponibilidade', biblioteca)
                    elif disponibilidadeLivro == 'Indisponível':
                        livrosBuscados = self.__pesquisarLivroPorInfo(False, 'disponibilidade', biblioteca)
                    else:
                        print('\nVocê não digitou corretamente o status de disponibilidade do livro.')
                case 0:
                    break
                    
            if livrosBuscados != []:
                total = len(livrosBuscados)
                for i in range(total):
                    livrosBuscados[i].info()
                    input(f"\nAperte 'Enter' para continuar. ({i+1}/{total})")
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
        return int(input('Digite a opção da ação desejada: '))
    
    def pesquisarAluguel(self, alugados: any):
        while True:
            escolha = self.__menuPesquisaAluguel()
            
            alugueiBuscados = []
            match(escolha):
                case 1:
                    codigoLivro = int(input('Qual o código do livro? '))
                    alugueiBuscados = self.__pesquisarAluguelPorInfo(codigoLivro, 'codigoLivro', alugados)
                case 2:
                    nomeLivro = str(input('Qual o nome do livro? '))
                    alugueiBuscados = self.__pesquisarAluguelPorInfo(nomeLivro, 'nomeLivro', alugados)
                case 3:
                    nomePessoa = str(input('Qual o nome da pessoa? '))
                    alugueiBuscados = self.__pesquisarAluguelPorInfo(nomePessoa, 'nomePessoa', alugados)
                case 4:
                    dataAluguel = str(input('Qual a data do aluguel? '))
                    alugueiBuscados = self.__pesquisarAluguelPorInfo(dataAluguel, 'dataAluguel', alugados)
                case 5:
                    dataEntega = str(input('Qual a data de devolução? '))
                    alugueiBuscados = self.__pesquisarAluguelPorInfo(dataEntega, 'dataEntega', alugados)
                case 0:
                    break
                    
            if alugueiBuscados != []:
                total = len(alugueiBuscados)
                for i in range(total):
                    alugueiBuscados[i].info()
                    input(f"\nAperte 'Enter' para continuar. ({i+1}/{total})")
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