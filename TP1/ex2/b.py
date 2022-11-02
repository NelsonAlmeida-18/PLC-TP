import re
import pandas as pd
import matplotlib.pyplot as plt


class b():
    def b(self, data):
        sportsPerYear, totalSports = self.sportsPerYearandTotal(data)
        indexes = sorted(sportsPerYear)
        # dá sort ao dicionário sportsPerYear por data
        sportsPerYear = {i: sportsPerYear[i] for i in indexes}
        # ordena o dicionário pelos valores, neste caso quantos desportistas estão presentes no dataset para cada desporto
        totalSports = dict(sorted(totalSports.items(), key=lambda x: x[1]))
        # gera os gráficos dos datasets guardando-os na pasta src para depois ser usado na criação do website
        self.plotter(sportsPerYear, totalSports)
        # gera o ficheiro html com as tabelas dos desportos por ano e desportos no total juntamente com as imagens dos gráficos geradas acima
        self.htmlGenerator(sportsPerYear, totalSports)

    def sportsPerYearandTotal(self, data):
        sportsPerYear = {}
        totalSports = {}
        while (data):
            # vamos buscar uma data arbitrária ao array, neste caso a primeira
            year = re.match("(([0-9]{1,4})-*)", data[0][2]).group(2)
            # passamos a data colecionada acima à função sports per year que a vai utilizar para filtrar os dados dos desportos com registos nesse ano
            # e retorna também todos os elementos do array cujos registos são em anos diferentes ao passado à função
            sportsYear, updatedData = self.sportsPerYear(data, year)
            # adiciona a informação do desporto nesse ano ao dicionário de desportos por ano onde a chave é o ano(sabemos que isto nunca se repetirá devido à forma como a função
            # sportsPerYear está concebida
            sportsPerYear[year] = sportsYear
            data = updatedData

        # com os dados colecionados no dicionário sportsPerYear soma o número de desportistas para cada ano e para cada desporto e coleciona no novo dicionário de totalSports
        for year in sportsPerYear:
            for sport in sportsPerYear[year]:
                if sport not in totalSports:
                    totalSports[sport] = 0
                totalSports[sport] += sportsPerYear[year][sport]
        return sportsPerYear, totalSports

    def sportsPerYear(self, data, yearToFilter):
        sportsPerY = {}
        newData = []
        for person in data:
            # a
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
