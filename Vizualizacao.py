import matplotlib.pyplot as plt
import numpy as np
from Pesquisa import Pesquisa

class Vizualizacao():
    def plotGraficos(self, data): 

        data_agrupada = data.groupby('Rede')

        for name, group in data_agrupada:
            plt.figure(figsize=(10, 6))
            plt.plot(group['Ano'], group['Valor (%)'])
            plt.title(f'Taxa de Aprovação - {name}')
            plt.xlabel('Ano')
            plt.ylabel('Taxa de Aprovação (%)')
            plt.grid(True)
            plt.show()