import cv2

import numpy as np

n = 12
img = cv2.imread("Particles.png")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

I = gray


def max_filter(img):
    row, column = img.shape

    pad = int(n / 2)

    max_f = np.zeros((row + pad * 2, column + pad * 2))

    max_f[pad: pad + row, pad: pad + column] = gray.copy()

    tmp = max_f.copy()
    max = 0
    for y in range(row):
        for x in range(column):
            # for i in range(n):
            #     for j in range(n):
            #         if max<tmp[y+i][x+j]:
            #             max=tmp[y+i][x+j]
            max_f[pad + y, pad + x] = np.max(tmp[y: y + n, x: x + n])

    max_f = max_f[pad: pad + row, pad: pad + column]

    return max_f


def min_filter(img):
    row, column = img.shape

    pad = int(n / 2)

    min_f = np.zeros((row + pad * 2, column + pad * 2))

    min_f[pad: pad + row, pad: pad + column] = gray.copy()

    tmp = min_f.copy()
    max = 0
    for y in range(row):
        for x in range(column):
            # for i in range(n):
            #     for j in range(n):
            #         if max<tmp[y+i][x+j]:
            #             max=tmp[y+i][x+j]
            min_f[pad + y, pad + x] = np.min(tmp[y: y + n, x: x + n])

    min_f = min_f[pad: pad + row, pad: pad + column]

    return min_f


A = max_filter(gray)

cv2.imwrite("A.jpg", A)

B = min_filter(A)
cv2.imwrite("B.jpg", B)

O = I - B
cv2.imwrite("O.jpg", O)
