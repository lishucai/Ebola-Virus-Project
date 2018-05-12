## model.py

This program creates both a linear regression model and a gaussian model using the data from a text file provided by the user. It also calculates the sum squared error, calculates leave one out cross validation and graphs both models. When this program is run the only input it takes is the name of the file that contains all of the data (see allTemps.txt) and then it outputs the sum squared error, leave one out cross validation and graphs for both modles. 

*NOTE* This program produces many warnings. This is because our client requested that we use some libraries that are outdated and therefore produce warnings when used. 

## allTemps.txt

This is the text file that contains all of our data. It can be named anything as long as it is in the same directory as model.py and the correct name is given to model.py when it is run. This file must be formatted with the skin temperature, then a space, then the core temperature of the same person and then the following lines should be in the same format but each line is for a different person or the same person at a different time. The skin temperatures should come from the image processing code and the core temperatures should be measured with a thermometer.

