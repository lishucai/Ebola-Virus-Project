There are three programs in this folder. reader.py fakeDataGenerator.py and
roc.py

reader.py is a module to grab data from the fake data generator.

fakeDataGenerator.py creates fake data to be used to test roc.py. It uses
command line arguments to create the data. The data created has the format
x,z,y where x is the measured data, y is the real data, and z is if it is
correct or not.

The command to run the program is: python fakeDataGenerator.py <minMeasured>
<maxMeasured> <minReal> <maxReal> <number of line> <optional argument for
precent correct>

The first four arguments are the ranges of the temperatures generated.
The fifth argument is the amount of data generated.
The last optional argument is to force a percent correctness. If no argument
is provided the it defualts to 50% correct.

An example to run this is python 0.0 100.0 0.0 100.0 100 80

This will create 100 lines of data with temperature ranges from 0 to 100 and
the data will be approximately 80% correct.


roc.py creates a roc curve using the data that is formated like data produced
by the fakeDataGenerator.py It relys on matplotlib.pyplot. Without this module
it does not work. 

The command to run roc.py is: python roc.py <Name of your data.txt>
An example is: python roc.py fakeData.txt

This will create an roc curve, and plot it to the screen using the data
provided in fakeData.txt
