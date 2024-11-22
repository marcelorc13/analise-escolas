from CarregadorDeArquivos import CarregadorDeArquivos
from Pesquisa import Pesquisa
from Vizualizacao import Vizualizacao

class Main:
    def executarBusca(self):
        pesquisa = Pesquisa('taxa-aprovacao.xls')
        print(f'Insira o município que deseja saber as taxas de aprovação: ')
        cidade = input()

        data = pesquisa.procurarCidade(cidade)

        print(data)
        
        viz = Vizualizacao()
        viz.plotGraficos(data)
        
main = Main()
main.executarBusca()
