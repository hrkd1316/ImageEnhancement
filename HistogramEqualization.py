import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread("Mono-Image2/512X512/Aerial2.bmp", 0)

plt.hist(img.ravel(), 256, [0, 256])
plt.savefig('Result/normal_hist', bbox_inches='tight')
plt.clf()

equ = cv2.equalizeHist(img)
cv2.imwrite('Result/equ_img.png', equ)

plt.hist(equ.ravel(), 256, [0, 256])
plt.savefig('Result/equ_hist', bbox_inches='tight')
plt.clf()

plt.subplot(121)
plt.imshow(img, cmap="gray")
plt.title("Original")
plt.xticks([]), plt.yticks([])
plt.subplot(122)
plt.imshow(equ, cmap="gray")
plt.title("Equalized")
plt.xticks([]), plt.yticks([])
plt.savefig('Result/equalizing_compare_img', bbox_inches='tight')
plt.clf()

plt.subplot(121)
plt.hist(img.ravel(), 256, [0, 256])
plt.title("Original")
plt.xticks([]), plt.yticks([])
plt.subplot(122)
plt.hist(equ.ravel(), 256, [0, 256])
plt.title("Equalized")
plt.xticks([]), plt.yticks([])
plt.savefig('Result/equalizing_compare_hist', bbox_inches='tight')
plt.clf()
