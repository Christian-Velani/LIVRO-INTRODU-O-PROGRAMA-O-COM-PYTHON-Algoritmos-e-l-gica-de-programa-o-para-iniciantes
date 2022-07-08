#Exercício 10.2 Atualmente, a classe Televi.são inicializa o canal com 2. Modifique a
#classe Televisão de forma a receber o canal inicial em seu construtor.

class Televisao():
    def __init__(self, min, max, inicial):
        self.ligada = False
        self.canal = inicial
        self.cmin = min
        self.cmax = max
    def muda_canal_para_baixo(self):
        if self.canal - 1 >= self.cmin:
            self.canal -= 1
    def muda_canal_para_cima(self):
        if self.canal + 1 <= self.cmax:
            self.canal += 1

tv = Televisao(1, 99, 5)
print(tv.canal)
tv.muda_canal_para_baixo()
print(tv.canal)
tv2 = Televisao(2, 25, 10)
print(tv2.canal)
for i in range(15):
    tv2.muda_canal_para_cima()
print(tv2.canal)