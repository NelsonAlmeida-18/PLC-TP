import csv
from email.utils import decode_rfc2231
import re
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from b import b
from c import c
from d import d
from e import e


class ex2:
    def __init__(self):
        option = ""
        pathToFile = input("What is the path to a the file(\\n for default)")
        file = self.parser(pathToFile)
        bOutput = b().b(file)
        cOutput = c().c(file)
        dOutput = d().d(file)
        eOutput = e().e(file)
        places = []
        nums = []
        # for i in bOutput[1]:
        #    places.append(i)
        #    nums.append(bOutput[1][i])
        #df = pd.DataFrame(nums, index=places)
        # df.plot(kind="bar")
        # print(bOutput[1])
        #df = pd.DataFrame(dOutput)
        # df.plot(kind="bar")
        #sortedDict = sorted(bOutput[1])
        #newDict = {i: bOutput[1][i] for i in sortedDict}
        #df2 = pd.DataFrame.from_dict(newDict, orient='index')
        #df2 = df2.transpose()
        #ax = df2.plot(kind="bar")
        #ax.set_xticks(np.arange(3), sortedDict)
        #ax.set_title("Distribuição de praticantes de desporto por anos")
        # ax.legend()
        # plt.show()

    def setUpDataFrame(self, data):
        df = {}
        for i in data:
            for sport in data[i]:
                if sport not in df:
                    df[sport] = []
                df[sport].append(data[i][sport])
        return df

    def parser(self, pathToFile):
        if len(pathToFile) <= 4:
            pathToFile = "./TP1/ex2/emd.csv"
        parsedData = []
        with open(pathToFile, newline='') as file:
            data = csv.reader(file, delimiter=' ', quotechar='|')
            for line in data:
                parsedData.append(re.split(",", line[0]))
        return parsedData

    def htmlGenerator(self, data, nameOfFile):
        df = pd.DataFrame(data, index=[""])
        result = df.to_html()
        file = open(f"{nameOfFile}.html", "w")
        file.write(result)
        file.close()


ex2()
