import os
import sys
import reader
import matplotlib.pyplot as plt

#Getting file name of the data
fName = sys.argv[1]
print fName

#using a reader module to grab the data and put them into lists.
#grabbing the measured data and the correctness data.
data = reader.readData(fName)
measured = data[0]
correct = data[2]

#Creating lists for the false positive rate and the true postive rate.
fpr = list()
tpr = list()

#sorting them in decending order using zip.
#First pairs them, then sorts then unpacks them into two lists.
measured, correct = (list(t) for t in (zip(*sorted(zip(measured, correct), reverse = True))))

#counting the total number of correct and incorrect readings.
totalCorrect = correct.count('Y')
totalIncorrect = len(correct) - totalCorrect

#Accounting for if there are no correct readings, or incorrect readings
if(totalCorrect == 0):
    totalCorrect = 1

if(totalIncorrect == 0):
    totalIncorrect = 1

#Initial setup for the calculations
xCount = 0
yCount = 0

#Appending (0,0) to the list.
fpr.append(0.0)
tpr.append(0.0)

#Calculating the ROC curve
#If it sees a Y then the true positive count is increased
#Else it increases the false positve count.
#appends the currecnt value of both the true positive and false positive to the lists.
for i in range(len(measured)):
    if(correct[i] == 'Y'):
        yCount += 1
    else:
        xCount += 1
    tpr.append(float(yCount)/totalCorrect)
    fpr.append(float(xCount)/totalIncorrect)

#Appending the point (1,1) to the list.
fpr.append(1.0)
tpr.append(1.0)

#Plotting the curve
plt.scatter(fpr, tpr)
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")

#plotting a line for reference. The line is y = x.
plt.plot([0,1])

#showing the plot.
plt.show()

