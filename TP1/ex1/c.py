import re


class c:
    def __init__(self, processos):  # ver a abertura do file.txt e os prints nao tao bem
        print(self.tiposParentesco(processos))

    def tiposParentesco(self, pessoas):
        tipos = {}  # iremos obter algo como -> { pai:5, tio:50, ...}   key -> parentesco  values-> nº elems de cada parentesco
        for pessoa in pessoas:
            # Com [PMTISAFNB] obtemos todas as iniciais dos tipos de parentesco
            for elem in pessoa:
                parent = re.findall(
                    r'(?<=[a-z]\,)([PMTISANB][A-Za-z ]+|Filho|Filhos)(?=\.)', elem)
                for x in parent:
                    if x in tipos.keys():
                        # incrementamos o nº desse parentesco
                        tipos[x] = tipos.get(x, 0) + 1
                    else:
                        # adicionamos essa key e value inicial = 1
                        tipos[x] = 1
        return tipos
