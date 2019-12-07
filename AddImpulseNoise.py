import numpy as np
import cv2
from itertools import product
from random import random
img = cv2.imread("Mono-Image2/512X512/Aerial2.bmp", 0)
height, width = img.shape
amount = 0.008
img = img.copy()

for y, x in product(*map(range, (height, width))):
    r = random()
    if r < amount:
        img[y, x] = 0

cv2.imwrite("Result/impulse_noise.png", img)
