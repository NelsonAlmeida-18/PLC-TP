import re
import csv


class b():
    def b(self, processos):
        data = processos[1:]  # aqui ficam tudo menos os indicadores
        # ir buscar os indices pelo n0me de parcela e colocar num dict tipo{id:0,dataEMD:1,"nome/primeiro":2,...}
        return (self.sportsPerYearandTotal(data))

    def sportsPerYearandTotal(self, data):
        sportsPerYear = {}
        totalSports = {}
        while (data):
            year = re.match("(([0-9]{1,4})-*)", data[0][2]).group(2)
            sportsYear, updatedData = self.sportsPerYear(data, year)
            sportsPerYear[year] = sportsYear
            data = updatedData
        # pode ser optimizado com o total sports a ser editado no while acima
        for year in sportsPerYear:
            for sport in sportsPerYear[year]:
                if sport not in totalSports:
                    totalSports[sport] = 0
                totalSports[sport] += sportsPerYear[year][sport]
        return sportsPerYear, totalSports

    def sportsPerYear(self, data, yearToFilter):
        sportsPerY = {}
        newData = []  # dataset sem as entradas no ano a ser filtrado
        for person in data:
            if re.match(yearToFilter+r"(-[0-9]{1,2}){2}", person[2]):
                sport = person[8]
                if sport not in sportsPerY:
                    sportsPerY[sport] = 0
                sportsPerY[sport] += 1
            else:
                newData.append(person)
        return sportsPerY, newData
