This program creates fake data.
It is run by command line arguments.
It it is run by this command: python fakeDataGenerator.py <minMeasured>
<maxMeasured> <minReal> <maxReal> <number of samples>

where minMeasured and maxMeasured is the range of temperatures for the
measured temperature.
minReal and maxReal is the range of temperatures for the real temperature.
and number of samples is the amount of data created.

An example to run this is: python fakeDataGenerator.py 30.4 40.3 31.2 42.5 25

This will create 25 lines of data. Where the measured temperature will range
from 30.4C to 40.3C and the real temperature will range from 31.2C and 42.5C

To run the reader program run: python reader.py <text file>

this will print out the data in a list.
