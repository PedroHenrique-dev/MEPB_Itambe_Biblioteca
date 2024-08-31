from datetime import date

from src.banco import Banco, TypeCollections
from src.tratamento import TratamentoErro, ErroSoftware


class AcaoAluguel(TratamentoErro):
    data_atual = date.today().strftime('%d/%m/%Y')

    def __init__(self, banco: Banco):
        self._banco = banco

    @staticmethod
    def _gerar_data_proximo_mes():
        ano = date.today().year
        mes = date.today().month + 1
        dia = date.today().day

        if mes == 2 and dia > 28:
            dia = 3
        elif dia == 31 and (mes == 4 or mes == 6 or mes == 9 or mes == 11):
            dia = 1

        nova_data = date(ano, mes, dia)
        return nova_data.strftime('%d/%m/%Y')

    def alugar(self, informacoes_aluguel: list) -> None:
        codigo_livro, nome_pessoa = informacoes_aluguel

        filtro_documento = {'_id': codigo_livro}
        existe_documento = self._banco.exists_document(
            type_collection=TypeCollections.LIVROS,
            data_type=filtro_documento
        )

        if existe_documento:
            documentos = self._banco.find_document(type_collection=TypeCollections.LIVROS, data_type={"_id": codigo_livro})
            documento = documentos[0]
            disponivel = documento['disponibilidade']

            if disponivel:
                try:
                    data_entrega = self._gerar_data_proximo_mes()

                    aluguel = {
                        "_id": documento['_id'],
                        "nome_pessoa": nome_pessoa,
                        "nome_livro": documento['nome'],
                        "data_aluguel": AcaoAluguel.data_atual,
                        "data_entrega": data_entrega,
                        "multa": 0
                    }

                    self._banco.add_document(type_collection=TypeCollections.ALUGUEIS, document=aluguel)
                    self._banco.update_document(
                        type_collection=TypeCollections.LIVROS,
                        filter_document=filtro_documento,
                        update_document={'$set': {'disponibilidade': False}}
                    )
                except Exception as erro:
                    self.erro(erro)
            else:
                self.erro('O livro não está disponível!')
        else:
            raise ErroSoftware('Livro inexistente!')

    def devolucao(self, codigo_livro: int) -> None:
        filtro_documento = {'_id': codigo_livro}

        existe_documento = self._banco.exists_document(
            type_collection=TypeCollections.ALUGUEIS,
            data_type=filtro_documento
        )

        if existe_documento:
            self._banco.delete_document(type_collection=TypeCollections.ALUGUEIS, code_document_delete=codigo_livro)
            self._banco.update_document(
                type_collection=TypeCollections.LIVROS,
                filter_document=filtro_documento,
                update_document={'$set': {'disponibilidade': True}}
            )
        else:
            raise ErroSoftware('Livro inexistente!')
