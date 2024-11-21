class AnalysisException(Exception):
    def __str__(self):
        if self.analysis_details:
            return f"[AnalysisException] Erro na análise de dados: {self.message}. Detalhes: {self.analysis_details}"
        return f"[AnalysisException] {self.message}"
