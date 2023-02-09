from datetime import date

class FuncoesAuxiliares:
    def verificaExistenciaLivro(self, codigoLivro: int, biblioteca: any):
        existeciaCodigo = False
        for i in range(len(biblioteca)):
            if biblioteca[i].getCodigo() == codigoLivro:
                existeciaCodigo = True
                return i, existeciaCodigo
        return -1, existeciaCodigo
    
    def buscarAlugado(self, codigoLivro: int, alugados: any):
        for alugado in alugados:
            if alugado.getCodigo() == codigoLivro:
                return alugado
        return ''
    
    def gerarDataAtual(self):
        return date.today().strftime('%d/%m/%Y')
    
    def gerarDataProximoMes(self):
        ano = date.today().year
        mes = date.today().month
        dia = date.today().day
        
        if mes == 2 and dia > 28:
            dia = 3
        elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
            dia = 1
        
        novaData = date(ano, mes+1, dia)
        return novaData.strftime('%d/%m/%Y')