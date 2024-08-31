from .acoes import AcaoCadastro, AcaoAluguel, AcaoPesquisar
from .banco import Banco, TypeCollections
from .configuracao import Configuracao


class Biblioteca():
    def __init__(self) -> None:
        configuracao = Configuracao()
        self._banco = Banco(string_connection=configuracao.conexao, string_bank=configuracao.nome_banco)

        self._cadastro = AcaoCadastro(banco=self._banco)
        self._aluguel = AcaoAluguel(banco=self._banco)
        self._pesquisa = AcaoPesquisar(banco=self._banco)

    def app_cadastrar_livro_biblioteca(self, informacoes_livro: list) -> None:
        self._cadastro.cadastrar_livro(informacoes_livro=informacoes_livro)

    def app_remover_livro_biblioteca(self, codigo_livro: int) -> None:
        self._cadastro.remover_livro(codigo_livro=codigo_livro)

    def app_alugar_livro_biblioteca(self, informacoes_aluguel: list) -> None:
        self._aluguel.alugar(informacoes_aluguel=informacoes_aluguel)

    def app_devolucao_livro_biblioteca(self, codigo_livro: int) -> None:
        self._aluguel.devolucao(codigo_livro=codigo_livro)

    def app_pesquisar_livro_biblioteca(self, pesquisa: str, tipo_pesquisa: str) -> str:
        return self._pesquisa.pesquisar_livro(
            pesquisa=pesquisa,
            tipo_pesquisa=tipo_pesquisa,
            mensagem_vazio='Este livro não está cadastrado!'
        )

    def app_pesquisar_aluguel_biblioteca(self, pesquisa: str, tipo_pesquisa: str) -> str:
        return self._pesquisa.pesquisar_aluguel(
            pesquisa=pesquisa,
            tipo_pesquisa=tipo_pesquisa,
            mensagem_vazio='Este livro não está alugado!'
        )

    def app_mostrar_livros_biblioteca(self) -> str:
        return self._pesquisa.pesquisar_livro(
            pesquisa='',
            tipo_pesquisa='',
            mensagem_vazio='Não existe livro cadastrado!'
        )

    def app_mostrar_alugados_biblioteca(self) -> str:
        return self._pesquisa.pesquisar_aluguel(
            pesquisa='',
            tipo_pesquisa='',
            mensagem_vazio='Não existe livro alugado!'
        )

    def app_gasto_total_livros(self) -> str:
        gasto = 0
        livros = self._banco.find_document(type_collection=TypeCollections.LIVROS, data_type={})
        for livro in livros:
            gasto += livro['preco']
        gasto_total = f'{gasto:5.2f}'
        return f'R$ {gasto_total.replace(".", ",")}'
