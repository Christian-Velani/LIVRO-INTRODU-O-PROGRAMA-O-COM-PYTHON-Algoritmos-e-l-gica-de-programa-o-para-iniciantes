#Exercício 10.4 Utilizando o que aprendemos com funções, modifique o construtor
#da classe Televisão de forma que min e max sejam parâmetros opcionais, em que min
#vale 2 e max vale 14, caso outro valor não seja passado.

class Televisao():
    def __init__(self,  inicial, min = 2, max = 14):
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

tv = Televisao(5)
tv2 = Televisao(5, 5)
tv3 = Televisao(2, max = 35)

print(tv.cmin, tv.cmax)
print(tv2.cmin, tv2.cmax)
print(tv3.cmin, tv3.cmax)