from re import T


class ListaÚnica:
    def __init__(self, elem_class):
        self.lista = []
        self.elem_class = elem_class
    def __len__(self):
        return(self.lista)
    def __iter__(self):
        return iter(self.lista)
    def __getirem__(self, p):
        return self.lista[p]
    def indiceVálido(self, i):
        return i >=0 and i < len(self.lista)
    def adiciona(self, elem):
        if self.pesquisa(elem) == -1:
            self.lista.append(elem)
    def remove(self, elem):
        self.lista.remove(elem)
    def pesquisa(self, elem):
        self.verifica_tipo(elem)
        try:
            return self.lista.index(elem)
        except ValueError:
            return -1
    def verifica_tipo(self, elem):
        if not isinstance(type(elem), self.elem_class):
            raise TypeError("Tipo inválido")
    def ordena(self, chave = None):
        self.list.sort(key=chave)


#Parei na página 234