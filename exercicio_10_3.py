#Exercício 10.3 Modifique a classe Televi.são de forma que, se pedirmos para mudar
#o canal para baixo, além do mínimo, ela vá para o canal máximo. Se mudarmos
#para cima, além do canal máximo, que volte ao canal mínimo. Exemplo:

class Televisao():
    def __init__(self, min, max, inicial):
        self.ligada = False
        self.canal = inicial
        self.cmin = min
        self.cmax = max
    def muda_canal_para_baixo(self):
        if self.canal - 1 >= self.cmin:
            self.canal -= 1
        elif self.canal == self.cmin:
            self.canal = self.cmax
    def muda_canal_para_cima(self):
        if self.canal + 1 <= self.cmax:
            self.canal += 1
        elif self.canal == self.cmax:
            self.canal = self.cmin
tv = Televisao(2, 10, 2)
tv.muda_canal_para_baixo()
print(tv.canal)
tv.muda_canal_para_cima()
print(tv.canal)