from datetime import date

from src.banco import Banco, TypeCollections
from src.tratamento import TratamentoErro, ErroSoftware


class AcaoCadastro(TratamentoErro):
    data_atual = date.today().strftime('%d/%m/%Y')

    @staticmethod
    def _novo_codigo(banco: Banco) -> int:
        codigo = 1001
        ultimo_documento = banco.get_last_document(TypeCollections.LIVROS)

        if ultimo_documento != {}:
            codigo = ultimo_documento['_id'] + 1
        return codigo

    def _criar_documento_livro(self, informacoes_livro: list, codigo: int) -> dict:
        nome, autor, editora, paginas, genero, preco = informacoes_livro

        if paginas < 6:
            raise ErroSoftware('Quantidade insuficiente!')

        for info in informacoes_livro:
            self.teste_nome_valido(nome=info)

        documento = {
            "_id": codigo,
            "nome": nome,
            "autor": autor,
            "editora": editora,
            "paginas": paginas,
            "genero": genero,
            "preco": preco,
            "disponibilidade": True,
            "data_cadastro": AcaoCadastro.data_atual
        }
        return documento

    def cadastrar_livro(self, banco: Banco, informacoes_livro: list) -> None:
        codigo = self._novo_codigo(banco=banco)
        livro = self._criar_documento_livro(informacoes_livro=informacoes_livro, codigo=codigo)
        banco.add_document(type_collection=TypeCollections.LIVROS, document=livro)

    @staticmethod
    def remover_livro(banco: Banco, codigo_livro: int) -> None:
        existe_documento = banco.exists_document(
            type_collection=TypeCollections.LIVROS,
            data_type={"_id": codigo_livro}
        )
        if existe_documento:
            banco.delete_document(
                type_collection=TypeCollections.LIVROS,
                code_document_delete=codigo_livro
            )
        else:
            raise ErroSoftware('Livro inexistente!')
