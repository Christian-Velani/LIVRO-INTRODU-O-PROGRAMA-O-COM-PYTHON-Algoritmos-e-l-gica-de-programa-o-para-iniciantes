#Exercício 10.9 - Crie classes para representar estados e cidades. Cada estado tem um
#nome, sigla e cidades. Cada cidade tem nome e população. Escreva um programa 
#de testes que crie três estados com algumas cidades em cada um. Exiba a população 
#de cada estado como a soma da população de suas cidades.

class Estado:
    def __init__(self, nome, sigla):
        self.nome = nome
        self.sigla = sigla
        self.cidades = []
    def adicionar_cidade(self, *cidades):
        for cidade in cidades:
            self.cidades.append(cidade)
    def populacao(self):
        populacao = 0
        for cidade in self.cidades:
            for i in range(len(cidade)):
                populacao += cidade[i].populacao
        print(f'População de {self.nome}: {populacao}')
    def listar_cidades(self):
        for cidade in self.cidades:
            for i in range(len(cidade)):
                print(f'Cidade: {cidade[i].nome} População: {cidade[i].populacao}')

class Cidade:
    def __init__(self, nome, populacao):
        self.nome = nome
        self.populacao = populacao

Minas_Gerais = Estado('Minas Gerais', 'MG')
Sao_Paulo = Estado('São Paulo', 'SP')
Goias = Estado('Goiás', 'GO')

sao_paulo = Cidade('São Paulo', 12396372)
guarulhos = Cidade('Guarulhos', 1404694)
campinas = Cidade('Campinas', 1223237)

belo_horizonte = Cidade('Belo Horizonte', 2521564)
uberlandia = Cidade('Uberlândia', 699097)
contagem = Cidade('Contagem', 668949)

goiania = Cidade('Goiânia', 155626)
aparecida_de_goiania = Cidade('Aparecida de Goiânia', 601844)
anapolis = Cidade('Anápolis', 396526)

Sao_Paulo.adicionar_cidade([sao_paulo, guarulhos, campinas])
Minas_Gerais.adicionar_cidade([belo_horizonte, uberlandia, contagem])
Goias.adicionar_cidade([goiania, aparecida_de_goiania, anapolis])

Sao_Paulo.listar_cidades()
Minas_Gerais.listar_cidades()
Goias.listar_cidades()

Sao_Paulo.populacao()
Minas_Gerais.populacao()
Goias.populacao()
