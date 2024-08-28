from datetime import date

from src.tratamento import *
from ..banco import *


class AcaoAluguel(TratamentoErro):
    data_atual = date.today().strftime('%d/%m/%Y')

    @staticmethod
    def _gerar_data_proximo_mes():
        ano = date.today().year
        mes = date.today().month
        dia = date.today().day

        if mes == 2 and dia > 28:
            dia = 3
        elif dia > 30 and (mes == 4 or mes == 6 or mes == 9 or mes == 11):
            dia = 1

        nova_data = date(ano, mes + 1, dia)
        return nova_data.strftime('%d/%m/%Y')

    def alugar(self, banco: Banco, informacoes_aluguel: list) -> None:
        codigo_livro, nome_pessoa = informacoes_aluguel

        filtro_documento = {'codigo': codigo_livro}

        existe_documento = banco.exists_document(
            type_collection=TypeCollections.LIVROS,
            data_type=filtro_documento
        )

        if existe_documento:
            documentos = banco.find_document(type_collection=TypeCollections.LIVROS, data_type={"codigo": codigo_livro})
            documento = documentos[0]
            disponivel = documento['disponibilidade']

            if disponivel:
                try:
                    data_entrega = self._gerar_data_proximo_mes()

                    aluguel = {
                        "nome_pessoa": nome_pessoa,
                        "codigo": documento['codigo'],
                        "nome_livro": documento['nome'],
                        "data_aluguel": AcaoAluguel.data_atual,
                        "data_entrega": data_entrega,
                        "multa": 0
                    }

                    banco.update_document(
                        type_collection=TypeCollections.LIVROS,
                        filter_document=filtro_documento,
                        update_document={'$set': {'disponibilidade': False}}
                    )
                    banco.add_document(type_collection=TypeCollections.ALUGUEIS, document=aluguel)
                    print('\nLivro alugado com sucesso.')
                except Exception as erro:
                    self.erro(erro)
        else:
            print('\nNão existe este livro nos cadastros.')

    def terminal_alugar(self, banco: Banco) -> None:
        self.__titulo_alugar()

        try:
            codigo_livro = int(input('Qual o código do livro? '))
            nome_pessoa = self.inserirNome('\nDigite o nome completo da pessoa que está alugando o livro: ')
            self.alugar(banco=banco, informacoes_aluguel=[codigo_livro, nome_pessoa])
        except Exception as erro:
            self.erro(erro)

    @staticmethod
    def app_devolucao(banco: Banco, codigo_livro: int) -> None:
        filtro_documento = {'codigo': codigo_livro}

        existe_documento = banco.exists_document(
            type_collection=TypeCollections.ALUGUEIS,
            data_type=filtro_documento
        )

        if existe_documento:
            banco.delete_document(type_collection=TypeCollections.ALUGUEIS, code_document_delete=codigo_livro)
            banco.update_document(
                type_collection=TypeCollections.LIVROS,
                filter_document=filtro_documento,
                update_document={'$set': {'disponibilidade': True}}
            )
        else:
            raise ErroSoftware('Livro inexistente!')

    def devolucao(self, banco: Banco) -> None:
        self.__titulo_devolucao()

        try:
            codigo_livro = int(input('Qual o código do livro? '))
            self.app_devolucao(banco=banco, codigo_livro=codigo_livro)
        except Exception as erro:
            self.erro(erro)

    @staticmethod
    def __titulo_alugar() -> None:
        print('''
======================================================
======================= Alugar =======================
======================================================
''')

    @staticmethod
    def __titulo_devolucao() -> None:
        print('''
======================================================
====================== Devolver ======================
======================================================
''')
