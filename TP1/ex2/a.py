import re
import pandas as pd
import matplotlib.pyplot as plt


class a:
    def a(self, file):
        datas = [i[2] for i in file]
        file = open("./TP1/ex2/1/website/a.html", "w")
        templateText = '''<!DOCTYPE html >
<html lang = "en" >
<head >
    <meta charset = "UTF-8" >
    <meta http-equiv = "X-UA-Compatible" content = "IE=edge" >
    <meta name = "viewport" content = "width=device-width, initial-scale=1.0" >
    <title >a</title >
    <link rel="stylesheet" href="./main.css">
</head >
<body >
</body >
</html >'''
        newText = re.sub(
            "<body >", f'''\n<body >\n<p class="title">Datas extremas dos registos no dataset</p>\n<p class="minData">Extremo inferior do dataset: {min(datas)}</p>\n<p class="maxData">Extremo superior do dataset: {max(datas)}</p>''', templateText)
        file.write(newText)
        file.close()
