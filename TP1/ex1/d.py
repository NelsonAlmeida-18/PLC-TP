import re


class d:
    def __init__(self, processos):
        print(self.jsonFormatter(processos)[20])

    def jsonFormatter(self, pessoas):
        jsonFormatData = []
        for pessoa in pessoas:
            pessoa.append("")
            jsonFormatData.append({"folder_id": pessoa[0], "date": pessoa[1], "name": pessoa[2],
                                   "father": pessoa[3], "mother": pessoa[4], "obs": pessoa[5]})
        return jsonFormatData
