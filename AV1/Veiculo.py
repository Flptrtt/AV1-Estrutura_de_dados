class Veiculo:
    def __init__(self,marca,modelo,ano_fabricacao,chassi,cor,quilometragem):
        self.marca = marca
        self.modelo = modelo
        self.ano_fabricacao = ano_fabricacao
        self.chassi = chassi
        self.cor = cor
        self.quilometragem = quilometragem

    def registrar_manutencao(self, tipo, custo):
        return f"Tipo de manutenção: {tipo}\nCusto: R${custo:.2f}"


    def exibir_informacoes(self,detalhado = False):
        if detalhado:
            return f"---informações detalhadas do veiculo-----\nMarca: {self.marca}\nModelo: {self.modelo}\nAno de fabricação: {self.ano_fabricacao}\nChassi: {self.chassi}\nCor: {self.cor}\nQuilometragem: {self.quilometragem}km"
        else:
            return f"------informações resumidas do veiculo-----\nMarca: {self.marca}\nModelo: {self.modelo}\nQuilometragem: {self.quilometragem}km"