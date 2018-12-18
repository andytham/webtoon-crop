import os
from PIL import Image
import numpy as np

imgOpen = Image.open('images/test2.png')# import image
img = np.array(imgOpen) #convert to array

# layout
# [ [ [ 3 rgb for one pixel] ... ] one line is an array of arrays... ] then surrounded by an array of each line
# 

newImg = []
iterator = 0
# for index, line in enumerate(img):
white = 235
black = 15

for line in img:
    startingColor = [line[0][0], line[0][1], line[0][2]]
    isSolidLine = True
    for pixel in line:
        r = pixel[0]
        g = pixel[1]
        b = pixel[2]
        
        if startingColor != [r,g,b]:
            isSolidLine = False
            # print("not solid")
        # else:
            # print("solid")
    if isSolidLine == False:
        newImg.append(line.tolist())
createImg = Image.fromarray(np.uint8(np.array(newImg)))
createImg.save('./images/test.jpg')
# Image.show(createImg)
# print(np.array(newImg))
# print(newImg)
#delete white/black space

#check every pixel

#save as new image


# TODO: 
# stitch whole image? 
# pros - single file. cons - large size
# scrape and download images from a source
