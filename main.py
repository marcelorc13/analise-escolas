from data_loader import DataLoader
from search import Search

# data = DataLoader('taxa-aprovacao.xls')
# s = data.loadData()
# print(s)

teste = Search('taxa-aprovacao.xls')

cidade = input()
t = teste.procurarCidade(cidade)

print(t)
print(teste.codigo)
