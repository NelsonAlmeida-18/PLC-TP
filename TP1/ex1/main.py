import re
import os


class ex1:

    def __init__(self):
        file = open("./TP1/ex1/processos.txt", "r")
        pessoas = []
        for line in file.readlines():
            pessoas.append(re.split("::", line))
        # por cada ano, função genérica que permite o filtro de processos por espaço de tempo selecionado
        self.processesPerTimeSpan(pessoas, 1)

        file.close()

    def processesPerTimeSpan(self, pessoas, timeSpan):
        processos = self.filtraProcessos(pessoas)
        print(len(processos), len(pessoas))
        ano = re.match("(([0-9]{1,4})-*)", processos[0][1]).group(2)
        print(self.filtraPorAno(pessoas, ano))
        # filtro por ano

    def filtraPorAno(self, pessoas, yearToFilter):
        procPerYear = []
        for pessoa in pessoas:
            for elem in pessoa:
                print(elem)
                # testar a passagem pelo formatador
                if re.search(f"{yearToFilter}-[0-9]{2}-[0-9]{1,2}", elem):
                    procPerYear.append(pessoa)
        return procPerYear

    def filtraProcessos(self, pessoas):
        processos = []
        for pessoa in pessoas:
            for elem in pessoa:
                if re.search("Proc.[0-9]*", elem):
                    processos.append(pessoa)
        return processos


ex1()
