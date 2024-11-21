from CarregadorDeArquivos import CarregadorDeArquivos
import pandas as pd

class Search(CarregadorDeArquivos):
    
    codigo = None
    searchData = None
    
    def __init__(self, filePath):
        super().__init__(filePath)
        
        
    def procurarCidade(self, input):
        load = CarregadorDeArquivos(self.filePath)
        load.carregarDados()
        load.limparDados()
        
        data = load.data
        
        municipio = input.upper()
        
        for index, row in data.iterrows():
            if(row['Município'] == municipio):
                self.codigo = row['Código']
        
        data = data[data['Código'] == self.codigo ]

        for index, row in data.iterrows():
            if pd.isna(row['Valor (%)']):
                data.at[index, 'Valor (%)'] = 'Não consta'

        self.searchData = data
        return self.searchData
        