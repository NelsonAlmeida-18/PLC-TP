import json
import re


class d:
    def __init__(self, processos, limit):
        if (self.jsonFormatter(processos[0:limit])):
            print("Ficheiro criado com sucesso")
        else:
            print("Ocorreu um erro a criar o ficheiro")

    def jsonFormatter(self, pessoas):
        file = open("./TP1/ex1/rois.json", "w")
        file.write("{\"data\":[")
        templateJson = '''{"folder_id":#,"date":#, "name":#,"father":#,"mother":#,"obs":#}'''
        pos = 0
        for pessoa in pessoas:
            # para eliminar a possibilidade das obs estarem vazias e matarem o programa
            pessoa.append("")
            person = templateJson
            for i in pessoa:
                person = re.sub("#", f"\"{i}\"", person, count=1)
            if (pos < len(pessoas)-1):
                file.write(person+",\n")
            else:
                file.write(person)
            pos += 1
        file.write("]}")
        file.close()
        return True
