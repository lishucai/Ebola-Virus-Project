import numpy as np
import cv2
from os import listdir #to get all files in a directory
from os.path import isfile, join
import os
import sys
import matplotlib.pyplot as plt
import csv


MYPATH = 'C:\Users\Tair\Documents\pictures'
FILES_NUM = 0
csv_list = []
tiff_list = []
invalid_file_type = []
#getting the names of all the files in a directory
getfiles = [f for f in listdir(MYPATH) if isfile(join(MYPATH,f))] # a list of all the file in a folder specified by MYPATH

for f in getfiles:
    if(f.endswith(".tiff")):#Add more if statements as necessary for more file types
        tiff_list.append(f)
    elif(f.endswith(".csv")):
        csv_list.append(f)
    else:
        invalid_file_type.append(f)


#if the file is a tiff file
for i in tiff_list :
    #making it easy to read between images
    print()
    print()
    print()
    print()
    print()
    print()
    print(i)
    print()
    print()
    print()
    print()
    print()
    print()

    #joining the path and the specific file in this loop
    temp_file = join(MYPATH,i)
    #reading in the image
    img = cv2.imread(temp_file,cv2.IMREAD_ANYCOLOR | cv2.IMREAD_ANYDEPTH)

   
    #shows the image until you press a keyboard
    cv2.imshow('image',img)
    cv2.waitKey(1000)
    cv2.destroyAllWindows()
    
    #prints out the shape of the image
    #two values if grey, three if it's in color
    print "image shape (y and x)"
    print img.shape
    #print img.shape[0]
    #print img.shape[1]
    y = img.shape[0]
    x = img.shape[1]
    
    pixel_list = [] #the list that will hold all of the pixels' values and possition
    #for loop that goes throu the image and prints every pixle value
    sum_pixles = 0 
    for i in range (0,10): #currently just 10 because it crashes with more and take too long
        for j in range (0,10):
            px = img[i,j] #goes through the image
            temp = [i,j,px[0], px[1], px[2]] #get the three values of each pixle
            #print(temp)
            pixel_list.append(temp) #append the value to the list 
            #print(px)
            #the scale is of 0 to 255
            '''if (px > 230 or px < 50):
                sum_pixles += 0
            else:
                sum_pixles = sum_pixles +px
            
            #print(i)
            #print(j)
            #print(px)        
    print "sum of pixles: %d" %sum_pixles
    avg = sum_pixles/(y*x)
    print "avg of pixles: %d" % avg
    '''
    print(pixel_list)
    
for c in csv_list:
    temp_file = join(MYPATH,c)
    temperatureData = list()
    with open(temp_file, 'rb') as f:
        data = csv.reader(f, delimiter=';')
        for row in data:
            for temp in row:
                if(temp == ''):
                    pass
                else:
                    temperatureData.append(float(temp))
    plt.hist(temperatureData)
    plt.title("Temperature Histogram")
    plt.xlabel("Temp in C")
    plt.ylabel("Frequency")
    plt.show()
    good_range = []
    for element in temperatureData:
        if (element > 43 or element < 35):
            continue
        else:
            good_range.append(element)

    range_mean = np.mean(good_range)
    range_max = np.max(good_range)
    range_min = np.min(good_range)
    range_median = np.median(good_range)
    range_st_deviation = np.std(good_range)



    #print(good_range)
    #print(range_mean)

    print "mean: %.2f, max: %.2f, min: %.2f, median: %.2f, standard deviation: %.2f " % (range_mean, range_max, range_min, range_median, range_st_deviation)


