import re


class a:
    def __init__(self, processos):
        print(self.processesPerTimeSpan(processos))

    def processesPerTimeSpan(self, processos):
        processosPorData = {}
        while (processos != []):
            ano = re.match("(([0-9]{1,4})-*)", processos[0][1]).group(2)
            processosNoAno, processosNoutrosAnos = self.filtraPorAno(
                processos, ano)
            processosPorData[ano] = processosNoAno
            processos = processosNoutrosAnos

        return processosPorData

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
