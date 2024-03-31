class Livro:
    def __init__(self, codigo: int, nome: str, autor: str, editora: str, paginas: int, genero: str, preco: float,
                 disponivel: bool, dataCadastro: str) -> None:
        self.__codigo = codigo
        self.__nome = nome
        self.__autor = autor
        self.__editora = editora
        self.__paginas = paginas
        self.__genero = genero
        self.__preco = preco
        self.__disponivel = disponivel
        self.__dataCadastro = dataCadastro

    def info(self) -> None:
        disponibilidade = 'Disponível' if self.__disponivel else 'Indisponível'

        print(f'''______________________________________________________
    * Livro {self.__codigo} *
Nome: {self.__nome}
Autor: {self.__autor}
Editora: {self.__editora}
Páginas: {self.__paginas}
Gênero: {self.__genero}
Disponibilidade para alugar: {disponibilidade}
Data de cadastro: {self.__dataCadastro}
______________________________________________________ ''')

    def getInfo(self):
        disponibilidade = 'Disponível' if self.__disponivel else 'Indisponível'

        informacoes = f'''_________________________________________________
        
    * Livro {self.__codigo} *
Nome: {self.__nome}
Autor: {self.__autor}
Editora: {self.__editora}
Páginas: {self.__paginas}
Gênero: {self.__genero}
Disponibilidade para alugar: {disponibilidade}
Data de cadastro: {self.__dataCadastro}
'''
        return informacoes

    def getCodigo(self) -> int:
        return self.__codigo

    def getNome(self) -> str:
        return self.__nome

    def getAutor(self) -> str:
        return self.__autor

    def getEditora(self) -> str:
        return self.__editora

    def getPaginas(self) -> int:
        return self.__paginas

    def getGenero(self) -> str:
        return self.__genero

    def getPreco(self) -> float:
        return self.__preco

    def getDisponivel(self) -> bool:
        return self.__disponivel

    def validarAluguel(self):
        if self.__disponivel:
            self.__disponivel = False
            return True
        else:
            return False

    def validarDevolucao(self):
        if not self.__disponivel:
            self.__disponivel = True
            return True
        else:
            return False

    def getDataCadastro(self) -> str:
        return self.__dataCadastro
