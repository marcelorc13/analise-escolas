class Report:
    def __init__(self, analysis):
        self.analysis = analysis
    def generate_report(self):
        print("Relatório de Análise:")
        print("-----------------------")
        print(f"Análise concluida: {self.analysis}")
        print("Relatório gerado com sucesso!")

