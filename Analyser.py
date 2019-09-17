import pandas as pd
import matplotlib as matplt
from matplotlib import pyplot as plt
from matplotlib import rcParams
import numpy as np

class Analyser:
    def readExcel(self):
        rcParams.update({'figure.autolayout':True})
        file = "e:\\Worksheet in D  Lesson 2019 Applied Sriptong Using Python Python Elective (IT49450) - Project_14Mar19.xlsx"
        data = pd.read_excel(file)
        data.columns.values[0]='date'
        printdata = data.iloc[400:410,0:3]
        print(printdata)
        printdata.set_index('date').plot(kind='bar')
        plt.show()

analyser = Analyser()
analyser.readExcel()
