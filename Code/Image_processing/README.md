## images2.py

This program can be used to process a CSV file and produce a mean value from it. The CSV should hold the temperature data from a thermal image.
The temperatures should be in Celsius. The program will find where the head of the person in the image begins and produce the mean of the head values.


## To run the code

You can either hard code a folder of CSV files in the code or you can define the folder as a command line argument. If you supply a folder at run time the code will use the folder specified in the code.

Run: python images2.py <optional folder path>

## Output

The code produces a CSV file that holds all the mean values of the CSV files in the folder. In DEBUG mode the code doesn't create a file but it prints out the mean values of each file followed by the name of the file. This can help when trying to train the model. Printing the filename would help to match the calculated temperature with the temperature given by the thermometer.
