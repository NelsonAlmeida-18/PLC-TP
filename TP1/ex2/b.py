import re
import pandas as pd
import matplotlib.pyplot as plt


class b():
    def b(self, data):
        sportsPerYear, totalSports = self.sportsPerYearandTotal(data)
        indexes = sorted(sportsPerYear)
        sportsPerYear = {i: sportsPerYear[i] for i in indexes}
        totalSports = dict(sorted(totalSports.items(), key=lambda x: x[1]))
        self.plotter(sportsPerYear, totalSports)
        self.htmlGenerator(sportsPerYear, totalSports)

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

    def htmlGenerator(self, data1, data2):
        file = open(f"./TP1/ex2/1/website/b.html", "w")
        templateText1 = pd.DataFrame(data1).to_html()
        templateText1 = re.sub(
            r'''<table border="1" class="dataframe">''', '''<h1 class="title">Distribuição por modalidade em cada ano e no total</h1>\n<div class="images" style="display: flex; width: 100%; padding-bottom: 2rem;"><img src="./src/b1.png" alt="" style="width:50%">\n<img src="./src/b2.png" alt="" style="width:50%">\n</div>\n<link rel="stylesheet" href="./main.css">\n<table border="1" class="dataframe">''', templateText1
        )
        file.write(templateText1)
        templateText2 = pd.DataFrame(data2, index=["Praticantes"]).to_html()
        file.write(templateText2)
        file.close()

    def plotter(self, data1, data2):
        df1 = pd.DataFrame(data1)
        df1.plot(kind="bar")
        plt.savefig("./TP1/ex2/1/website/src/b1.png")
        df2 = pd.DataFrame(data2, index=["Praticantes"])
        df2.plot(kind="bar")
        plt.savefig("./TP1/ex2/1/website/src/b2.png")
