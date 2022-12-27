import re
import pandas as pd
import matplotlib.pyplot as plt


class e:
    def e(self, data):
        data = data[1:]
        readinessStats = {}
        # ir buscar os anos, e os aptos/total, não aptos/total
        while (data):
            year = re.match("(([0-9]{1,4})-*)", data[0][2]).group(2)
            (ready, total), newData = self.readinessPerYear(data, year)
            readinessPerc = (ready/total)
            readinessStats[year] = {
                "ready": float("{:.2f}".format(100*readinessPerc)),
                "not_ready": float("{:.2f}".format(100*(1-readinessPerc)))
            }
            data = newData
        self.plotter(readinessStats)
        self.htmlGenerator(readinessStats)

    def readinessPerYear(self, data, year):
        ready = 0
        total = 0
        newData = []
        for person in data:
            if re.match(year+r"(-[0-9]{1,2}){2}", person[2]):
                if person[-1] == "true":
                    ready += 1
                total += 1
            else:
                newData.append(person)
        return (ready, total), newData

    def htmlGenerator(self, data1):
        file = open(f"./TP1/ex2/1/website/e.html", "w")
        templateText = pd.DataFrame(data1).to_html()
        templateText = re.sub(
            r'''<table border="1" class="dataframe">''', '''<p class="title">Percentagem de aptos e não aptos por ano</p>\n<div class="images" style="padding-bottom: 2rem;"><img src="./src/e.png" alt="">\n</div>\n<link rel="stylesheet" href="main.css">\n<table border="1" class="dataframe">''', templateText)
        file.write(templateText)
        file.close()

    def plotter(self, data):
        df1 = pd.DataFrame(data)
        df1.plot(kind="bar")
        plt.savefig("./TP1/ex2/1/website/src/e.png")
