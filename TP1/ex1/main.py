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
        processosPorData = {}
        while (processos != []):
            #print(len(processos), len(processosPorData))
            ano = re.match("(([0-9]{1,4})-*)", processos[0][1]).group(2)
            processosNoAno, processosNoutrosAnos = self.filtraPorAno(
                processos, ano)
            processosPorData[ano] = processosNoAno
            processos = processosNoutrosAnos
        print(processosPorData)

    def filtraPorAno(self, processos, yearToFilter):
        procPerYear = 0
        processosNoutrosAnos = []
        for pessoa in processos:
            flag = 0
            for elem in pessoa:
                if re.search(yearToFilter+r"-[0-9]{2}-[0-9]{1,2}", elem):
                    flag = 1
            if flag == 1:
                procPerYear += 1
            else:
                processosNoutrosAnos.append(pessoa)
        return (procPerYear, processosNoutrosAnos)

    def filtraProcessos(self, pessoas):
        processos = []
        for pessoa in pessoas:
            for elem in pessoa:
                if re.search("Proc.[0-9]*", elem):
                    processos.append(pessoa)
        return processos


ex1()
