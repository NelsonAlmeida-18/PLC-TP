import csv
import re
import matplotlib.pyplot as plt
from a import a
from b import b
from c import c
from d import d
from e import e
import os


class ex2:
    def __init__(self):
        # instala os packages necessários para a execução do programa
        os.system("pip3 install -r ./TP1/requirements.txt")
        option = ""
        # pede ao utilizador o path do ficheiro que quer utilizar tendo por default o emd.csv
        pathToFile = input("What is the path to a the file(\\n for default)")
        # retorna o ficheiro em arrays separados pelas virgulas
        file = self.parser(pathToFile)
        # invoca o exercício a com ficheiro parsed
        a().a(file)
        # invoca o exercício b com ficheiro parsed
        b().b(file)
        # invoca o exercício c com ficheiro parsed
        c().c(file)
        # invoca o exercício d com ficheiro parsed
        d().d(file)
        # invoca o exercício e com ficheiro parsed
        e().e(file)

    def parser(self, pathToFile):
        # caso o path sugerido pelo utilizador seja menor do que x.csv que tem tamanho 5 utiliza o default path
        if len(pathToFile) <= 5:
            pathToFile = "./TP1/ex2/emd.csv"
        parsedData = []
        # abre o ficheiro e adiciona ao array data cada linha do ficheiro separado por virgulas
        with open(pathToFile, newline='') as file:
            data = csv.reader(file, delimiter=' ', quotechar='|')
            for line in data:
                parsedData.append(re.split(",", line[0]))
        return parsedData[1:]


ex2()
