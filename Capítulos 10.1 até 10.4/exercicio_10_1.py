#Exercício 10.1 Adicione os atributos tamanho e marca à classe Televi.são. Crie dois
#objetos Televisão e atribua tamanhos e marcas diferentes. Depois, imprima o valor
#desses atributos de forma a confirmar a independência dos valores de cada instância
#(objeto).

class Televisao():
    def __init__(self):
        self.ligada = False
        self.canal = 2
        self.marca = "AOC"
        self.tamanho = 42

tv = Televisao()
tv_sala = Televisao()
tv_sala.marca = "TCL"
tv_sala.tamanho = 50

print(tv.marca)
print(tv_sala.marca)
print(tv.tamanho)
print(tv_sala.tamanho)
