import pandas as pd
import re

class DataLoader:
    filePath = None
    data = None
    
    def __init__(self, filePath):
        self.filePath = filePath
    
    def loadData(self):
        self.data = pd.read_excel(self.filePath)
        
        return self.data
        
    def cleanData(self):
        data = self.data
        data['Rede e Ano'] = data['Variável'].str.replace('Taxa de Aprovação no Ensino Médio - ', '', regex=False)
        
        for index, row in data.iterrows():
                a = re.findall(r'\d+', data.at[index, 'Rede e Ano'])
                ano = int(a[0]) 
                r = re.sub(r'\d+', '', data.at[index, 'Rede e Ano'])
                rede = r.strip()                
                data.at[index, 'Rede'] = rede
                data.at[index, 'Ano'] = ano
                
        self.data = data[['Código', 'Município', 'Rede', 'Ano', 'Valor (%)']]
        