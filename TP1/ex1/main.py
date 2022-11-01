import re
from a import a
from d import d
from b import b
from c import c
import os
import platform


class ex1:
    def __init__(self):
        option = ""
        pathToFile = input("What is the path to a the file(\\n for default)")
        cOs = platform.platform().lower()
        file = self.parser(pathToFile)
        while (option != "quit"):
            option = input("What do you wish to do(\"help\" for help):")
            option = option.lower()
            self.clearConsole(cOs)
            if option == "help":
                print('''a: Get the frequency of processes by year\nb: Get the frequency of first and last names per century\nc: Get the frequency for each type of relationship\nd: Get the first 20 entries of the input file in json\nquit: Quit''')
            if option == "a":
                a(file)
            if option == "b":
                b(file)
            if option == "c":
                c(file)
            if option == "d":
                d(file, 20)
            if option == "quit":
                self.clearConsole(cOs)
                exit()

    def parser(self, path):
        if len(path) < 4:
            path = "./TP1/ex1/processos.txt"
        file = open(path, "r")
        pessoas = []
        for line in file.readlines():
            pessoas.append(re.split("::", line))
        file.close()
        processos = []
        for pessoa in pessoas:
            if pessoa[0] != "\n":
                processos.append(pessoa)
        return processos

    def clearConsole(self, cOs):
        if cOs == "windows":
            os.system("cls")
        else:
            os.system("clear")


ex1()
