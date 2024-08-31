from src.banco import TypeCollections, Banco
from src.tratamento import TratamentoErro


class AcaoPesquisar(TratamentoErro):
    def pesquisar_livro(self, banco: Banco, pesquisa: str, tipo_pesquisa: str, mensagem_vazio:str ) -> str:
        return self._pesquisar(
            banco=banco,
            type_collection=TypeCollections.LIVROS,
            pesquisa=pesquisa,
            tipo_pesquisa=tipo_pesquisa,
            mensagem_vazio=mensagem_vazio
        )

    def pesquisar_aluguel(self, banco: Banco, pesquisa: str, tipo_pesquisa: str, mensagem_vazio:str) -> str:
        return self._pesquisar(
            banco=banco,
            type_collection=TypeCollections.ALUGUEIS,
            pesquisa=pesquisa,
            tipo_pesquisa=tipo_pesquisa,
            mensagem_vazio=mensagem_vazio
        )

    def _pesquisar(self, banco: Banco, type_collection:TypeCollections, pesquisa: str, tipo_pesquisa: str, mensagem_vazio: str):
        if pesquisa == 'Disponível':
            pesquisa = True
        elif pesquisa == 'Indisponível':
            pesquisa = False

        pesquisar_todos = pesquisa == '' and tipo_pesquisa == ''

        if isinstance(pesquisa, str) and tipo_pesquisa == 'codigo':
            tipo_pesquisa = '_id'
            pesquisa = int(pesquisa)

        filtro_documento = {}
        if not pesquisar_todos:
            filtro_documento = {tipo_pesquisa: pesquisa}

        existe_documento = banco.exists_document(
            type_collection=type_collection,
            data_type=filtro_documento
        )

        informacoes = ''
        if pesquisar_todos:
            match type_collection:
                case TypeCollections.LIVROS:
                    informacoes = self._app_titulo_todos_livros()
                case TypeCollections.ALUGUEIS:
                    informacoes = self._app_titulo_todos_alugueis()
        else:
            informacoes = '    *** Livros ***\n'

        if existe_documento:
            documentos = banco.find_document(type_collection=type_collection, data_type=filtro_documento)
            for documento in documentos:
                match type_collection:
                    case TypeCollections.LIVROS:
                        informacoes += self._exibir_info_livro(documento=documento)
                    case TypeCollections.ALUGUEIS:
                        informacoes += self._exibir_info_aluguel(documento=documento)
            return informacoes
        else:
            return mensagem_vazio

    @staticmethod
    def _exibir_info_livro(documento: dict) -> str:
        disponibilidade = 'Disponível' if documento['disponibilidade'] else 'Indisponível'
        return f'''__________________________________________________
    * Livro {documento['_id']} *
Nome: {documento['nome']}
Autor: {documento['autor']}
Editora: {documento['editora']}
Páginas: {documento['paginas']}
Gênero: {documento['genero']}
Disponibilidade para alugar: {disponibilidade}
Data de cadastro: {documento['data_cadastro']}
__________________________________________________ '''

    @staticmethod
    def _exibir_info_aluguel(documento: dict) -> str:
        return f'''__________________________________________________
    * Livro {documento['_id']} *
Nome da pessoa: {documento['nome_pessoa']}
Codigo: {documento['_id']}
Nome do livro: {documento['nome_livro']}
Data do aluguel: {documento['data_aluguel']}
Data da entrega: {documento['data_entrega']}
Multa: {documento['multa']}
__________________________________________________'''

    @staticmethod
    def _app_titulo_todos_livros() -> str:
        return '''
============================================
===============  Todos os Livros  ================
============================================
'''

    @staticmethod
    def _app_titulo_todos_alugueis() -> str:
        return '''
============================================
==============  Todos os Alugueis  ===============
============================================
'''