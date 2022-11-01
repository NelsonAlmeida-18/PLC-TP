import csv
from IPython.display import HTML, display
import re
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from a import a
from b import b
from c import c
from d import d
from e import e


class ex2:
    def __init__(self):
        option = ""
        pathToFile = input("What is the path to a the file(\\n for default)")
        file = self.parser(pathToFile)
        aOutput = a().a(file)
        bOutput = b().b(file)
        cOutput = c().c(file)
        dOutput = d().d(file)
        eOutput = e().e(file)

    def parser(self, pathToFile):
        if len(pathToFile) <= 4:
            pathToFile = "./TP1/ex2/emd.csv"
        parsedData = []
        with open(pathToFile, newline='') as file:
            data = csv.reader(file, delimiter=' ', quotechar='|')
            for line in data:
                parsedData.append(re.split(",", line[0]))
        return parsedData[1:]


ex2()
