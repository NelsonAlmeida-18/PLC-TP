import re
import pandas as pd
import matplotlib.pyplot as plt


class d:
    def d(self, processos):
        data = processos[1:]
        data = self.distByAddress(data)
        self.plotter(data)
        self.htmlGenerator(data)

    def distByAddress(self, data):
        distByAddress = {}
        for person in data:
            address = person[7]
            if address not in distByAddress:
                distByAddress[address] = 0
            distByAddress[address] += 1
        return distByAddress

    def htmlGenerator(self, data1):
        file = open(f"./TP1/ex2/1/website/d.html", "w")
        templateText = pd.DataFrame(data1, index=[""]).to_html()
        templateText = re.sub(
            r'''<table border="1" class="dataframe">''', '''<p class="title">Distribuição por morada</p>\n<div class="images" style="padding-bottom: 2rem;"><img src="./src/d.png" alt="">\n</div>\n<link rel="stylesheet" href="./main.css">\n<table border="1" class="dataframe">''', templateText)
        file.write(templateText)
        file.close()

    def plotter(self, data):
        # dividir os charts
        if len(data) >= 50:
            df1 = pd.DataFrame(data, index=[""])
            df1.plot(kind="bar")
            plt.savefig("./TP1/ex2/1/website/src/d.png")
        else:
            df1 = pd.DataFrame(data, index=[""])
            df1.plot(kind="bar")
            plt.savefig("./TP1/ex2/1/website/src/d.png")
