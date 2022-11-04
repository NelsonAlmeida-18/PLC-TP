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
        ageIndex = 5  # indice da representação dos dados relativos à idade no array
        genderIndex = 6  # indice da representação dos dados relativos ao género no array
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
        # através do dicionário criado acima, utilizamos a library pandas para através de um dataframe gerar a representação da tabela
        # em html guardada numa variável para depois ser processada
        templateText = pd.DataFrame(data1).to_html()
        templateText = re.sub(
            r'''<table border="1" class="dataframe">''', '''<p class="title">Distribuição por idade e género</p>\n<div class="images" style="padding-bottom: 2rem;"><img src="./src/c.png" alt="">\n</div>\n<link rel="stylesheet" href="./main.css">\n<table border="1" class="dataframe">''', templateText)
        file.write(templateText)
        file.close()

    def plotter(self, data):
        # com os dados passados a esta função geramos os gráficos(recorrendo à library pandas e matplotlib)
        df1 = pd.DataFrame(data)
        df1.plot(kind="bar")
        plt.savefig("./TP1/ex2/1/website/src/c.png")
