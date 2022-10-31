import re


class d:
    def __init__(self, processos):
        if (self.jsonFormatter(processos)):
            print("Ficheiro criado com sucesso")
        else:
            print("Ocorreu um erro a criar o ficheiro")

    def jsonFormatter(self, pessoas):
        jsonFormatData = []
        file = open("data.json", "w")
        for pessoa in pessoas:
            pessoa.append("")
            file.write({"folder_id": pessoa[0], "date": pessoa[1], "name": pessoa[2],
                        "father": pessoa[3], "mother": pessoa[4], "obs": pessoa[5]})
        file.close()
