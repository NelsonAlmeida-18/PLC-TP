import re
import csv


class c:
    def c(self, processos):
        data = processos[1:]  # aqui ficam tudo menos os indicadores
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
