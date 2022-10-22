import re
import csv


class ex2c:
    def __init__(self):
        data = self.parser()
        data = data[1:]  # aqui ficam tudo menos os indicadores
        return self.distByAgeAndGender(data)

    def distByAgeAndGender(self, data):
        dist = {"<35": {}, ">=35": {}}
        ageIndex = 5  # tentar generalizar estes indices com um interpretador
        genderIndex = 6
        for person in data:
            ageRange = ">=35"
            if int(person[ageIndex]) < 35:
                ageRange = "<35"
            if person[genderIndex] not in dist[ageRange]:
                dist[ageRange][person[genderIndex]] = 0
            dist[ageRange][person[genderIndex]] += 1
        return dist

    def parser(self):
        parsedData = []
        with open('./TP1/ex2/emd.csv', newline='') as file:
            data = csv.reader(file, delimiter=' ', quotechar='|')
            for line in data:
                parsedData.append(re.split(",", line[0]))
        return parsedData


ex2c()
