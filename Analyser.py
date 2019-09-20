import pandas as pd
import matplotlib as matplt
from matplotlib import pyplot as plt
from matplotlib import rcParams
import numpy as np

class Analyser:
    asia = [' Brunei Darussalam ', ' Indonesia ', ' Malaysia ', \
            ' Philippines ', ' Thailand ', ' Viet Nam ', ' Myanmar ', ' Japan ', \
            ' Hong Kong ', ' China ', ' Taiwan ', ' Korea, Republic Of ', ' India ', \
            ' Pakistan ', ' Sri Lanka ', ' Saudi Arabia ', ' Kuwait ', ' UAE ']
    # ' United Kingdom ', ' Germany ', ' France ', ' Italy ', ' Netherlands ',
    # ' Greece ', ' Belgium & Luxembourg ', ' Switzerland ', ' Austria ',
    # ' Scandinavia ', ' CIS & Eastern Europe ', ' USA ', ' Canada ',
    # ' Australia ', ' New Zealand ', ' Africa '],' India','Pakistan','Sri Lanka']
    def readExcel(self):
        file = "e:\\Worksheet in D  Lesson 2019 Applied Sriptong Using Python Python Elective (IT49450) - Project_14Mar19.xlsx"
        data = pd.read_excel(file,header=0,index_col=0)
        data = data.replace(' na ', 0)
        #print(data)
        #data.columns.values[0]='date'
        self.parsed_data=data[self.asia]
        print(self.parsed_data)

    def conDataByYears(self):
        #datablock = self.parsed_data[self.asia].iloc[400:420]
        datablock = self.parsed_data
        print(datablock)
        year=0
        oldYear = 0
        y = -1
        appendRows = False
        yearRange = range(1988,1998)
        self.con_df = None

        for i in range(len(datablock.index)):
            date = datablock.index[i]
            year = int(date.split()[0])

            if(year in yearRange):
                row = datablock.iloc[[i]].values
                nprow = np.array(row)
                print("date and row read")
                print(date)
                print(nprow)
                appendRows = False

                if (y == -1):
                    print('init')
                    nprowTotal = nprow

                if(year == oldYear):
                    print("Add nprows")
                    #nprowTotal = nprowTotal+nprow
                    nprowTotal = nprowTotal + nprow
                    #print(nprow)
                    print(nprowTotal)
                else:
                    print("Join date")
                    nprowTotalWithDate = np.append(oldYear,nprowTotal)
                    print(nprowTotalWithDate)
                    if(y==0):
                        nprows = [nprowTotalWithDate]
                        print(nprows)
                    elif(y>0):
                        nprows = np.append(nprows, [nprowTotalWithDate],axis=0)
                        print(nprows)

                    y += 1
                    oldYear = year
                    appendRows = True
                    nprowTotal = nprow

        if(appendRows==False and y!=-1):
            print("Last Join date")
            nprowTotalWithDate = np.append(oldYear, nprowTotal)
            print(nprowTotalWithDate)
            nprows = np.append(nprows, [nprowTotalWithDate], axis=0)

        if(y!=-1):
            print(nprows)
            self.con_df = pd.DataFrame(data=nprows,columns=['date']+self.asia)
            print(self.con_df)

    def plotData(self):
        # printdata = data[asia].iloc[400:410,0:3]
        if(self.con_df is not None):
            rcParams.update({'figure.autolayout': True})
            self.con_df.set_index('date', inplace=True)
            trans_df = self.con_df.transpose()
            print('plot data transpose')
            print(trans_df)
            self.con_df.plot(kind='bar')
            # data.set_index('date').plot(kind='bar')
            plt.show()

analyser = Analyser()
analyser.readExcel()
analyser.conDataByYears()
analyser.plotData()
