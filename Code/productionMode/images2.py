import numpy as np
import cv2
from os import listdir  # to get all files in a directory
from os.path import isfile, join
import os
import sys
# import matplotlib.pyplot as plt
import csv

good_range = list()


def correcting_values(temperatureData):
    min_value = 1000
    for elements in temperatureData:
        temp_min_value = min(elements)
        if temp_min_value < min_value:
            min_value = temp_min_value
    # min_value = min(temperatureData)
    # if DEBUG:
    #    print min_value
    for row_counter, elements in enumerate(temperatureData):
        for column_counter, element in enumerate(elements):
            element = element - min_value
            temperatureData[row_counter][column_counter] = element
            # [float(i)-min_value for i in elements]
            # print temperatureData[row][column]

    return temperatureData


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


def starting_point_bad_file(temperatureData):
    for row_counter, elements in enumerate(temperatureData):
        for column_counter, element in enumerate(elements):
            if element < 50 and element > 30:
                good = []
                for iterator in range(1, 5):
                    # print len(elements)
                    if (column_counter + iterator) < len(elements):
                        if elements[column_counter + iterator] < 50 and elements[column_counter + iterator] > 30:
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


def get_mean(x, y, WIDTH, HEIGHT, temperatureData):
    if ((y + HEIGHT) > 120):
        print "PERSON OUT OF RANGE"
        return 0
    if ((x + (WIDTH / 2)) > 160):
        print "PERSON OUT OF RANGE"
        return 0
    for row in range(y, (y + HEIGHT)):
        # y is the row it begains, h is the width of the length of the head
        for column in range(x - (WIDTH / 2), x + (WIDTH / 2)):
            if (temperatureData[row][column] > 43 or temperatureData[row][column] < 35):
                continue
            else:
                good_range.append(temperatureData[row][column])

    if (len(good_range) == 0):
        return 0

    range_mean = sum(good_range) / float(len(good_range))
    return range_mean


def get_mean_bad_file(x, y, WIDTH, HEIGHT, temperatureData):
    for row in range(y, (y + HEIGHT)):
        # y is the row it begains, h is the width of the length of the head
        for column in range(x - (WIDTH / 2), x + (WIDTH / 2)):
            if (temperatureData[row][column] > 50 or temperatureData[row][column] < 30):
                continue
            else:
                good_range.append(temperatureData[row][column])

    range_mean = sum(good_range) / float(len(good_range))
    return range_mean


# MYPATH = 'C:\Users\Tair\Documents\Pictures\Real\Running'
# MYPATH = 'nfs/stak/users/maimonc/Ebola-Virus-Project/Code/Image_processing\Real\Running'
# MYPATH = './Real/resting'

def processImages():
    MYPATH = "./Images"
    FILES_NUM = 0
    HEIGHT = 30
    WIDTH = 40
    DEBUG = 0
    FILE_IS_GOOD = 1
    y = 0
    x = 0
    csv_list = []
    tiff_list = []
    invalid_file_type = []
    # getting the names of all the files in a directory
    getfiles = [f for f in listdir(MYPATH) if
                isfile(join(MYPATH, f))]  # a list of all the file in a folder specified by MYPATH

    for f in getfiles:
        if (f.endswith(".tiff")):  # Add more if statements as necessary for more file types
            tiff_list.append(f)
        elif (f.endswith(".csv")):
            csv_list.append(f)
        else:
            invalid_file_type.append(f)

    print "IMAGES PROCESSED"
    print csv_list

    temperatureMeans = list()
    for c in csv_list:
        # print c
        temp_file = join(MYPATH, c)  # getting the file with the path, file name is in c
        temperatureData = list()
        tempList = []
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
        # print(len(temperatureData))
        # print(len(temperatureData[0]))
        # print len(temperatureData[0])
        good_range = []

        # y = 15
        # x = 75
        cordinates = []
        cordinates = starting_point(temperatureData)
        if not cordinates:
            print "ERROR! NO VALID DATA. CAN NOT FIND PERSON"
            return [0]

        if DEBUG:
            print 'row number is %d, column number is %d ' % (cordinates[0], cordinates[1])

        # if(len(cordinates) == 0):
        #	return 0

        y = cordinates[0]
        x = cordinates[1]

        if FILE_IS_GOOD:
            temperatureMeans.append(get_mean(x, y, WIDTH, HEIGHT, temperatureData))

    return temperatureMeans


'''		
	    else:
		range_mean = get_mean_bad_file(  x,y,WIDTH, HEIGHT, temperatureData)
'''

'''
	    if DEBUG:
		print 'mean: %f range_mean %s' % (range_mean, c)
	    else:
	       with open('resting.csv', 'a') as file:
		     file.write(str(range_mean))
		     file.write('\n')
		#print '%0.2f %s' %(range_mean, c)
	    return temeratureMeans	
'''
