from Veiculo import Veiculo
class CarroPasseio(Veiculo):
    def __init__(self,marca,modelo,ano_fabricacao,chassi,cor,quilometragem,numero_portas,tipo_combustivel):
        super().__init__(marca,modelo,ano_fabricacao,chassi,cor,quilometragem)
        self.numero_portas = numero_portas
        self.tipo_combustivel = tipo_combustivel
    
    
    def calcular_depreciacao(self,anos_uso, taxa_extra):
        taxa_base= 0.10
        depreciacao=taxa_base*anos_uso+(taxa_extra*anos_uso)
        return f"Depreciacao: {depreciacao*100:.2f}%"

    def exibir_informacoes(self,detalhado = False):
        informacoes_carro = super().exibir_informacoes(detalhado)
        if detalhado:
            return f"{informacoes_carro}\nPortas: {self.numero_portas}\nCombustivel: {self.tipo_combustivel}"
        return informacoes_carro