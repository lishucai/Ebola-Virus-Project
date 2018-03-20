import os
import sys
import random

def generate(minMeasured, maxMeasured, minReal, maxReal, lines, correctness = 50):
    wrong = 100 - correctness

    correctPercent = list()
    for i in range(correctness):
        correctPercent.append('Y')
    for i in range(wrong):
        correctPercent.append('N')

    random.shuffle(correctPercent)

    fo = open("fakeData.txt", "wb")
    
    for i in range(lines):
        fo.write(str(round(random.uniform(minMeasured, maxMeasured),1)))
        fo.write(',')
        fo.write(str(round(random.uniform(minReal,maxReal),1)))
        fo.write(',')
        fo.write(random.choice(correctPercent))
        fo.write('\n')

    fo.close()





args = sys.argv[0:]

if(len(args) == 7):
    generate(float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6]))

else:
    generate(float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4]), int(sys.argv[5]))
