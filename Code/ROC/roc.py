import os
import sys
import reader
import matplotlib.pyplot as plt

def calcFalsePositive(tempList, correctnessList, thold):
    falsePositive=0
    for i in range(0,len(tempList)):
        if(tempList[i] >= thold and correctnessList[i] == 'N'):
            falsePositive += 1

    return falsePositive

        
def calcTruePositive(tempList, correctnessList, thold):
    truePositive=0
    for i in range(0,len(tempList)):
        if(tempList[i] >= thold and correctnessList[i] == 'Y'):
            truePositive += 1
    
    return truePositive

fName = sys.argv[1]
print fName

data = reader.readData(fName)
measured = data[0]
real = data[1]
correct = data[2]
fprs = list()
tprs = list()
for temp in measured:
    threshold = temp
    fp = calcFalsePositive(measured, correct, threshold)
    tp = calcTruePositive(measured, correct, threshold)
    fprs.append(float(fp)/(fp + tp))
    tprs.append(float(tp)/(fp + tp))


plt.scatter(fprs, tprs)
plt.show()
