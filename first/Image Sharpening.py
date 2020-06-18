# -*- coding: utf-8 -*-
import cv2
import numpy as np
import math



image = cv2.imread('cat.png', cv2.IMREAD_GRAYSCALE)
# cv2.imshow('sa',image)

img_gaus1 = cv2.GaussianBlur(image, (1,1), 0)
cv2.imwrite('gaussian1.jpg', img_gaus1)

h = image - img_gaus1
for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        try:
            h[i][j] = int(image[i][j]) - int(img_gaus1[i][j])
        except:
            print(h[i][j],image[i][j],img_gaus1[i][j])

# cv2.imwrite('h.jpg', h)

addition = h * 1.25
cv2.imwrite('addition.jpg', img_gaus1)

the_sum = addition + image

c = the_sum[0][0]
d = the_sum[0][0]

for i in range(the_sum.shape[0]):
    for j in range(the_sum.shape[1]):
        if c > the_sum[i][j]:
            c = the_sum[i][j]
        if d < the_sum[i][j]:
            d = the_sum[i][j]
a=0
b=255


for i in range(the_sum.shape[0]):
    for j in range(the_sum.shape[1]):
        the_sum[i][j]=(the_sum[i][j]-c)*(b-a)/(d-c)

cv2.imwrite('O.jpg', the_sum)