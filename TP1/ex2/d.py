import re
import csv


class ex2d:
    def __init__(self):
        data = self.parser()
        data = data[1:]
        print(self.distByAddress(data))

    def distByAddress(self, data):
        distByAddress = {}
        for person in data:
            address = person[7]
            if address not in distByAddress:
                distByAddress[address] = 0
            distByAddress[address] += 1
        return distByAddress

    def parser(self):
        parsedData = []
        with open('./TP1/ex2/emd.csv', newline='') as file:
            data = csv.reader(file, delimiter=' ', quotechar='|')
            for line in data:
                parsedData.append(re.split(",", line[0]))
        return parsedData


ex2d()
