import os
import sys
import random

minMeasured = float(sys.argv[1])
maxMeasured = float(sys.argv[2])
minReal = float(sys.argv[3])
maxReal = float(sys.argv[4])
lines = int(sys.argv[5])

fo = open("fakeData.txt", "wb")

for i in range(lines):
    fo.write(str(round(random.uniform(minMeasured, maxMeasured),1)))
    fo.write(',')
    fo.write(str(round(random.uniform(minReal,maxReal),1)))
    fo.write('\n')

fo.close()

