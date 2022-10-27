import re
import csv


class d:
    def d(self, processos):
        data = processos[1:]
        return (self.distByAddress(data))

    def distByAddress(self, data):
        distByAddress = {}
        for person in data:
            address = person[7]
            if address not in distByAddress:
                distByAddress[address] = 0
            distByAddress[address] += 1
        return distByAddress
