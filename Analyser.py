import pandas as pd


class Analyser:
    def readExcel(self):
        file = "e:\\Worksheet in D  Lesson 2019 Applied Sriptong Using Python Python Elective (IT49450) - Project_14Mar19.xls"
        data = pd.read_excel(file)
        print(data)

analyser = Analyser()
analyser.readExcel()