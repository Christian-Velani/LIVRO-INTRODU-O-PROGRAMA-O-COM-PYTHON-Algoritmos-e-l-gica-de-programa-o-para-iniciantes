from functools import total_ordering
import lista_unica

@total_ordering
class TipoTelefone:
    def __init__(self, tipo):
        self.tipo = tipo
    def __str__(self):
        return f'({self.tipo})'
    def __eq__(self, outro):
        if outro is None:
            return False
        return self.tipo == outro.tipo
    def __lt__(self, outro):
        return self.tipo < outro.tipo

class Telefone:
    def __init__(self, numero, tipo = None):
        self.numero = numero
        self.tipo = tipo
    def __str__(self):
        if self.tipo is not None:
            tipo = self.tipo
        else:
            tipo = ''
        return f'{self.numero} {tipo}'
    def __eq__(self, outro):
        return self.numero == outro.numero and ((self.tipo == outro.tipo) or (self.tipo is None or outro.tipo is None))
    @property
    def numero(self):
        return self.__numero
    @numero.setter
    def numero(self, valor):
        if valor is None or not valor.strip():
            raise ValueError('Número não pode ser None ou em branco')
        self.__numero = valor

class Telefones(lista_unica.ListaÚnica):
    def __init__(self):
        super().__init__(Telefone)

class DadoAgenda:
    def __init__(self, nome):
        self.nome = nome
        self.telefones = Telefones()

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, valor):
        if not isinstance(type(valor), Nome):
            raise TypeError('nome deve ser uma instância da classe Nome')
        self.__nome = valor

    def pesquisaTelefone(self, telefone):
        posição = self.telefones.pesquisa(Telefone(telefone))
        if posição == -1:
            return None
        else:
            return self.telefones[posição]

class TiposTelefone(lista_unica.ListaÚnica):
    def __init__(self):
        super().__init__(TipoTelefone)

class Agenda(lista_unica.ListaÚnica):
    def __init__(self):
        super().__init__(DadoAgenda)
        self.tiposTelefone = TiposTelefone()
    def adicionaTipo(self, nome):
        if isinstance(type(none), str):
            nome = Nome(nome)
        for dados in self.lista:
            if dados.nome == nome:
                return dados
            else:
                return None
    def ordena(self):
        super().ordena(lambda dado: str(dado.nome))