import re
import pandas as pd
import matplotlib.pyplot as plt


class c:
    def c(self, processos):
        data = processos[1:]  # aqui ficam tudo menos os indicadores
        data = self.distByAgeAndGender(data)
        self.plotter(data)
        self.htmlGenerator(data)

    def distByAgeAndGender(self, data):
        dist = {"<35": {}, ">=35": {}}
        ageIndex = 5  # tentar generalizar estes indices com um interpretador
        genderIndex = 6
        for person in data:
            ageRange = ">=35"
            if int(person[ageIndex]) < 35:
                ageRange = "<35"
            if person[genderIndex] not in dist[ageRange]:
                dist[ageRange][person[genderIndex]] = 0
            dist[ageRange][person[genderIndex]] += 1
        return dist

    def htmlGenerator(self, data1):
        file = open(f"./TP1/ex2/1/website/c.html", "w")
        templateText = pd.DataFrame(data1).to_html()
        templateText = re.sub(
            r'''<table border="1" class="dataframe">''', '''<p class="title">Distribuição por idade e género</p>\n<div class="images" style="padding-bottom: 2rem;"><img src="./src/c.png" alt="">\n</div>\n<link rel="stylesheet" href="./main.css">\n<table border="1" class="dataframe">''', templateText)
        file.write(templateText)
        file.close()

    def plotter(self, data):
        df1 = pd.DataFrame(data)
        df1.plot(kind="bar")
        plt.savefig("./TP1/ex2/1/website/src/c.png")
