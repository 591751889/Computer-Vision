import cv2

import numpy as np

img = cv2.imread("Cells.png")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

I = gray

n = 20


def max_filter(img, n):
    row, column = img.shape

    pad = int(n / 2)

    max_f = np.zeros((row + pad * 2, column + pad * 2))

    max_f[pad: pad + row, pad: pad + column] = gray.copy()

    tmp = max_f.copy()

    for y in range(row):

        for x in range(column):
            max_f[pad + y, pad + x] = np.max(tmp[y: y + n, x: x + n])

    max_f = max_f[pad: pad + row, pad: pad + column].astype(np.uint8)

    return max_f


def min_filter(img, n):
    row, column = img.shape

    # Zero padding

    pad = n // 2

    min_f = np.zeros((row + pad * 2, column + pad * 2), dtype=np.float)

    min_f[pad: pad + row, pad: pad + column] = gray.copy().astype(np.float)

    tmp = min_f.copy()

    for y in range(row):

        for x in range(column):
            min_f[pad + y, pad + x] = np.min(tmp[y: y + n, x: x + n])

    min_f = min_f[pad: pad + row, pad: pad + column].astype(np.uint8)

    return min_f


A = min_filter(gray, n)
cv2.imwrite("A.jpg", A)

B = max_filter(A, n)
cv2.imwrite("B.jpg", B)

O = I - B
cv2.imwrite("O.jpg", O)
