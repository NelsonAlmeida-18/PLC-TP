import re

class ex3:
    def __init__(self):  #ver a abertura do file.txt e os prints nao tao bem
        file = open("processos.txt", "r")
        pessoas = []
        for line in file.readlines():
            pessoas.append(re.split("::", line))
        file.close()
        self.tiposParentesco(pessoas)
        return None

    def tiposParentesco(self,pessoas):
        tipos = {}  # iremos obter algo como -> { pai:5, tio:50, ...}   key -> parentesco  values-> nº elems de cada parentesco
        for pessoa in pessoas:
            for elem in pessoa:         #Com [PMTISAFNB] obtemos todas as iniciais dos tipos de parentesco 
                parent = re.findall(r'(?<=[a-z]\,)([PMTISANB][A-Za-z ]+|Filho|Filhos)(?=\.)',elem)
                for x in parent:
                    if x in tipos.keys():
                        #incrementamos o nº desse parentesco
                        tipos[x]= tipos.get(x, 0) + 1
                    else:
                        #adicionamos essa key e value inicial = 1
                        tipos[x]=1
        print(tipos)
        return tipos
ex3()


#Falta agora tirar Parente caso nao seja um grau de parentesco

#1780-04-21::Bento Jose Gomes::Jose Manuel::Angela Fernandes::Francisco Goncalves,Primo Materno. Proc.29163.     Francisco Pereira Minado,Parente. Pro
#1377::1731-06-06::Francisco Bernardo Sa Sotomaior::Miguel Cunha::Tecla Maria Sa Sotomaior::Em Anexo: Varios Documentos.   Ver Inquiricao de Pedro Pereira Lago,Parente.Proc.7330.::
#1377::1731-06-06::Francisco Bernardo Sa Sotomaior::Miguel Cunha::Tecla Maria Sa Sotomaior::Em Anexo: Varios Documentos.   Ver Inquiricao de Pedro Pereira Lago,Parente.Proc.7330.::
#1268::1727-10-16::Francisco Pereira Minado::Alexandre Fernandes::Domingas Goncalves::Bento Jose Gomes,Parente. Proc.31762.::