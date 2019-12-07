import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread("Result/impulse_noise.png", 0)

blur = cv2.blur(img, (5, 5))
plt.imshow(blur, cmap="gray")
plt.xticks([]), plt.yticks([])
plt.savefig('Result/blur_img')
plt.clf()

plt.subplot(121)
plt.imshow(img, cmap="gray")
plt.title("Original")
plt.xticks([]), plt.yticks([])
plt.subplot(122)
plt.imshow(blur, cmap="gray")
plt.title("Smoothed")
plt.xticks([]), plt.yticks([])
plt.savefig('Result/smoothing_compare_img', bbox_inches='tight')
