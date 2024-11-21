from CarregadorDeArquivos import CarregadorDeArquivos
from Pesquisa import Search

# data = CarregadorDeArquivos('taxa-aprovacao.xls')
# s = data.loadData()
# print(s)

teste = Search('taxa-aprovacao.xls')

cidade = input()
t = teste.procurarCidade(cidade)

print(t)
print(teste.codigo)
