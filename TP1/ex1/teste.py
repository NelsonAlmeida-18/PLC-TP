import re

testes = ["1970-09-10", "1999-09-02", "1290-02-01"]
ano = "1970"
for teste in testes:
    if re.search(ano+r"-[0-9]{1,2}-[0-9]{1,2}", teste):
        print(teste)
