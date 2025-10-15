from Veiculo import Veiculo
class CaminhaoCarga(Veiculo):
    def __init__(self,marca,modelo,ano_fabricacao,chassi,cor,quilometragem,capacidade_toneladas,eixos):
        super().__init__(marca,modelo,ano_fabricacao,chassi,cor,quilometragem)
        self.capacidade_toneladas = capacidade_toneladas
        self.eixos = eixos


    def registrar_vistoria(self,motivo, multa):
        self.motivo_vistoria = motivo
        self.multa = multa
        return f"Motivo da vistoria: {self.motivo_vistoria}\nMulta: R${self.multa:.2f}"

    def exibir_informacoes(self,detalhado=False):
        informacoes_caminhao = super().exibir_informacoes(detalhado)
        if detalhado:
            return f"{informacoes_caminhao}\nCapacidade(toneladas): {self.capacidade_toneladas}\nEixos: {self.eixos}"
        return informacoes_caminhao