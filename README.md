# AV1-Estrutura_de_dados - Filipe Trotte
Descrição do projeto: 
Desenvolver um sistema que gerencie diferentes tipos de veículos de uma frota e suas manutenções, aplicando os conceitos de Herança, Polimorfismo (simulação de sobrecarga) e Encapsulamento em Python.
Classes: Veiculo(superclasse ou classe abstrata),CarroPasseio(subclasse) e CaminhaoCarga(subclasse)


Classe Veiculo: 
Primeira coisa que eu fiz foi criar a classe Veiculo e o construtor através do metodo especial do python __init__ utilizando self + exatamente os atributos do enunciado.

Criei o método registrar_manutencao que recebe como argumentos o tipo de manutenção e o custo da manutenção e retorna uma string com o tipo de manutenção e o custo em reais com 2 casas decimais após a virgula.

Criei o método exibir_informacoes que recebe como argumento um boolean chamado detalhado que por padrão é falso, escolhi deixar o padrão ser falso pois é mais comum buscar informações resumidas, dentro do método tem um if e else que se detalhado for verdadeiro vai exibir todas as informações e se for falso somente marca modelo e quuilometragem conforme o enunciado.


Classe CarroPasseio:
Importei do Módulo Veiculo a classe Veiculo
Criei a classe CarroPasseio e o construtor com __init__ utilizando super()para herdar todos os atributos da classe Veiculo e adiconei os atributos numero_portas e tipo_combustivel conforme o enunciado.

Criei o método calcular_depreciacao com argumentos anos_uso e taxa_extra, interpretei que se existe uma taxa_extra deve ter uma taxa_base e criei essa variavel com valor 0.10(10%) criei a variavel depreciacao que recebe o resultado do calculo e o método retorna a exibição da depreciação em %

Criei o método exibir_informacoes que recebe detalhado como argumento e como padrao começa false, criei a variável informacoes_carro e usei o super para que a variavel herde o exibir informacoes de veiculo e usei estrutura condicional if para retornar a informação completa caso true ou apenas as informaçoes resumidas que já estao na classe Veiculo.


Classe CaminhaoCarga:
Importei do Módulo Veiculo a classe Veiculo
Criei a classe CaminhaoCarga e o construtor com __init__ utilizando super() para herdar todos os atributos da calsse Veiculo e adicionei os atributos capacidade_toneladas e eixos.

Criei o método registrar_vistoria que recebe como argumento motivo e multa, criei uma variável motivo_vistoria que recebe o motivo e uma variavel multa que recebe multa, o método retorna a exibição do motivo da vistoria e a multa.

Criei o método exibir_informacoes que recebe detalhado como argumento e como padrao começa false, criei a variável informacoes_caminhao e usei o super para que a variavel herde o exibir informacoes de veiculo e usei estrutura condicional if para retornar a informação completa caso true ou apenas as informaçoes resumidas que já estao na classe Veiculo.


main:
Importei do Módulo CarroPasseio a classe CarroPasseio
Importei do Módulo CaminhaoCarga a classe CaminhaoCarga
Criei a função main que instancia 1 carro e 1 caminhao e exibe o return dos métodos das classes com print 
Executei a função main
