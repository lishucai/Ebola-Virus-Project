import numpy as np
import cv2
from os import listdir  # to get all files in a directory
from os.path import isfile, join
import os
import sys
# import matplotlib.pyplot as plt
import csv

#this function is used to correct the values in the CSV file. It finds the minimum values in
# the double list and substruct it from all the values in the list. This is done to help with the calibration
#of the camera.
def correcting_values(temperatureData):
    #setting intitial values so everythign would be smaller
    min_value = 1000
    #goes through the list to fin the absolute minimum
    for elements in temperatureData:
        temp_min_value = min(elements)
        if temp_min_value < min_value:
            min_value = temp_min_value
    # min_value = min(temperatureData)
    if DEBUG:
        print min_value
    #substruct the minimum value from all values
    for row_counter, elements in enumerate(temperatureData):
        for column_counter, element in enumerate(elements):
            element = element - min_value
            temperatureData[row_counter][column_counter] = element
            # [float(i)-min_value for i in elements]
            # print temperatureData[row][column]
    #returns the new list with changed values
    return temperatureData

#The following funciton finds the point where the head begings. It does that be looking throught the array until it
#finds five values in a row that are in the right range (30-45) then it returns a list with two variables [y,x]
# y is the row where the ead begins and x is the column. If it doesn't find the head it returns an empty list

def starting_point(temperatureData):
    for row_counter, elements in enumerate(temperatureData):
        for column_counter, element in enumerate(elements):
            if element < 45 and element > 30:
                good = []
                for iterator in range(1, 5):
                    # print len(elements)
                    if (column_counter + iterator) < len(elements):
                        if elements[column_counter + iterator] < 45 and elements[column_counter + iterator] > 30:
                            # print "added to good"
                            good.append(iterator)
                # print len(good)
                if len(good) == 4:
                    # print "in"
                    cordinates = []
                    cordinates.append(row_counter)
                    cordinates.append(column_counter)
                    return cordinates
    return []



#This function returns the mean of the head values.
#It recieves the following:
# X and Y the values from the starting point function
#WIDTH AND HEIGHT - variable that are hard coded from absorbing the images. If the person is about 2 meters from
#the camera the head in the picture is about 40 columns wide and 30 rows long
#temperatureData is the array with the temperature values

def get_mean(x, y, WIDTH, HEIGHT, temperatureData):
    if ((y + HEIGHT) > 120 or ((x + (WIDTH / 2)) > 160)):
        print "PERSON OUT OF RANGE"
        return 0
    for row in range(y, (y + HEIGHT)):
        # y is the row it begins, h is the width of the length of the head
        for column in range(x - (WIDTH / 2), x + (WIDTH / 2)):
            if (temperatureData[row][column] > 43 or temperatureData[row][column] < 35):
                continue
            else:
                good_range.append(temperatureData[row][column])
    if (len(good_range) == 0):
        return 0
    range_mean = sum(good_range) / float(len(good_range))
    return range_mean



if __name__ == '__main__':
    '''
       The following program processes a CSV file and outputs one float values.
       The CSV file should hold temp values and should not be empty.
       The program trasfers the CSV file into a double list and then processes the information in the list.
       Overall it finds the head of the person in the csv file and averages the temperatures that belong to the head.
       the directory should hold the csv files that you want to process
       '''

    # can set the file name in the command lind, just need to uncomment this MYPATH and comment out the hard coded one.
    if (len(sys.argv) == 1):
        MYPATH = 'C:\Users\Tair\Documents\Pictures\Real\Resting'
    elif (len(sys.argv)==2):
        MYPATH = str(sys.argv[1])
    
    #MYPATH = './Real/resting'
    FILES_NUM = 0
    # we hard coded the size of the head in the image. If the person is about 2 meter from the camera its about 30
    # rows long and about 40 columns wide. You should change these values if you think the head is in a different
    # size in you images.
    HEIGHT = 30
    WIDTH = 40
    # set DEBUG to 1 to use specific DEBUG functionalities. It will have more print statments and will not print a
    # single number
    DEBUG = 0

    #setting all nessesery parameters. x and y will hold the point where the head begins
    y = 0
    x = 0
    csv_list = []
    tiff_list = []
    invalid_file_type = []

    # getting the names of all the files in a directory
    getfiles = [f for f in listdir(MYPATH) if
                isfile(join(MYPATH, f))]  # a list of all the file in a folder specified by MYPATH
    #going over all the files in the directory. Putting all the CSV file names in one list and tiff file names in
    #another. We don't do anything with the tiff files but we left it incase someone want's to process them too.
    for f in getfiles:
        if (f.endswith(".tiff")):  # Add more if statements as necessary for more file types
            tiff_list.append(f)
        elif (f.endswith(".csv")):
            csv_list.append(f)
        else:
            invalid_file_type.append(f)
    # a loop that goes through all the csv file. It will process each csv file by itself.
    for c in csv_list:
        temp_file = join(MYPATH, c)  # getting the file with the path, file name is in c
        temperatureData = list()
        tempList = []
        #open csv file for read and trasnfer it into a two dimentional array. Each row is a list.
        # And the temperatureData list holds a list of the rows.
        with open(temp_file, 'rb') as f:
            data = csv.reader(f, delimiter=',')
            for row in data:
                tempList = []
                for temp in row:
                    if (temp == '\n'):
                        pass
                    else:
                        tempList.append(float(temp))
                temperatureData.append(tempList)
        temperatureData = correcting_values(temperatureData)
        # print len(temperatureData[0])
        good_range = []

        # y = 15
        # x = 75
        cordinates = []

        #cordinate will hold a list of two variables. y which is the hight of where the head begins and x which is the column
        # where the head begins
        cordinates = starting_point(temperatureData)
        if not cordinates:
            print "error! list of cordinates is empty"

        if DEBUG:
            print 'row number is %d, column number is %d ' % (cordinates[0], cordinates[1])

        y = cordinates[0]
        x = cordinates[1]

        #if you set FILE_IS_GOOD to 1, it will use the normal get_mean. If you set it to 0 it would use the bad file get mean
        #which uses a different range.

        range_mean = get_mean(x, y, WIDTH, HEIGHT, temperatureData)


        if DEBUG:
            print 'mean: %f range_mean %s' % (range_mean, c)
        else:
            #prints the calculated mean into a CSV file.
            with open('resting.csv', 'a') as file:
                
                file.write(str(range_mean) + "," + c )

                file.write('\n')
            # print '%0.2f %s' %(range_mean, c)
