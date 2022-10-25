import re


class b:
    def __init__(self, processos):
        print(self.nomesPorSeculo(processos))

    def nomesPorSeculo(self, processos):
        dic = {"firstNames": {}, "lastNames": {}}
        for processo in processos:
            ano = re.match("(([0-9]{1,4})-*)", processo[1]).group(2)
            sec = int(ano)//100 + 1
            if sec not in dic["firstNames"]:
                dic["firstNames"][sec] = {}
                dic["lastNames"][sec] = {}
            i = 2
            while (i <= 4):
                names = re.split(" ", processo[i])
                fstName = names[0]
                lastName = names[-1]
                if fstName not in dic["firstNames"][sec]:
                    dic["firstNames"][sec][fstName] = 0
                if lastName not in dic["lastNames"][sec]:
                    dic["lastNames"][sec][lastName] = 0
                dic["firstNames"][sec][fstName] += 1
                dic["lastNames"][sec][lastName] += 1
                i += 1
        return dic
