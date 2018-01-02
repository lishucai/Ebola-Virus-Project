import numpy as np
import cv2

# Load an color image in grayscale
#IMREAD_COLOR = 1
#IMRED_UNCHANGED = -1
#IMREAD_GRAYSCALE = 0


#reading the image, won't return an error if the path is wrong!
img = cv2.imread(r'''C:\Users\Tair\Documents\pictures\person.jpg''',0)

#shows the image until you press a keyboard
cv2.imshow('image',img)
cv2.waitKey(1000)
cv2.destroyAllWindows()
'''
#open the image in a new window
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
#getting pixle values

#getting the pixles value of [100,100]
print "getting pixle value for [100,100]"
px = img[100,100]
print(px)

#changing the pixle value of [100,100]
print "after changing pixle vlaue"
img[100,100] =255
print img[100,100]

#prints out the shape of the image
#two values if grey, three if it's in color
print "image shape (y and x)"
print img.shape[0]
print img.shape[1]
y = img.shape[0]
x = img.shape[1]

#for loop that goes throu the image and prints every pixle value
sum_pixles = 0 
for i in range (0,259):
    for j in range (0,194):
        px = img[i,j]
        #the scale is of 0 to 255
        if (px > 230 or px < 50):
            sum_pixles += 0
        else:
            sum_pixles = sum_pixles +px
        #print(i)
        #print(j)
        #print(px)        
print "sum of pixles: %d" %sum_pixles
avg = sum_pixles/(y*x)
print "avg of pixles: %d" % avg 

