import ply.lex as lex
import sys
import os
import re


class Paulocompiler:
    def __init__(self):
        nameOfFile = input("Path for file: ")
        print(os.getcwd())
        if (re.search(r"([a-zA-Z]|[0-9]|\/)*.paulo", nameOfFile, flags=re.IGNORECASE)):
            self.compiler(nameOfFile)
        else:
            print("Invalid file extension")

    def compiler(self, nameOfFile):
        file = open(nameOfFile, "r")
        content = file.readlines()
        print(content)


Paulocompiler()
