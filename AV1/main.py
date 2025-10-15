#Importando classes necessarias
from CarroPasseio import CarroPasseio
from CaminhaoCarga import CaminhaoCarga


def main():
    #Instânciando objeto da classe CarroPasseio
    carro1 = CarroPasseio("Honda","Civic",2021,"1234567890ABC","Preto",15000,4,"Gasolina")

    print(carro1.exibir_informacoes())#Testando método que exibe informações não detalhadas| detalhado = false
    print(carro1.exibir_informacoes(detalhado=True))#Testando método que exibe informaçoes completas
    print(carro1.calcular_depreciacao(5,0.02))#Testando método da classe CarroPasseio|Não tenho ideia de como funciona depreciação de veiculos, coloquei em porcentagem 
    print(carro1.registrar_manutencao("Troca de óleo", 250))#Testando método do veículo

    #Instânciando objeto da classe CaminhaoCarga
    caminhao1 = CaminhaoCarga("Scania","R 450",2019,"9876543210XYZ","Branco",120000,40,6)
    print(caminhao1.exibir_informacoes())#Testando método que exibe informações não detalhadas| detalhado = false
    print(caminhao1.exibir_informacoes(detalhado = True))#Testando método que exibe informaçoes completas
    print(caminhao1.registrar_vistoria("Inspeção de segurança",800))#Testando método do caminhao
    print(caminhao1.registrar_manutencao("Revisão de freios",1200))#Testando método do veículo


if __name__ == "__main__":
    main()