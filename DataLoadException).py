class DataLoadException(Exception):
    def __init__(self, message, data_source=None):
    def __str__(self):
        if self.data_source:
            return f"[DataLoadException] Erro ao carregar dados de '{self.data_source}': {self.message}"
        return f"[DataLoadException] {self.message}"
def load_data(data_source):
    if not data_source:
        raise DataLoadException("Fonte de dados inválida", data_source)
    print(f"Dados carregados com sucesso de {data_source}.")

