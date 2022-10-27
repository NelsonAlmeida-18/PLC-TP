from os import read
import re
import csv


class e:
    def e(self, data):
        data = data[1:]
        readinessStats = {}
        # ir buscar os anos, e os aptos/total, não aptos/total
        while (data):
            year = re.match("(([0-9]{1,4})-*)", data[0][2]).group(2)
            (ready, total), newData = self.readinessPerYear(data, year)
            readinessPerc = (ready/total)
            readinessStats[year] = {
                "ready": 100*readinessPerc, "not_ready": 100*(1-readinessPerc)}
            data = newData
        return (readinessStats)

    def readinessPerYear(self, data, year):
        ready = 0
        total = 0
        newData = []
        for person in data:
            if re.match(year+r"(-[0-9]{1,2}){2}", person[2]):
                if person[-1] == "true":
                    ready += 1
                total += 1
            else:
                newData.append(person)
        return (ready, total), newData
